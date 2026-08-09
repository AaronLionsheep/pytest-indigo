import datetime
from collections.abc import Iterator
from typing import Any, Self

from pytest_indigo.indigo.base.element import BaseElem
from pytest_indigo.indigo.collections import Dict
from pytest_indigo.indigo.enums import kFanMode, kHvacMode, kProtocol, kStateImageSel


class Device(BaseElem):
    """
    Base class for all Indigo device types.

    Exposed in Python as ``indigo.Device``.
    Properties defined in CDeviceBase_pyglue.cpp.
    """

    @classmethod
    def __create__(cls, id: int, name: str, server_ref: Self | None = None):
        instance = cls.__create__(id, name, server_ref)

        # Fake our __init__ and initialize the instance
        instance.__id = id
        instance.__name = name
        instance.__description = ""
        instance.__remote_display = True
        instance.__global_props = Dict()
        instance.__shared_props = Dict()
        instance.__server_ref = server_ref

        return instance

    # ---- Configuration / identity ----
    @property
    def configured(self) -> bool:
        """True if the device has been fully configured."""

    @configured.setter
    def configured(self, value: bool) -> None:
        """Owning plugin only: set the configured state directly on the local object,
        then call replaceOnServer() to persist."""

    @property
    def enabled(self) -> bool:
        """True if the device is enabled for Indigo processing."""

    @property
    def protocol(self) -> kProtocol:
        """Protocol used by this device (one of indigo.kProtocol.*)."""

    @property
    def model(self) -> str:
        """Model name string."""

    @property
    def subType(self) -> int:
        """Device sub-type integer."""

    @property
    def subModel(self) -> str:
        """Sub-model name string."""

    @property
    def version(self) -> str:
        """Device version string."""

    @property
    def address(self) -> str:
        """Protocol address string (e.g. INSTEON address "AA.BB.CC")."""

    @property
    def deviceTypeId(self) -> str:
        """Plugin-defined device type ID string."""

    @property
    def pluginId(self) -> str:
        """ID of the plugin that owns this device."""

    # ---- State / display ----
    @property
    def errorState(self) -> str:
        """
        Current error state string, or empty string if no error.
        Set via setErrorStateOnServer().
        """

    @property
    def displayStateId(self) -> str:
        """
        State key ID used for the primary display state. Read-only; set
        this locally (dev.displayStateId = "key") then call
        stateListOrDisplayStateIdChanged() to notify the server.
        """

    @property
    def displayStateValRaw(self) -> Any:
        """Raw value of the display state."""

    @property
    def displayStateValUi(self) -> str:
        """Human-readable UI string of the display state."""

    @property
    def displayStateImageSel(self) -> kStateImageSel:
        """Image selector for the display state (one of indigo.kStateImageSel.*)."""

    @property
    def states(self) -> dict:
        """
        Dict of all device states keyed by state name. Read/write locally;
        use updateStateOnServer() / updateStatesOnServer() to persist.
        """

    # ---- Hardware / timing ----
    @property
    def buttonGroupCount(self) -> int:
        """Number of button groups on this device."""

    @property
    def lastChanged(self) -> datetime.datetime:
        """Datetime of the last state change."""

    @property
    def lastSuccessfulComm(self) -> datetime.datetime:
        """Datetime of the last successful communication."""

    @property
    def batteryLevel(self) -> int | None:
        """Battery level (0-100), or None if not supported."""

    # ---- Energy monitoring ----
    @property
    def energyCurLevel(self) -> float | None:
        """Current energy consumption in watts, or None if not available."""

    @property
    def energyAccumTotal(self) -> float | None:
        """Accumulated energy total in watt-hours, or None if not available."""

    @property
    def energyAccumBaseTime(self) -> datetime.datetime | None:
        """Base time for energy accumulation, or None if not available."""

    @property
    def energyAccumTimeDelta(self) -> float | None:
        """Time delta for energy accumulation in seconds, or None."""

    # ---- Folder ----
    @property
    def folderId(self) -> int:
        """ID of the folder containing this device (0 = root)."""

    # ---- Capability flags ----
    @property
    def supportsOnState(self) -> bool:
        """True if the device supports an on/off state."""

    @property
    def supportsAllLightsOnOff(self) -> bool:
        """True if the device responds to All Lights On/Off commands."""

    @property
    def supportsAllOff(self) -> bool:
        """True if the device responds to All Off commands."""

    @property
    def supportsStatusRequest(self) -> bool:
        """True if the device supports status request commands."""

    # ---- Methods ----
    def refreshFromServer(self, waitUntilServerIdle: bool = False) -> None:
        """Refresh all device properties from the server."""

    def replaceOnServer(self) -> None:
        """Push local changes of the device to the server."""

    def replacePluginPropsOnServer(self, newProps: dict) -> None:
        """Replace the entire pluginProps dict on the server."""

    def replaceSharedPropsOnServer(self, newProps: dict) -> None:
        """Replace the shared props dict on the server."""

    def setErrorStateOnServer(self, errorState: str) -> None:
        """Set (or clear) the device error state on the server."""

    def stateListOrDisplayStateIdChanged(self) -> None:
        """
        Notify the server that the device's state list definition or
        displayStateId has changed. Called after modifying displayStateId locally.
        """

    def updateStateOnServer(
        self,
        key: str,
        value: Any,
        uiValue: str | None = None,
        clearErrorState: bool = True,
        decimalPlaces: int | None = None,
    ) -> None:
        """Update a single device state on the server."""

    def updateStatesOnServer(self, stateList: list[Dict]) -> None:
        """
        Update multiple device states on the server in a single call.
        Each dict in stateList should have keys: 'key', 'value', and optionally
        'uiValue', 'decimalPlaces'.
        """

    def updateStateImageOnServer(self, imageSelector: kStateImageSel) -> None:
        """Update the device's state image on the server (indigo.kStateImageSel.*)."""

    def updateTimeStampOnServer(self) -> None:
        """Update the lastSuccessfulComm timestamp on the server to now."""

    def __iter__(self) -> Iterator[tuple[str, Any]]:
        """Yields (key, value) pairs so dict(dev) works. Patched in by utils.py."""


