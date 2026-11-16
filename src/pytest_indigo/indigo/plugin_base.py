import logging
from typing import Any, Tuple  # noqa: UP035

from pytest_indigo.indigo.collections import Dict

# Indigo adds a THREADDEBUG level below DEBUG for more detailed debugging
logging.addLevelName(5, "THREADDEBUG")
logging.THREADDEBUG = 5  # type: ignore[attr-defined]


class IndigoLogger(logging.Logger):
    """
    Logger subclass registered via logging.setLoggerClass() in plugin_base.py.
    Adds the ``threaddebug`` method (level 5, below DEBUG) used by plugins.
    ``self.logger`` on PluginBase instances is always an IndigoLogger.
    """

    def threaddebug(self, msg: object, *args: object, **kwargs: Any) -> None:
        """Log at level THREADDEBUG (5), below DEBUG. No-op if level is not enabled."""
        if self.isEnabledFor(logging.THREADDEBUG):  # type: ignore[attr-defined]
            self._log(logging.THREADDEBUG, msg, args, **kwargs)  # type: ignore[attr-defined]


# Indigo creates all loggers as IndigoLoggers
logging.setLoggerClass(IndigoLogger)


class IndigoLogHandler(logging.Handler):
    """Logging handler that emits log messages into the Indigo Event Log."""

    def __init__(self, display_name: str, level: int = logging.NOTSET):
        super().__init__(level)
        self.display_name = display_name

    def emit(self, record: logging.LogRecord) -> None:
        from pytest_indigo import indigo_mock as indigo

        indigo.server.log(
            message=self.format(record), type=self.display_name, level=record.levelno
        )


class PluginBase:
    """
    Base class for all Indigo plugins. Plugin developers subclass this in plugin.py.
    Defined in Py3 Libraries/plugin_base.py and injected into the indigo namespace.

    Like Indigo, the snake_case methods are the implementations and the camelCase
    names are class-level aliases bound to them.
    """

    # ---- Nested exception classes ----
    class InterfaceError(Exception):
        """Raised when a hardware interface operation fails."""

    class PluginDisabled(Exception):
        """Raised when an operation requires a plugin that is installed but disabled."""

    class PluginNotInstalled(Exception):
        """Raised when an operation requires a plugin that is not installed."""

    class InvalidAction(Exception):
        """Raised when an action type ID is not valid for the target plugin."""

    class InvalidParameter(Exception):
        """Raised when a parameter passed to a plugin method is invalid."""

    class StopThread(Exception):
        """Raised internally to signal the plugin's concurrent thread to stop."""

    def __init__(
        self,
        pluginId: str,
        pluginDisplayName: str,
        pluginVersion: str,
        pluginPrefs: dict,
        **kwargs: Any,
    ) -> None:
        """Initialize the plugin. Call super().__init__() in your subclass."""
        self.plugin_id = self.pluginId = pluginId
        self.plugin_display_name = self.pluginDisplayName = pluginDisplayName
        self.plugin_version = self.pluginVersion = pluginVersion
        self.plugin_prefs = self.pluginPrefs = pluginPrefs

        # Indigo provides these from the plugin bundle, which is not loaded by pytest-indigo
        self.plugin_folder_path = self.pluginFolderPath = ""
        self.plugin_support_url = self.pluginSupportURL = ""

        self._debug = False
        self.logger: IndigoLogger = logging.getLogger("Plugin")  # type: ignore[assignment]
        self.logger.setLevel(logging.THREADDEBUG)  # type: ignore[attr-defined]

        # Replace the handlers added by any previous plugin instance (ex: an earlier test)
        for handler in list(self.logger.handlers):
            self.logger.removeHandler(handler)

        self.indigo_log_handler: logging.Handler = IndigoLogHandler(
            pluginDisplayName, logging.INFO
        )
        self.indigo_log_handler.setFormatter(logging.Formatter("%(message)s"))
        self.logger.addHandler(self.indigo_log_handler)

        # Indigo writes all levels to the plugin's log file, which pytest-indigo does not create
        self.plugin_file_handler: logging.Handler = logging.NullHandler(
            logging.THREADDEBUG  # type: ignore[attr-defined]
        )
        self.logger.addHandler(self.plugin_file_handler)

        self.stop_thread = self.stopThread = False

    @property
    def debug(self) -> bool:
        """True when debug logging is enabled for this plugin."""
        return self._debug

    @debug.setter
    def debug(self, value: bool) -> None:
        self._debug = value

        # Only the Indigo log handler changes, the plugin log file always shows debug logging
        if value:
            self.indigo_log_handler.setLevel(logging.DEBUG)
        else:
            self.indigo_log_handler.setLevel(logging.INFO)

    # ---- Plugin preferences UI ----
    def get_prefs_config_ui_values(self) -> Tuple[Dict, Dict]:  # noqa: UP006
        """Return (valuesDict, errorsDict) for the plugin preferences UI."""
        values_dict = self.plugin_prefs
        error_msg_dict = Dict()
        return (values_dict, error_msg_dict)  # type: ignore[return-value]

    getPrefsConfigUiValues = get_prefs_config_ui_values

    def validate_prefs_config_ui(self, valuesDict: dict) -> Tuple[bool, Dict, Dict]:  # noqa: UP006
        """Validate plugin preferences UI values."""
        return (True, valuesDict)  # type: ignore[return-value]

    validatePrefsConfigUi = validate_prefs_config_ui

    def closed_prefs_config_ui(self, valuesDict: dict, userCancelled: bool) -> None:
        """Called after the plugin preferences dialog is closed."""

    closedPrefsConfigUi = closed_prefs_config_ui
