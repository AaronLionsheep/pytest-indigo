import plistlib

import pytest

PLUGIN = """
import indigo


class Plugin(indigo.PluginBase):
    pass
"""


def make_plugin(pytester: pytest.Pytester, name: str, version: str = "1.0.0"):
    """Create a minimal Indigo plugin bundle in the pytester directory."""
    contents = pytester.path / f"{name}.indigoPlugin" / "Contents"
    server_plugin = contents / "Server Plugin"
    server_plugin.mkdir(parents=True)
    (server_plugin / "plugin.py").write_text(PLUGIN)
    (contents / "Info.plist").write_bytes(
        plistlib.dumps(
            {
                "PluginVersion": version,
                "ServerApiVersion": "3.0",
                "CFBundleDisplayName": name,
                "CFBundleIdentifier": f"com.example.{name.lower()}",
            }
        )
    )


@pytest.fixture()
def pytester(pytester: pytest.Pytester) -> pytest.Pytester:
    pytester.makeconftest('pytest_plugins = ["pytest_indigo"]')
    return pytester


def test_plugin_fixture(pytester: pytest.Pytester):
    make_plugin(pytester, "First", version="1.2.3")
    pytester.makepyfile(
        """
        def test_plugin(indigo, plugin, plugin_path):
            assert indigo.activePlugin is plugin
            assert plugin.plugin_id == "com.example.first"
            assert plugin.plugin_display_name == "First"
            assert plugin.plugin_version == "1.2.3"
            assert plugin.plugin_folder_path == plugin.pluginFolderPath == plugin_path
            assert plugin_path.endswith("First.indigoPlugin")

        def test_plugin_prefs(indigo, plugin):
            assert isinstance(plugin.plugin_prefs, indigo.Dict)
            assert plugin.plugin_prefs == {}

        def test_new_instance_per_test(indigo, plugin):
            assert type(plugin).__module__ == "plugin"
            assert isinstance(plugin, indigo.PluginBase)
        """
    )

    pytester.runpytest().assert_outcomes(passed=3)


def test_plugin_ini_option(pytester: pytest.Pytester):
    make_plugin(pytester, "First")
    make_plugin(pytester, "Second")
    pytester.makeini(
        """
        [pytest]
        indigo_plugin = Second.indigoPlugin
        """
    )
    pytester.makepyfile(
        """
        def test_plugin(plugin):
            assert plugin.plugin_id == "com.example.second"
        """
    )

    pytester.runpytest().assert_outcomes(passed=1)


def test_plugin_prefs_override(pytester: pytest.Pytester):
    make_plugin(pytester, "First")
    pytester.makepyfile(
        """
        import pytest

        @pytest.fixture()
        def plugin_prefs():
            return {"key": "value"}

        def test_plugin_prefs(indigo, plugin):
            assert isinstance(plugin.plugin_prefs, indigo.Dict)
            assert plugin.plugin_prefs == {"key": "value"}
        """
    )

    pytester.runpytest().assert_outcomes(passed=1)


def test_custom_active_plugin(pytester: pytest.Pytester):
    make_plugin(pytester, "First")
    pytester.makepyfile(
        """
        def test_custom_active_plugin(indigo):
            custom = indigo.PluginBase("com.example.custom", "Custom", "1.0.0", indigo.Dict())
            indigo.activePlugin = custom

            assert indigo.activePlugin is custom
        """
    )

    pytester.runpytest().assert_outcomes(passed=1)
