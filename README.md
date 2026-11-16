# pytest-indigo
pytest-indigo is a testing frame work that is designed to allow IndigoDomo plugins to be tested without having access to an Indigo Server. The primary use case is in CI/CD applications.

## What this project is, will be, or hopes to be
### An Indigo mocking tool
This will inject an object into the Python `sys.modules` object that will let your plugin *think* it is running in an Indigo Server environment.

## What this project isn't
### A functional Indigo Server
This is a testing utility.

### A 1:1 replication of Indigo
I will try my best to **mimic** Indigo Server behavior, but this will never be perfect.

## Getting started
### 1. Install pytest-indigo
Install pytest-indigo into the environment you use to test your plugin:

```bash
pip install -e /path/to/pytest-indigo
```

pytest-indigo is a pytest plugin, so pytest loads it automatically. Once it is loaded, `import indigo` resolves to the mock, both in your plugin's code and in your tests.

### 2. Write a test
Add a test to your plugin. The [`plugin`](#plugin) fixture creates a new instance of your plugin's `Plugin` class for each test:

```python
# MyPlugin.indigoPlugin/Contents/Server Plugin/tests/test_plugin.py
import indigo


def test_plugin_loads(plugin):
    assert plugin.pluginId == "com.example.myplugin"  # Your plugin's CFBundleIdentifier
    assert indigo.activePlugin is plugin
```

### 3. Run your tests
Run pytest from the folder containing your `.indigoPlugin` bundle:

```bash
cd MyPlugin
pytest
```

pytest-indigo finds your plugin bundle, and makes its `Server Plugin` modules importable by your tests, with no configuration.

### Next steps
- [Fixtures](#fixtures): set up and inspect Indigo's state, and start your plugin with saved preferences.
- [Marks](#marks): change the Indigo Server version or your plugin's preferences for a test, class or module.
- [Type hints](#type-hints): a one-time setup so your editor knows your plugin's members in every test.
- [Configuration](#configuration): choose a plugin when your project contains more than one.

## Project setup
### Project layout
pytest-indigo expects to run from a directory containing your `.indigoPlugin` bundle:

```
MyPlugin/                     <- run pytest from here
├── pytest.toml
└── MyPlugin.indigoPlugin/
    └── Contents/
        ├── Info.plist
        └── Server Plugin/
            ├── plugin.py
            ├── mymodule.py
            └── tests/
                └── test_plugin.py
```

Indigo runs your plugin with `Server Plugin` on the Python path, which is why `plugin.py` can `import mymodule`. pytest-indigo does the same before your tests and `conftest.py` files are loaded, so your tests can `from plugin import Plugin` and `import mymodule` with no extra configuration. If the rootdir contains more than one plugin, set the [`indigo_plugin`](#configuration) ini option to choose one.

### Loading pytest-indigo without autoloading
If your project disables pytest's plugin autoloading, load pytest-indigo from your root `conftest.py`:

```python
pytest_plugins = ["pytest_indigo"]
```

In this case, `Server Plugin` is added to the path a little later: after your root `conftest.py` is loaded, but before your tests are collected. To import your plugin's modules in the root `conftest.py` too, add `Server Plugin` with pytest's `pythonpath` option:

```toml
# pytest.toml
[pytest]
pythonpath = ["MyPlugin.indigoPlugin/Contents/Server Plugin"]
```

## Fixtures
| Fixture | Provides | Override to |
|---|---|---|
| [`indigo`](#indigo) | The mocked `indigo` module, reset before and after each test | - |
| [`indigo_api_version`](#indigo_api_version) | The plugin API version reported by `indigo.server.apiVersion` | Test against a different Indigo Server version |
| [`plugin`](#plugin) | A new instance of your plugin, set as `indigo.activePlugin` | - |
| [`plugin_prefs`](#plugin_prefs) | The preferences your plugin starts with | Start your plugin with custom preferences |
| [`plugin_path`](#plugin_path) | The path to the `.indigoPlugin` bundle under test | Test a different plugin bundle |

### `indigo`
The mocked `indigo` module. This is the same object your plugin gets from `import indigo`, so you can use it to set up and inspect Indigo's state.

```python
from pytest_indigo import IndigoMock


def test_server_api_version(indigo: IndigoMock):
    assert indigo.server.apiVersion == "3"
```

Before and after each test that uses this fixture, the mock is reset: ids, devices and server state are cleared, `indigo.activePlugin` goes back to its default, and `indigo.server.apiVersion` is set from the [`indigo_api_version` mark](#indigo_api_version-mark) or [fixture](#indigo_api_version). If a test changes `indigo` state without requesting the fixture, the change leaks until the next test that requests it. Request `indigo` in any test that changes Indigo state.

### `indigo_api_version`
The Indigo Server plugin API version reported by `indigo.server.apiVersion`. Defaults to the [`indigo_api_version`](#configuration) ini option, which is `"3"` unless you configure it.

Indigo APIs that are only available in newer servers check this version, and raise an `ApiVersionException` when the mocked server is too old. Use it to check that your plugin works with every Indigo version it supports.

To change the version for every test, set the ini option:

```toml
# pytest.toml
[pytest]
indigo_api_version = "3.4"
```

To change the version for a test, class or module, use the [`indigo_api_version` mark](#indigo_api_version-mark):

```python
import pytest


@pytest.mark.indigo_api_version("2.4")
def test_old_server(plugin):
    plugin.startup()
```

To run a test against several versions, parametrize `indigo_api_version` directly:

```python
@pytest.mark.parametrize("indigo_api_version", ["3.0", "3.4", "3.6"])
def test_startup(plugin):
    plugin.startup()
```

You can also override the fixture, for example in a `conftest.py` to change the version for all tests in a directory:

```python
import pytest


@pytest.fixture()
def indigo_api_version():
    return "2.4"
```

The fixture's value is the version used when no mark applies. To check the version a test actually runs against, read `indigo.server.apiVersion`.

### `plugin`
A new instance of your plugin's `Plugin` class, created the same way the Indigo plugin host creates it:

1. The plugin id (`CFBundleIdentifier`), display name (`CFBundleDisplayName`) and version (`PluginVersion`) are read from `Info.plist`.
2. `Contents/Server Plugin/plugin.py` is imported as the top-level `plugin` module, so `from plugin import Plugin` in your tests refers to the same class.
3. `Plugin(plugin_id, display_name, version, plugin_prefs)` is called, using [`plugin_prefs`](#plugin_prefs).
4. `plugin_folder_path` is set to the bundle path and the plugin is assigned to `indigo.activePlugin`.

Each test gets its own instance.

```python
def test_plugin_id(plugin):
    assert plugin.pluginId == "com.example.myplugin"
```

`startup()` is **not** called, so your tests control when, or if, the plugin starts:

```python
def test_startup(plugin):
    plugin.startup()
    ...
```

Your `Plugin.__init__()` and `startup()` run against the mock, so they can only use the parts of Indigo that pytest-indigo implements. Calling something that is missing raises an `AttributeError` or a `NotImplementedException`. See [INDIGO_COVERAGE.md](INDIGO_COVERAGE.md) for what is available.

#### Testing configuration UI callbacks
Pass an `indigo.Dict` to UI callbacks, just like Indigo does:

```python
import indigo


def test_validate_prefs_rejects_negative_timeout(plugin):
    is_valid, values_dict, errors = plugin.validatePrefsConfigUi(
        indigo.Dict({"timeout": "-1"})
    )

    assert not is_valid
    assert "timeout" in errors
```

#### Logging
`plugin.logger` behaves like it does in Indigo, including the `threaddebug()` level. Messages at the Indigo log handler's level (INFO, or DEBUG when `plugin.debug` is `True`) are forwarded to `indigo.server.log`. To make assertions about log messages, use pytest's `caplog` fixture:

```python
import logging


def test_logs_warning(plugin, caplog):
    with caplog.at_level(logging.WARNING, logger="Plugin"):
        plugin.do_something_risky()

    assert "risky" in caplog.text
```

### `plugin_prefs`
The preferences passed to your plugin when [`plugin`](#plugin) creates it. Defaults to an empty `indigo.Dict`.

A plain `dict` is converted to an `indigo.Dict` before it reaches your plugin.

To start your plugin with saved preferences for a test, class or module, use the [`indigo_plugin_prefs` mark](#indigo_plugin_prefs-mark):

```python
import pytest


@pytest.mark.indigo_plugin_prefs({"log-level": "debug", "timeout": "30"})
def test_debug_logging(plugin):
    assert plugin.pluginPrefs["log-level"] == "debug"
```

To share preferences across a directory, override the fixture in a `conftest.py`:

```python
import pytest


@pytest.fixture()
def plugin_prefs():
    return {"log-level": "debug", "timeout": "30"}
```

To run a test once per set of preferences, parametrize `plugin_prefs` directly:

```python
@pytest.mark.parametrize(
    "plugin_prefs",
    [
        {},  # A new install, before the preferences have been saved
        {"timeout": "30"},
    ],
)
def test_startup(plugin):
    plugin.startup()
```

pytest-indigo does not apply the `defaultValue`s from `PluginConfig.xml` to these preferences. Testing with an empty `plugin_prefs` is a good way to check how your plugin behaves after an upgrade adds new preferences.

### `plugin_path`
The path to the `.indigoPlugin` bundle that [`plugin`](#plugin) loads. It is resolved in this order:

1. The `indigo_plugin` ini option, if it is set (see [Configuration](#configuration)).
2. The only `.indigoPlugin` bundle found under the pytest rootdir. If there is no bundle, or more than one, a `PytestIndigoException` is raised.

To test a different bundle, override the fixture:

```python
import pytest


@pytest.fixture()
def plugin_path(request):
    return str(request.config.rootpath / "fixtures" / "Other.indigoPlugin")
```

## Marks
Marks set fixture values for a single test, a class, or a whole module. All pytest-indigo marks are prefixed with `indigo_`, and they are registered, so they work with `--strict-markers`.

| Mark | Sets | Used by |
|---|---|---|
| [`indigo_api_version(version)`](#indigo_api_version-mark) | The plugin API version reported by `indigo.server.apiVersion` | [`indigo`](#indigo) |
| [`indigo_plugin_prefs(prefs)`](#indigo_plugin_prefs-mark) | The preferences your plugin starts with | [`plugin`](#plugin) |

Apply a mark to a test function, to a class to cover all of its tests, or to a module with `pytestmark`:

```python
import pytest

pytestmark = pytest.mark.indigo_api_version("3.4")  # Every test in this module


def test_uses_module_version(indigo):
    assert indigo.server.apiVersion == "3.4"


@pytest.mark.indigo_api_version("2.4")  # Every test in this class
class TestOldServer:
    def test_uses_class_version(self, indigo):
        assert indigo.server.apiVersion == "2.4"

    @pytest.mark.indigo_api_version("3.0")  # Only this test
    def test_uses_function_version(self, indigo):
        assert indigo.server.apiVersion == "3.0"
```

### Precedence
When a value is set in more than one place, the first match wins:

1. The closest mark: on the test function, then its class, then its module.
2. The fixture's value: from direct parametrization, or from a fixture override.
3. The ini option, for the API version (see [Configuration](#configuration)).

Marks always win, so a mark on one test can override a version or preferences set for a whole directory by a `conftest.py` fixture.

### `indigo_api_version` mark
`@pytest.mark.indigo_api_version(version)` sets the version reported by `indigo.server.apiVersion`, in place of the [`indigo_api_version`](#indigo_api_version) fixture. `version` is a string, such as `"3.4"`.

```python
@pytest.mark.indigo_api_version("2.4")
def test_get_plugin_list_requires_2_4(indigo):
    indigo.server.getPluginList()
```

### `indigo_plugin_prefs` mark
`@pytest.mark.indigo_plugin_prefs(prefs)` sets the preferences the [`plugin`](#plugin) fixture starts your plugin with, in place of the [`plugin_prefs`](#plugin_prefs) fixture. `prefs` is a `dict` or an `indigo.Dict`.

```python
@pytest.mark.indigo_plugin_prefs({"timeout": "30"})
def test_timeout(plugin):
    assert plugin.pluginPrefs["timeout"] == "30"
```

Each test gets its own copy of the preferences, so a test that changes `plugin.pluginPrefs` does not affect other tests sharing a class or module mark.

## Using a custom `indigo.activePlugin`
`indigo.activePlugin` always holds a plugin. Without the [`plugin`](#plugin) fixture, it holds a bare `indigo.PluginBase`.

Code that reads the active plugin, for example `indigo.activePlugin.pluginPrefs`, can be tested without creating your whole plugin. Assign your own plugin in the test:

```python
def test_reads_active_plugin_prefs(indigo):
    indigo.activePlugin = indigo.PluginBase(
        "com.example.myplugin",
        "My Plugin",
        "1.0.0",
        indigo.Dict({"timeout": "30"}),
    )

    assert my_module.get_timeout() == 30
```

The [`indigo`](#indigo) fixture puts the default plugin back after the test.

## Type hints
pytest-indigo is typed, so your editor and type checker can check your tests. With a one-time setup, your editor also knows that the [`plugin`](#plugin) fixture and `indigo.activePlugin` are your plugin's `Plugin` class, in every test, without annotating each one.

### One-time setup
First, add your `Server Plugin` folder to your type checker's search path, so `from plugin import Plugin` resolves. Type checkers don't run pytest, so they can't find it on their own:

```toml
# pyproject.toml
[tool.pyright]
extraPaths = ["MyPlugin.indigoPlugin/Contents/Server Plugin"]

[tool.mypy]
mypy_path = "MyPlugin.indigoPlugin/Contents/Server Plugin"
```

Then, in a `conftest.py`, override the [`plugin`](#plugin) and [`indigo`](#indigo) fixtures with your plugin's types. Each override requests pytest-indigo's fixture of the same name and returns it unchanged, so only the type annotations are added:

```python
# conftest.py
import pytest
from plugin import Plugin

from pytest_indigo import IndigoMock


@pytest.fixture()
def plugin(plugin) -> Plugin:
    return plugin


@pytest.fixture()
def indigo(indigo) -> IndigoMock[Plugin]:
    return indigo
```

`IndigoMock` takes the type of `indigo.activePlugin` as a type parameter, so `IndigoMock[Plugin]` types `indigo.activePlugin` as your `Plugin`. Without a type parameter, `indigo.activePlugin` is an `indigo.PluginBase`.

If your project loads pytest-indigo with `pytest_plugins`, put this `conftest.py` in your tests folder rather than the root, or see [Loading pytest-indigo without autoloading](#loading-pytest-indigo-without-autoloading).

Your tests don't need any annotations:

```python
def test_validate_prefs(plugin):
    plugin.my_plugin_method()  # plugin is a Plugin


def test_active_plugin(indigo, plugin):
    indigo.activePlugin.my_plugin_method()  # indigo.activePlugin is a Plugin
```

Editors with pytest support, such as VS Code with Pylance and PyCharm, take a test's fixture types from the fixtures' return annotations.

### Command-line type checkers
`pyright` and `mypy` don't know about pytest fixtures, so they treat unannotated fixture parameters as `Any`. Your tests still pass type checking, but their use of the fixtures isn't checked. To check a test from the command line, annotate its fixture parameters:

```python
from plugin import Plugin

from pytest_indigo import IndigoMock


def test_active_plugin(indigo: IndigoMock[Plugin], plugin: Plugin):
    indigo.activePlugin.my_plugin_method()
```

### The type parameter is only a hint
The type parameter is not checked when the test runs. `indigo.activePlugin` holds your `Plugin` only when the test requests the [`plugin`](#plugin) fixture or assigns your plugin itself. Otherwise it holds a bare `indigo.PluginBase`, whatever the annotation says.

### Inside your plugin's code
Your plugin's own code is checked against the `indigo` stubs provided by the Indigo team, where `indigo.activePlugin` is always an `indigo.PluginBase`. pytest-indigo can't change that. Where your plugin needs its own members from the active plugin, use `typing.cast`:

```python
from typing import TYPE_CHECKING, cast

import indigo

if TYPE_CHECKING:
    # Only imported for type checking, since plugin.py imports this module
    from plugin import Plugin

plugin = cast("Plugin", indigo.activePlugin)
```

## Configuration
pytest-indigo reads these ini options from your pytest configuration file:

| Option | Type | Default | Description |
|---|---|---|---|
| `indigo_plugin` | string | `""` (search the rootdir) | Path to the `.indigoPlugin` bundle to test, relative to the rootdir. Only needed when the rootdir contains more than one plugin. Used by the [`plugin_path`](#plugin_path) fixture. |
| `indigo_api_version` | string | `"3"` | Indigo Server plugin API version reported by `indigo.server.apiVersion`. Used by the [`indigo_api_version`](#indigo_api_version) fixture. |

In `pytest.toml`:

```toml
[pytest]
indigo_plugin = "MyPlugin.indigoPlugin"
```

In `pyproject.toml`:

```toml
[tool.pytest]
indigo_plugin = "MyPlugin.indigoPlugin"
```

In `pytest.ini`:

```ini
[pytest]
indigo_plugin = MyPlugin.indigoPlugin
```

## `PluginBase` differences from Indigo
- Like Indigo, the snake_case methods (for example `validate_prefs_config_ui`) are the implementations, and the camelCase names (`validatePrefsConfigUi`) are class-level aliases to them. Overriding the snake_case method in your plugin does **not** change what the camelCase name calls on the base class. Call `super()` with the same name you override.
- `plugin_support_url` is always an empty string.
- Nothing is written to a log file. `plugin_file_handler` discards all messages.
- Only the preferences UI callbacks, logging and `debug` are implemented so far. Calling `super().startup()`, `super().deviceStartComm()` and similar methods raises an `AttributeError`.
