from pytest_indigo.indigo.collections import Dict


class PluginInfo:
    """
    Metadata about an installed Indigo plugin.
    Returned by indigo.server.getPlugin() and indigo.server.getPluginList().
    Defined in CPlugin_pyglue.cpp.
    """

    @property
    def pluginId(self) -> str:
        """Unique plugin ID string."""

    @property
    def pluginDisplayName(self) -> str:
        """Human-readable plugin name."""

    @property
    def pluginFolderPath(self) -> str:
        """POSIX path to the plugin bundle."""

    @property
    def pluginVersion(self) -> str:
        """Plugin version string."""

    @property
    def pluginBundleId(self) -> str:
        """Bundle ID string of the plugin."""

    @property
    def serverApiVersion(self) -> str:
        """Minimum required server API version string."""

    @property
    def apiVersion(self) -> str:
        """Plugin API version string."""

    @property
    def priority(self) -> int:
        """Plugin load priority."""

    @property
    def debuggingEnabled(self) -> bool:
        """True if debugging is enabled for the plugin."""

    @property
    def isLoaded(self) -> bool:
        """True if the plugin process is loaded."""

    @property
    def storeDescription(self) -> str:
        """Plugin Store description."""

    @property
    def storeReleaseNotesURL(self) -> str:
        """URL to plugin release notes."""

    @property
    def storeDownloadURL(self) -> str:
        """URL to download the plugin."""

    @property
    def storeChangelogURL(self) -> str:
        """URL to the plugin changelog."""

    @property
    def updateAvailable(self) -> bool:
        """True if a plugin update is available in the Plugin Store."""

    @property
    def latestVersion(self) -> str:
        """Latest version string available in the Plugin Store."""

    def isInstalled(self) -> bool:
        """Return True if the plugin is installed."""

    def isEnabled(self) -> bool:
        """Return True if the plugin is enabled."""

    def isRunning(self) -> bool:
        """Return True if the plugin process is currently running."""

    def restart(self, waitUntilDone: bool = True) -> None:
        """Restart the plugin process."""

    def restartAndDebug(self, waitUntilDone: bool = True) -> None:
        """Restart the plugin process in debug mode."""

    def executeAction(
        self,
        actionTypeId: str,
        deviceId: int = 0,
        props: Dict | dict | None = None,
        waitUntilDone: bool = True,
    ) -> Dict | str | None:
        """
        Execute a plugin-defined action by type ID.
        Returns a dict or str of results, or None if waitUntilDone is False.
        """
