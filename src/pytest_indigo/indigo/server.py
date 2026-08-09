from typing import Tuple, Any

import datetime
import logging

from .enums import kLicenseStatus
from .base import Dict


class ServerInfo:
    """
    Server properties and commands (``indigo.server``).
    Documented in server_commands.txt (wiki).
    """

    # ---- Properties (read-only) ----
    @property
    def address(self) -> str:
        """IP address of the currently connected Indigo Server."""
        ...

    @property
    def apiVersion(self) -> str:
        """Currently connected Indigo Server plugin API version string (e.g. "3.8")."""
        ...

    @property
    def connectionGood(self) -> bool:
        """True if the connection to the Indigo Server is currently good."""
        ...

    @property
    def licenseStatus(self) -> kLicenseStatus:
        """License status (one of indigo.kLicenseStatus.*)."""
        ...

    @property
    def portNum(self) -> int:
        """Port number of the currently connected Indigo Server."""
        ...

    @property
    def version(self) -> str:
        """Version string of the currently connected Indigo Server."""
        ...

    # ---- Commands ----
    def broadcastToSubscribers(
        self, messageName: str, props: Dict | dict | None = None
    ) -> None:
        """Broadcast a message to all plugins subscribed to messageName."""
        ...

    @staticmethod
    def _getWSS() -> Dict:
        """Internal: return the web server settings dict. Only callable from the Web Server plugin."""
        ...

    def calculateSunrise(self, date: datetime.date | None = None) -> datetime.datetime:
        """
        Return a datetime representing sunrise for the given date,
        or the next sunrise if no date is provided.
        """
        ...

    def calculateSunset(self, date: datetime.date | None = None) -> datetime.datetime:
        """
        Return a datetime representing sunset for the given date,
        or the next sunset if no date is provided.
        """
        ...

    def getEventLogList(
        self,
        returnAsList: bool = False,
        lineCount: int = 1500,
        showTimeStamp: bool = True,
    ) -> str | list[Dict]:
        """
        Return the latest event log entries.
        If returnAsList is True, returns a list of dicts; otherwise a newline-delimited string.
        """
        ...

    def getDbName(self) -> str:
        """Return the current database name (without file extension)."""
        ...

    def getDbFilePath(self) -> str:
        """Return the POSIX path to the current database file (including extension)."""
        ...

    def getDeprecatedElems(self, includeWarnings: bool = False) -> Any:
        """Return the server's list of deprecated elements."""
        ...

    def getInstallFolderPath(self) -> str:
        """Return the POSIX path to the current Indigo installation folder."""
        ...

    def getLogsFolderPath(self, pluginId: str | None = None) -> str:
        """Return the POSIX path to the server or plugin logs folder.
        Pass a pluginId to get that plugin's logs folder, or omit for the server logs folder.
        """
        ...

    def getLatitudeAndLongitude(self) -> Tuple[float, float]:
        """Return (latitude, longitude) as a tuple of floats."""
        ...

    def getPlugin(self, pluginId: str) -> PluginInfo:
        """Return a PluginInfo object for the given plugin ID."""
        ...

    def getPluginList(self) -> list[PluginInfo]:
        """Return a list of all enabled plugin instances."""
        ...

    def getReflectorURL(self) -> str | None:
        """
        Return the active reflector URL string, or None if no reflector
        is configured or remote access is disabled.
        """
        ...

    def getSerialPorts(self, filter: str = "") -> dict:
        """
        Return a dict of serial ports where key = POSIX path, value = display name.
        Pass filter="indigo.ignoreBluetooth" to exclude Bluetooth ports.
        """
        ...

    def getTime(self) -> datetime.datetime:
        """Return a datetime representing the server's current time."""
        ...

    def getWebServerURL(self) -> str:
        """
        Return the best URL string for the active Indigo Web Server.
        Order: reflector URL > Bonjour name > localhost. No trailing slash.
        """
        ...

    def log(
        self,
        message: str,
        type: str = "",
        level: int = logging.INFO,
        isError: bool = False,
    ) -> None:
        """
        Write a log entry to the Indigo event log.
        Use level=logging.WARNING for orange text, level=logging.ERROR or isError=True for red.
        """
        ...

    def removeAllDelayedActions(self) -> None:
        """Remove all currently scheduled delayed actions."""
        ...

    def restartPlugin(self, message: str, isError: bool = False) -> None:
        """
        Tell the server to restart this plugin process.
        Can only be called from within a plugin.
        """
        ...

    def savePluginPrefs(self) -> None:
        """Immediately save plugin preferences to disk."""
        ...

    def sendEmailTo(
        self,
        addresses: str,
        subject: str = "",
        body: str = "",
    ) -> None:
        """
        Send an email using the SMTP settings configured in Indigo preferences.
        addresses is a semicolon-separated string of email addresses.
        """
        ...

    def speak(self, text: str, waitUntilDone: bool = True) -> None:
        """Speak a text string using the built-in speech synthesizer."""
        ...

    def stopPlugin(self, message: str, isError: bool = False) -> None:
        """
        Tell the server to shut down this plugin process (leaves plugin enabled
        but stopped). Can only be called from within a plugin.
        """
        ...

    def subscribeToLogBroadcasts(self) -> None:
        """
        Subscribe to all server event log broadcasts. Plugin's logBroadcast()
        method will be called for each log entry.
        """
        ...

    def waitUntilIdle(self) -> None:
        """Block until the server has completed event processing and command sending."""
        ...
