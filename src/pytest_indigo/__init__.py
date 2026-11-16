import importlib
import os
import plistlib
import sys
from collections.abc import Generator
from functools import lru_cache
from typing import Any

from pytest import fixture, hookimpl

from pytest_indigo.exceptions import PytestIndigoException
from pytest_indigo.indigo import Dict, PluginBase

from .mock import DEFAULT_API_VERSION, IndigoMock

indigo_mock = IndigoMock()
sys.modules["indigo"] = indigo_mock


@lru_cache
def find_plugin(base_dir):
    plugins = []
    for dirpath, dirnames, _ in os.walk(base_dir):
        for dirname in dirnames:
            if dirname.endswith(".indigoPlugin"):
                plugins.append(os.path.join(dirpath, dirname))

    if len(plugins) == 0:
        raise PytestIndigoException(f"No Indigo plugins were found in {base_dir}!")
    elif len(plugins) > 1:
        raise PytestIndigoException(
            "More than one Indigo plugin was found! "
            "You must manually configure pytest_indigo with the plugin to test. "
            f"{plugins}"
        )

    return plugins[0]


def load_plugin_info(plugin_path: str) -> dict:
    """Load the Info.plist from an Indigo plugin bundle."""
    with open(os.path.join(plugin_path, "Contents", "Info.plist"), "rb") as f:
        return plistlib.load(f)


def resolve_plugin_path(config) -> str:
    """
    Find the .indigoPlugin bundle to test.

    Uses the indigo_plugin ini option when set, otherwise the only plugin found in
    the rootdir.

    :raises PytestIndigoException: If the rootdir has no plugin, or more than one.
    """
    if path := config.getini("indigo_plugin"):
        return os.path.join(config.rootpath, path)

    return find_plugin(config.rootpath)


def add_server_plugin_path(plugin_path: str) -> None:
    """
    Add the "Server Plugin" folder of an Indigo plugin bundle to the path.

    Like IndigoPluginHost3, this makes plugin.py and the plugin's other modules
    importable as top-level modules.
    """
    server_plugin_path = os.path.join(plugin_path, "Contents", "Server Plugin")
    if server_plugin_path not in sys.path:
        sys.path.insert(0, server_plugin_path)


def load_plugin_class(plugin_path: str) -> type[PluginBase]:
    """Import the Plugin class from an Indigo plugin bundle."""
    add_server_plugin_path(plugin_path)
    return importlib.import_module("plugin").Plugin


def pytest_addoption(parser):
    group = parser.getgroup("Indigo", "Configuration for my internal test suite")

    parser.addini(
        "indigo_plugin",
        help="Path to the .indigoPlugin bundle to test, relative to the rootdir. "
        "Only needed when the rootdir contains more than one plugin.",
        default="",
    )
    parser.addini(
        "indigo_api_version",
        help="Indigo Server plugin API version reported by indigo.server.apiVersion.",
        default=DEFAULT_API_VERSION,
    )

    # 2. Register the INI option fallback
    parser.addini(
        "myplugin_retries",
        help="Default retry count handled by configuration file",
        type="int",
        default=3,
    )

    # 3. Add a CLI argument to the group that overrides or complements the INI option
    group.addoption(
        "--retries",
        action="store",
        dest="cli_retries",
        help="Override the myplugin_retries INI setting via command line",
    )


def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "indigo_api_version(version): Indigo Server plugin API version reported by "
        "indigo.server.apiVersion. Takes precedence over the indigo_api_version fixture.",
    )
    config.addinivalue_line(
        "markers",
        "indigo_plugin_prefs(prefs): Plugin preferences the plugin fixture starts the "
        "plugin with. Takes precedence over the plugin_prefs fixture.",
    )

    # pytest_load_initial_conftests is missed when pytest-indigo is loaded by a conftest
    add_plugin_to_path(config)


@hookimpl(tryfirst=True)
def pytest_load_initial_conftests(early_config):
    # Before conftests are loaded, so they can import the plugin's modules
    add_plugin_to_path(early_config)


def add_plugin_to_path(config) -> None:
    """Make the plugin's modules importable by tests, like IndigoPluginHost3 does."""
    try:
        add_server_plugin_path(resolve_plugin_path(config))
    except PytestIndigoException:
        # Only an error for tests that use the plugin fixture, which reports it
        pass


def get_mark_value(request, name: str, value_type: type) -> Any:
    """
    Get the argument of the closest mark applied to the test.

    :param request: The pytest request of the fixture reading the mark.
    :param name: The name of the mark.
    :param value_type: The type the mark's single argument must be.
    :return: The mark's argument, or None if the mark is not applied.
    :raises PytestIndigoException: If the mark does not have exactly one argument of
        value_type.
    """
    marker = request.node.get_closest_marker(name)
    if marker is None:
        return None

    if (
        len(marker.args) != 1
        or marker.kwargs
        or not isinstance(marker.args[0], value_type)
    ):
        raise PytestIndigoException(
            f"The {name} mark takes a single {value_type.__name__} argument, "
            f"but got args={marker.args} kwargs={marker.kwargs}"
        )

    return marker.args[0]


@fixture(name="indigo_api_version")
def fixture_indigo_api_version(request) -> str:
    """
    Indigo Server plugin API version reported by indigo.server.apiVersion.

    Uses the indigo_api_version ini option. Override or parametrize this fixture to
    test against a different Indigo Server version. An indigo_api_version mark takes
    precedence over this fixture.
    """
    return request.config.getini("indigo_api_version")


@fixture(name="indigo")
def fixture_indigo(
    request, indigo_api_version: str
) -> Generator[IndigoMock, None, None]:
    if (version := get_mark_value(request, "indigo_api_version", str)) is not None:
        indigo_api_version = version

    indigo_mock.reset(api_version=indigo_api_version)
    yield indigo_mock
    indigo_mock.reset()


@fixture(name="plugin_path")
def fixture_plugin_path(request) -> str:
    """
    Path to the .indigoPlugin bundle under test.

    Uses the indigo_plugin ini option when set, otherwise the only plugin found in
    the rootdir. Override this fixture to test a different plugin.
    """
    return resolve_plugin_path(request.config)


@fixture(name="plugin_prefs")
def fixture_plugin_prefs() -> Dict:
    """
    Plugin preferences passed to the plugin under test.

    Override this fixture to start the plugin with custom preferences. A plain dict
    is converted to an indigo.Dict. An indigo_plugin_prefs mark takes precedence over
    this fixture.
    """
    return Dict()


@fixture(name="plugin")
def fixture_plugin(
    request, indigo: IndigoMock, plugin_path: str, plugin_prefs: Dict | dict
) -> PluginBase:
    """
    A new instance of the plugin under test, set as indigo.activePlugin.

    Like IndigoPluginHost3, the plugin is created from its Info.plist values, but
    startup() is not called so tests control when the plugin starts.
    """
    # Indigo always provides the plugin preferences as an indigo.Dict
    if (prefs := get_mark_value(request, "indigo_plugin_prefs", dict)) is not None:
        # Copy the preferences, since a class or module mark is shared by many tests
        plugin_prefs = Dict(prefs)
    elif not isinstance(plugin_prefs, Dict):
        plugin_prefs = Dict(plugin_prefs)

    info = load_plugin_info(plugin_path)
    plugin = load_plugin_class(plugin_path)(
        info["CFBundleIdentifier"],
        info["CFBundleDisplayName"],
        info["PluginVersion"],
        plugin_prefs,
    )
    plugin.plugin_folder_path = plugin.pluginFolderPath = plugin_path

    indigo.activePlugin = plugin
    return plugin
