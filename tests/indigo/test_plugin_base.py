import logging

import pytest

from pytest_indigo import IndigoMock
from pytest_indigo.indigo import Dict, IndigoLogger, PluginBase


@pytest.fixture()
def plugin(indigo: IndigoMock) -> PluginBase:
    return PluginBase("com.example.pytest", "Pytest", "1.0.0", Dict({"key": "value"}))


# MARK: __init__()
class TestInit:
    def test_attributes(self, plugin: PluginBase):
        assert plugin.plugin_id == plugin.pluginId == "com.example.pytest"
        assert plugin.plugin_display_name == plugin.pluginDisplayName == "Pytest"
        assert plugin.plugin_version == plugin.pluginVersion == "1.0.0"
        assert plugin.plugin_prefs == {"key": "value"}
        assert plugin.pluginPrefs is plugin.plugin_prefs

    def test_stop_thread(self, plugin: PluginBase):
        assert plugin.stop_thread is False
        assert plugin.stopThread is False


# MARK: Logging
class TestLogging:
    def test_logger_is_indigo_logger(self, plugin: PluginBase):
        assert isinstance(plugin.logger, IndigoLogger)

    def test_indigo_log_handler_level(self, plugin: PluginBase):
        assert plugin.indigo_log_handler.level == logging.INFO

    def test_plugin_file_handler_level(self, plugin: PluginBase):
        assert plugin.plugin_file_handler.level == logging.THREADDEBUG  # type: ignore[attr-defined]

    def test_replaces_previous_handlers(self, indigo: IndigoMock, plugin: PluginBase):
        other = PluginBase("com.example.other", "Other", "1.0.0", Dict())

        assert other.logger.handlers == [
            other.indigo_log_handler,
            other.plugin_file_handler,
        ]

    def test_logs_to_indigo_server(
        self, indigo: IndigoMock, plugin: PluginBase, monkeypatch
    ):
        entries = []
        monkeypatch.setattr(
            indigo.server, "log", lambda **kwargs: entries.append(kwargs)
        )

        plugin.logger.info("Hello")

        assert entries == [
            {"message": "Hello", "type": "Pytest", "level": logging.INFO}
        ]

    def test_threaddebug(self, plugin: PluginBase, caplog):
        with caplog.at_level(logging.THREADDEBUG, logger="Plugin"):  # type: ignore[attr-defined]
            plugin.logger.threaddebug("Hello")

        assert [(r.levelname, r.message) for r in caplog.records] == [
            ("THREADDEBUG", "Hello")
        ]

    def test_threaddebug_disabled(self, plugin: PluginBase, caplog):
        plugin.logger.setLevel(logging.DEBUG)

        with caplog.at_level(logging.THREADDEBUG):  # type: ignore[attr-defined]
            plugin.logger.threaddebug("Hello")

        assert caplog.records == []


# MARK: debug
class TestDebug:
    def test_default(self, plugin: PluginBase):
        assert plugin.debug is False

    def test_enable(self, plugin: PluginBase):
        plugin.debug = True

        assert plugin.debug is True
        assert plugin.indigo_log_handler.level == logging.DEBUG

    def test_disable(self, plugin: PluginBase):
        plugin.debug = True
        plugin.debug = False

        assert plugin.debug is False
        assert plugin.indigo_log_handler.level == logging.INFO


# MARK: Plugin preferences UI
class TestPrefsConfigUi:
    def test_get_prefs_config_ui_values(self, plugin: PluginBase):
        values_dict, errors = plugin.get_prefs_config_ui_values()

        assert values_dict is plugin.plugin_prefs
        assert isinstance(errors, Dict)
        assert errors == {}

    def test_validate_prefs_config_ui(self, plugin: PluginBase):
        values_dict = Dict({"key": "value"})

        assert plugin.validate_prefs_config_ui(values_dict) == (True, values_dict)

    def test_closed_prefs_config_ui(self, plugin: PluginBase):
        assert plugin.closed_prefs_config_ui(Dict(), userCancelled=False) is None

    @pytest.mark.parametrize(
        ("camel_case", "snake_case"),
        [
            ("getPrefsConfigUiValues", "get_prefs_config_ui_values"),
            ("validatePrefsConfigUi", "validate_prefs_config_ui"),
            ("closedPrefsConfigUi", "closed_prefs_config_ui"),
        ],
    )
    def test_camel_case_aliases(self, camel_case, snake_case):
        assert getattr(PluginBase, camel_case) is getattr(PluginBase, snake_case)

    def test_aliases_bound_to_base_implementation(self, indigo: IndigoMock):
        """Like Indigo, overriding the snake_case method does not change the camelCase alias"""

        class Plugin(indigo.PluginBase):
            def get_prefs_config_ui_values(self):
                return Dict({"overridden": True}), Dict()

        plugin = Plugin("com.example.pytest", "Pytest", "1.0.0", Dict())

        assert plugin.get_prefs_config_ui_values()[0] == {"overridden": True}
        assert plugin.getPrefsConfigUiValues()[0] == {}


# MARK: activePlugin
class TestActivePlugin:
    def test_default(self, indigo: IndigoMock):
        assert isinstance(indigo.activePlugin, PluginBase)

    def test_reset_restores_default(self, indigo: IndigoMock, plugin: PluginBase):
        indigo.activePlugin = plugin
        indigo.reset()

        assert isinstance(indigo.activePlugin, PluginBase)
        assert indigo.activePlugin is not plugin
