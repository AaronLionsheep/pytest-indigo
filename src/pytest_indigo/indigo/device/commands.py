from typing import Any, Tuple  # noqa: UP035

from pytest_indigo.indigo.base import ElemKey
from pytest_indigo.indigo.collections import Dict, List
from pytest_indigo.indigo.enums import kFanMode, kHvacMode

from .models import Device


class DeviceCmds:
    """
    Command interface for device operations (``indigo.device``).
    Properties defined in CDeviceBase_pyglue.cpp.
    """

    supported_device_types: list[type]
    """List of Device subclasses this command namespace supports. Patched in by utils.py."""

    def supports_device(self, indigo_object: Device) -> bool:
        """Return True if *indigo_object* is a device type supported by this command namespace.
        Patched in by utils.py.
        """

    def create(
        self,
        address: str = "",
        deviceTypeId: str = "",
        hostId: str = "",
        name: str = "",
        description: str = "",
        pluginId: str = "",
        props: Dict | None = None,
        folder: ElemKey | None = None,
    ) -> Device:
        """Create a new device on the Indigo Server."""

    def duplicate(self, device: ElemKey, duplicateName: str = "") -> Device:
        """Duplicate an existing device."""

    def delete(self, device: ElemKey) -> None:
        """Delete a device from the Indigo Server."""

    def getDependencies(self, device: ElemKey | List | Tuple) -> Any:  # noqa: UP006
        """Return all element dependencies for the given device(s)."""

    def getGroupList(self, device: ElemKey) -> list[int]:
        """Return a list of device IDs in the same group as the given device."""
        return []

    def groupWithDevice(self, device: ElemKey, groupWithDevice: ElemKey) -> None:
        """Add a device to the same group as another device."""

    def ungroupDevice(self, device: ElemKey) -> None:
        """Remove a device from its group."""

    def moveToFolder(self, device: ElemKey, value: ElemKey) -> None:
        """Move a device to a different folder."""

    def displayInRemoteUI(self, device: ElemKey, value: bool) -> None:
        """Change a device's remote UI display visibility."""

    def enable(
        self, device: ElemKey, value: bool, delay: int = 0, duration: int = 0
    ) -> None:
        """Enable or disable a device with optional delay and duration (in seconds)."""

    def changeDeviceTypeId(self, device: ElemKey, deviceTypeId: str) -> None:
        """Change the device type ID of a device."""

    def x10ChangeAddress(self, device: ElemKey, address: str) -> None:
        """Change the X10 address of a device."""

    def x10ChangeModel(self, device: ElemKey, model: str) -> None:
        """Change the X10 model of a device."""

    def removeDelayedActions(self, device: ElemKey) -> None:
        """Remove all pending delayed actions for the given device."""

    def allOff(
        self, suppressLogging: bool = False, updateStatesOnly: bool = False
    ) -> None:
        """Send All Off command."""

    def beep(self, device: ElemKey, suppressLogging: bool = False) -> None:
        """Send a beep command to the device."""

    def statusRequest(
        self,
        device: ElemKey,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
    ) -> None:
        """Request a status update from the device."""

    def ping(self, device: ElemKey, suppressLogging: bool = False) -> None:
        """Send a ping to the device."""

    def turnOn(
        self,
        device: ElemKey,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
        delay: int = 0,
    ) -> None:
        """Turn the device on."""

    def turnOff(
        self,
        device: ElemKey,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
        delay: int = 0,
    ) -> None:
        """Turn the device off."""

    def toggle(
        self,
        device: ElemKey,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
        delay: int = 0,
    ) -> None:
        """Toggle the device on/off state."""

    def lock(
        self,
        device: ElemKey,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
    ) -> None:
        """Send a lock command to the device."""

    def unlock(
        self,
        device: ElemKey,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
    ) -> None:
        """Send an unlock command to the device."""

    def open(
        self,
        device: ElemKey,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
    ) -> None:
        """Send an open command to the device."""

    def close(
        self,
        device: ElemKey,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
    ) -> None:
        """Send a close command to the device."""

    def energyResetTotal(self, device: ElemKey, suppressLogging: bool = False) -> None:
        """Reset the device's accumulated energy total."""

    def energyUpdate(self, device: ElemKey, suppressLogging: bool = False) -> None:
        """Request an energy update from the device."""


class RelayDeviceCmds(DeviceCmds):
    """
    Command interface for relay device operations (``indigo.relay``).
    Inherits all DeviceCmds methods.
    Defined in CDeviceRelay_pyglue.cpp.
    """

    def allLightsOff(
        self, suppressLogging: bool = False, updateStatesOnly: bool = False
    ) -> None:
        """Send All Lights Off command."""

    def allLightsOn(
        self, suppressLogging: bool = False, updateStatesOnly: bool = False
    ) -> None:
        """Send All Lights On command."""

    def setLedState(
        self,
        device: ElemKey,
        index: int,
        value: bool,
        suppressLogging: bool = False,
    ) -> None:
        """Set the state of a specific LED on the device."""