class RelayDevice(Device):
    """
    A relay (on/off) device.

    Exposed in Python as ``indigo.RelayDevice``.
    Properties defined in CDeviceRelay_pyglue.cpp.
    """

    @property
    def onState(self) -> bool:
        """True if the relay is currently on. Read-only; use indigo.device.turnOn/Off/toggle() to change."""

    @property
    def buttonConfiguredCount(self) -> int:
        """Number of configured buttons on this device."""

    @property
    def ledStates(self) -> list[bool]:
        """List of boolean LED states."""


class DimmerDevice(RelayDevice):
    """
    A dimmer (variable brightness) device.

    Exposed in Python as ``indigo.DimmerDevice``.
    Properties defined in CDeviceDimmer_pyglue.cpp.
    """

    @property
    def brightness(self) -> int:
        """Current brightness level (0-100). Read-only; use indigo.dimmer.setBrightness() to change."""

    @property
    def defaultBrightness(self) -> int:
        """Default brightness level (0-100) when turned on. Read-only."""

    @property
    def onBrightensToDefaultToggle(self) -> bool:
        """True if turning on brightens to the default level. Read-only."""

    @property
    def onBrightensToLast(self) -> bool:
        """True if turning on brightens to the last brightness level. Read-only."""

    # ---- Color ----
    @property
    def supportsColor(self) -> bool:
        """True if the device supports color control."""

    @property
    def supportsRGB(self) -> bool:
        """True if the device supports RGB color."""

    @property
    def supportsWhite(self) -> bool:
        """True if the device supports a white channel."""

    @property
    def supportsTwoWhiteLevels(self) -> bool:
        """True if the device supports two independent white level channels."""

    @property
    def supportsWhiteTemperature(self) -> bool:
        """True if the device supports white color temperature."""

    @property
    def supportsRGBandWhiteSimultaneously(self) -> bool:
        """True if RGB and white channels can be active simultaneously."""

    @property
    def redLevel(self) -> int:
        """Red color channel level (0-100). Read-only; use indigo.dimmer.setColorLevels() to change."""

    @property
    def greenLevel(self) -> int:
        """Green color channel level (0-100). Read-only; use indigo.dimmer.setColorLevels() to change."""

    @property
    def blueLevel(self) -> int:
        """Blue color channel level (0-100). Read-only; use indigo.dimmer.setColorLevels() to change."""

    @property
    def whiteLevel(self) -> int:
        """White channel level (0-100). Read-only; use indigo.dimmer.setColorLevels() to change."""

    @property
    def whiteLevel2(self) -> int:
        """Second white channel level (0-100). Read-only; use indigo.dimmer.setColorLevels() to change."""

    @property
    def whiteTemperature(self) -> int:
        """White color temperature in Kelvin. Read-only; use indigo.dimmer.setColorLevels() to change."""


class SensorDevice(Device):
    """
    A sensor (read-only state) device.

    Exposed in Python as ``indigo.SensorDevice``.
    Properties defined in CDeviceSensor_pyglue.cpp.
    """

    @property
    def onState(self) -> bool | None:
        """Boolean on/off state of the sensor, or None if not applicable."""

    @property
    def allowOnStateChange(self) -> bool:
        """True if plugins are allowed to change the onState via updateStateOnServer."""

    @property
    def sensorValue(self) -> float | None:
        """Numeric sensor value, or None if not applicable."""

    @property
    def allowSensorValueChange(self) -> bool:
        """True if plugins are allowed to change the sensorValue via updateStateOnServer."""

    @property
    def supportsSensorValue(self) -> bool:
        """True if this sensor supports a numeric sensorValue."""


class SpeedControlDevice(Device):
    """
    A multi-speed fan/motor control device.

    Exposed in Python as ``indigo.SpeedControlDevice``.
    Properties defined in CDeviceSpeedControl_pyglue.cpp.
    """

    @property
    def onState(self) -> bool:
        """True if the speed control device is on (speedIndex > 0). Read-only; use indigo.speedcontrol.turnOn/Off() to change."""

    @property
    def speedLevel(self) -> int:
        """Current speed as a percentage (0-100). Read-only; use indigo.speedcontrol.setSpeedLevel() to change."""

    @property
    def speedIndex(self) -> int:
        """Current speed as an index (0 = off, 1-N = speed steps). Read-only; use indigo.speedcontrol.setSpeedIndex() to change."""

    @property
    def speedIndexCount(self) -> int:
        """Total number of speed steps (excluding off)."""