class DimmerDeviceCmds(RelayDeviceCmds):
    """
    Command interface for dimmer device operations (``indigo.dimmer``).
    Inherits all RelayDeviceCmds methods.
    Defined in CDeviceDimmer_pyglue.cpp.
    """

    def brighten(
        self,
        device: ElemKey,
        brightenBy: int = 0,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
        delay: int = 0,
    ) -> None:
        """Brighten the device by a specified amount."""

    def dim(
        self,
        device: ElemKey,
        dimBy: int = 0,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
        delay: int = 0,
    ) -> None:
        """Dim the device by a specified amount."""

    def setBrightness(
        self,
        device: ElemKey,
        value: int,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
        delay: int = 0,
    ) -> None:
        """Set the device's brightness to a specific level (0-100)."""

    def setColorLevels(
        self,
        device: ElemKey,
        redLevel: int | None = None,
        greenLevel: int | None = None,
        blueLevel: int | None = None,
        whiteLevel: int | None = None,
        whiteLevel2: int | None = None,
        whiteTemperature: int | None = None,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
    ) -> None:
        """Set one or more color channel levels on the device."""


class SensorDeviceCmds(DeviceCmds):
    """
    Command interface for sensor device operations (``indigo.sensor``).
    Defined in CDeviceSensor_pyglue.cpp.
    """

    def setOnState(
        self,
        device: ElemKey,
        value: bool,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
    ) -> None:
        """Set the sensor's on/off state."""


class SpeedControlDeviceCmds(DeviceCmds):
    """
    Command interface for speed control device operations (``indigo.speedcontrol``).
    Defined in CDeviceSpeedControl_pyglue.cpp.
    """

    def increaseSpeedIndex(
        self,
        device: ElemKey,
        delta: int = 1,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
    ) -> None:
        """Increase the device's speed index by delta steps."""

    def decreaseSpeedIndex(
        self,
        device: ElemKey,
        delta: int = 1,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
    ) -> None:
        """Decrease the device's speed index by delta steps."""

    def setSpeedLevel(
        self,
        device: ElemKey,
        value: int,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
    ) -> None:
        """Set the device's speed to a specific percentage (0-100)."""

    def setSpeedIndex(
        self,
        device: ElemKey,
        value: int,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
    ) -> None:
        """Set the device's speed to a specific index step."""


class ThermostatDeviceCmds(DeviceCmds):
    """
    Command interface for thermostat device operations (``indigo.thermostat``).
    Defined in CDeviceThermostat_pyglue.cpp.
    """

    def setHvacMode(
        self,
        device: ElemKey,
        value: kHvacMode,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
    ) -> None:
        """Set the HVAC operating mode (one of indigo.kHvacMode.*)."""

    def setFanMode(
        self,
        device: ElemKey,
        value: kFanMode,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
    ) -> None:
        """Set the fan mode (one of indigo.kFanMode.*)."""

    def setCoolSetpoint(
        self,
        device: ElemKey,
        value: float,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
    ) -> None:
        """Set the cool setpoint temperature."""

    def setHeatSetpoint(
        self,
        device: ElemKey,
        value: float,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
    ) -> None:
        """Set the heat setpoint temperature."""

    def increaseCoolSetpoint(
        self,
        device: ElemKey,
        delta: float = 1.0,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
    ) -> None:
        """Increase the cool setpoint by delta degrees."""

    def decreaseCoolSetpoint(
        self,
        device: ElemKey,
        delta: float = 1.0,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
    ) -> None:
        """Decrease the cool setpoint by delta degrees."""

    def increaseHeatSetpoint(
        self,
        device: ElemKey,
        delta: float = 1.0,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
    ) -> None:
        """Increase the heat setpoint by delta degrees."""

    def decreaseHeatSetpoint(
        self,
        device: ElemKey,
        delta: float = 1.0,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
    ) -> None:
        """Decrease the heat setpoint by delta degrees."""


class SprinklerDeviceCmds(DeviceCmds):
    """
    Command interface for sprinkler device operations (``indigo.sprinkler``).
    Defined in CDeviceSprinkler_pyglue.cpp.
    """

    def nextZone(
        self,
        device: ElemKey,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
    ) -> None:
        """Advance to the next zone."""

    def previousZone(
        self,
        device: ElemKey,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
    ) -> None:
        """Advance to the previous zone."""

    def pause(
        self,
        device: ElemKey,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
    ) -> None:
        """Pause the current schedule."""

    def resume(
        self,
        device: ElemKey,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
    ) -> None:
        """Resume a paused schedule."""

    def run(
        self,
        device: ElemKey,
        schedule: list[float] | None = None,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
    ) -> None:
        """
        Run a sprinkler schedule. If schedule is None, reruns the previous schedule.
        Schedule is a list of zone durations in minutes.
        """

    def stop(
        self,
        device: ElemKey,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
    ) -> None:
        """Stop the current schedule."""

    def setActiveZone(
        self,
        device: ElemKey,
        index: int | None,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
    ) -> None:
        """
        Turn on a specific zone by 1-based index. Pass None or 0 to stop all zones.
        """

    def turnOnZone(
        self,
        device: ElemKey,
        index: int,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
    ) -> None:
        """
        Deprecated. Use setActiveZone() instead.
        Turn on a specific zone by 0-based index.
        """


class MultiIODeviceCmds(DeviceCmds):
    """
    Command interface for multi-I/O device operations (``indigo.iodevice``).
    Defined in CDeviceMultiIO_pyglue.cpp.
    """

    def setBinaryOutput(
        self,
        device: ElemKey,
        index: int,
        value: bool,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
    ) -> None:
        """
        Turn on or off a specific binary (relay) output by 0-based index.
        """