class ThermostatDevice(Device):
    """
    A thermostat device.

    Exposed in Python as ``indigo.ThermostatDevice``.
    Properties defined in CDeviceThermostat_pyglue.cpp.
    """

    @property
    def hvacMode(self) -> kHvacMode:
        """Current HVAC operating mode (one of indigo.kHvacMode.*). Read-only; use indigo.thermostat.setHvacMode() to change."""

    @property
    def fanMode(self) -> kFanMode:
        """Current fan mode (one of indigo.kFanMode.*). Read-only; use indigo.thermostat.setFanMode() to change."""

    @property
    def coolSetpoint(self) -> float:
        """Cool setpoint temperature. Read-only; use indigo.thermostat.setCoolSetpoint() to change."""

    @property
    def heatSetpoint(self) -> float:
        """Heat setpoint temperature. Read-only; use indigo.thermostat.setHeatSetpoint() to change."""

    @property
    def temperatures(self) -> list[float]:
        """List of current temperatures (one per sensor zone)."""

    @property
    def humidities(self) -> list[float]:
        """List of current humidity values (one per sensor)."""

    @property
    def coolSetpoints(self) -> list[float]:
        """List of cool setpoints (for multi-zone thermostats)."""

    @property
    def heatSetpoints(self) -> list[float]:
        """List of heat setpoints (for multi-zone thermostats)."""

    @property
    def hvacOperationModeIsOff(self) -> bool:
        """True if HVAC mode is Off."""

    @property
    def hvacOperationModeIsHeat(self) -> bool:
        """True if HVAC mode is Heat."""

    @property
    def hvacOperationModeIsCool(self) -> bool:
        """True if HVAC mode is Cool."""

    @property
    def hvacOperationModeIsHeatCool(self) -> bool:
        """True if HVAC mode is Heat/Cool."""

    @property
    def hvacOperationModeIsProgramHeat(self) -> bool:
        """True if HVAC mode is Program Heat."""

    @property
    def hvacOperationModeIsProgramCool(self) -> bool:
        """True if HVAC mode is Program Cool."""

    @property
    def hvacOperationModeIsProgramHeatCool(self) -> bool:
        """True if HVAC mode is Program Heat/Cool."""

    @property
    def hvacFanModeIsAuto(self) -> bool:
        """True if fan mode is Auto."""

    @property
    def hvacFanModeIsAlwaysOn(self) -> bool:
        """True if fan mode is Always On."""

    @property
    def fanIsOn(self) -> bool:
        """True if the fan is currently running (shortcut for dev.states['hvacFanIsOn'])."""

    @property
    def coolIsOn(self) -> bool:
        """True if the cooling system (compressor) is currently running (shortcut for dev.states['hvacCoolerIsOn'])."""

    @property
    def heatIsOn(self) -> bool:
        """True if the heater is currently running (shortcut for dev.states['hvacHeaterIsOn'])."""

    @property
    def temperatureInputsAll(self) -> list[float]:
        """All temperature input values."""

    @property
    def humidityInputsAll(self) -> list[float]:
        """All humidity input values."""

    @property
    def numTemperatureInputs(self) -> int:
        """Number of temperature inputs."""

    @property
    def numHumidityInputs(self) -> int:
        """Number of humidity inputs."""

    @property
    def supportsHvacOperationMode(self) -> bool: ...

    @property
    def supportsHvacFanMode(self) -> bool: ...

    @property
    def supportsCoolSetpoint(self) -> bool: ...

    @property
    def supportsHeatSetpoint(self) -> bool: ...

    @property
    def supportsTemperatureReporting(self) -> bool: ...

    @property
    def supportsHumidityReporting(self) -> bool: ...


class SprinklerDevice(Device):
    """
    A sprinkler/irrigation controller device.

    Exposed in Python as ``indigo.SprinklerDevice``.
    Properties defined in CDeviceSprinkler_pyglue.cpp.
    """

    @property
    def activeZone(self) -> int | None:
        """1-based index of the currently active zone, or None if all zones are off."""

    @property
    def zoneCount(self) -> int:
        """Number of zones on this device."""

    @property
    def zoneEnableList(self) -> list[bool]:
        """List of booleans indicating which zones are enabled."""

    @property
    def zoneNames(self) -> list[str]:
        """List of zone name strings."""

    @property
    def zoneMaxDurations(self) -> list[float | None]:
        """List of maximum zone durations in minutes (None if unlimited)."""

    @property
    def zoneScheduledDurations(self) -> list[float]:
        """List of scheduled zone durations in minutes."""

    @property
    def pausedScheduleZone(self) -> int | None:
        """1-based index of the paused zone, or None if not paused."""

    @property
    def pausedScheduleRemainingZoneDuration(self) -> float | None:
        """Remaining duration in minutes for the paused zone, or None."""


class MultiIODevice(Device):
    """
    A multi-I/O device (digital/analog inputs and outputs).

    Exposed in Python as ``indigo.MultiIODevice``.
    Properties defined in CDeviceMultiIO_pyglue.cpp.
    """

    @property
    def analogInputCount(self) -> int:
        """Number of analog inputs."""

    @property
    def binaryInputCount(self) -> int:
        """Number of binary (digital) inputs."""

    @property
    def sensorInputCount(self) -> int:
        """Number of sensor inputs."""

    @property
    def binaryOutputCount(self) -> int:
        """Number of binary (relay) outputs."""

    @property
    def analogInputs(self) -> list[int]:
        """List of current analog input values."""

    @property
    def binaryInputs(self) -> list[bool]:
        """List of current binary input states."""

    @property
    def sensorInputs(self) -> list[int]:
        """List of current sensor input values."""

    @property
    def binaryOutputs(self) -> list[bool]:
        """List of current binary output states."""
