"""
indigo.pyi - Python type stub for the Indigo home automation server plugin API.

This stub provides IDE autocompletion (PyCharm, VS Code/Pylance, etc.) for
plugin and script code running inside IndigoPluginHost3 or IndigoServer.

Generated from:
  - Boost.Python bindings in source/Common Db/*_pyglue.cpp
  - Boost.Python bindings in source/Common Util/*_pyglue.cpp
  - Py3 Libraries/indigo_base.py
  - Py3 Libraries/plugin_base.py
  - wiki server_commands.txt documentation

NOTE: This is a stub file for static analysis only. Do not import it at runtime.
"""

from __future__ import annotations

import datetime
import logging
from typing import Any, Iterator, Tuple

from . import utils

# ==============================================================================
# BEGIN SECTION: C++ Boost.Python bindings
# Source: source/Common Db/*_pyglue.cpp, source/Common Util/*_pyglue.cpp
# To update: read the relevant _pyglue.cpp files and regenerate only this section.
# ==============================================================================

# ---------------------------------------------------------------------------
# Type alias for element keys accepted by most API calls.
# Elements can be addressed by integer ID, string name, or an element instance.
# ---------------------------------------------------------------------------
ElemKey = int | str | "BaseElem"


# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# Enumerations (exposed at module level by Boost.Python)
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

class kProtocol(int):
    """Device protocol type enumeration (indigo.kProtocol.*)."""
    Insteon: kProtocol
    X10: kProtocol
    ZWave: kProtocol
    Plugin: kProtocol

class kAllDeviceSel(int):
    """All-device selector enumeration (indigo.kAllDeviceSel.*)."""
    All: kAllDeviceSel
    Insteon: kAllDeviceSel
    ZWave: kAllDeviceSel
    X10: kAllDeviceSel
    HouseCodeA: kAllDeviceSel
    HouseCodeB: kAllDeviceSel
    HouseCodeC: kAllDeviceSel
    HouseCodeD: kAllDeviceSel
    HouseCodeE: kAllDeviceSel
    HouseCodeF: kAllDeviceSel
    HouseCodeG: kAllDeviceSel
    HouseCodeH: kAllDeviceSel
    HouseCodeI: kAllDeviceSel
    HouseCodeJ: kAllDeviceSel
    HouseCodeK: kAllDeviceSel
    HouseCodeL: kAllDeviceSel
    HouseCodeM: kAllDeviceSel
    HouseCodeN: kAllDeviceSel
    HouseCodeO: kAllDeviceSel
    HouseCodeP: kAllDeviceSel

class kStateImageSel(int):
    """State image selector enumeration (indigo.kStateImageSel.*)."""
    Auto: kStateImageSel
    NoImage: kStateImageSel   # also accessible as kStateImageSel.None (Python keyword workaround)
    Error: kStateImageSel
    Custom: kStateImageSel
    PowerOff: kStateImageSel
    PowerOn: kStateImageSel
    Unlocked: kStateImageSel
    Locked: kStateImageSel
    Closed: kStateImageSel
    Opened: kStateImageSel
    DimmerOff: kStateImageSel
    DimmerOn: kStateImageSel
    FanOff: kStateImageSel
    FanLow: kStateImageSel
    FanMedium: kStateImageSel
    FanHigh: kStateImageSel
    SprinklerOff: kStateImageSel
    SprinklerOn: kStateImageSel
    HvacOff: kStateImageSel
    HvacCoolMode: kStateImageSel
    HvacHeatMode: kStateImageSel
    HvacAutoMode: kStateImageSel
    HvacFanOn: kStateImageSel
    HvacCooling: kStateImageSel
    HvacHeating: kStateImageSel
    SensorOff: kStateImageSel
    SensorOn: kStateImageSel
    SensorTripped: kStateImageSel
    EnergyMeterOff: kStateImageSel
    EnergyMeterOn: kStateImageSel
    LightSensor: kStateImageSel
    LightSensorOn: kStateImageSel
    MotionSensor: kStateImageSel
    MotionSensorTripped: kStateImageSel
    DoorSensorClosed: kStateImageSel
    DoorSensorOpened: kStateImageSel
    WindowSensorClosed: kStateImageSel
    WindowSensorOpened: kStateImageSel
    TemperatureSensor: kStateImageSel
    TemperatureSensorOn: kStateImageSel
    HumiditySensor: kStateImageSel
    HumiditySensorOn: kStateImageSel
    HumidifierOff: kStateImageSel
    HumidifierOn: kStateImageSel
    DehumidifierOff: kStateImageSel
    DehumidifierOn: kStateImageSel
    WindSpeedSensor: kStateImageSel
    WindSpeedSensorLow: kStateImageSel
    WindSpeedSensorMedium: kStateImageSel
    WindSpeedSensorHigh: kStateImageSel
    WindDirectionSensor: kStateImageSel
    WindDirectionSensorNorth: kStateImageSel
    WindDirectionSensorNorthEast: kStateImageSel
    WindDirectionSensorEast: kStateImageSel
    WindDirectionSensorSouthEast: kStateImageSel
    WindDirectionSensorSouth: kStateImageSel
    WindDirectionSensorSouthWest: kStateImageSel
    WindDirectionSensorWest: kStateImageSel
    WindDirectionSensorNorthWest: kStateImageSel
    BatteryCharger: kStateImageSel
    BatteryChargerOn: kStateImageSel
    BatteryLevel: kStateImageSel
    BatteryLevelLow: kStateImageSel
    BatteryLevel25: kStateImageSel
    BatteryLevel50: kStateImageSel
    BatteryLevel75: kStateImageSel
    BatteryLevelHigh: kStateImageSel
    TimerOff: kStateImageSel
    TimerOn: kStateImageSel
    AvStopped: kStateImageSel
    AvPaused: kStateImageSel
    AvPlaying: kStateImageSel

class kHvacMode(int):
    """HVAC operating mode enumeration (indigo.kHvacMode.*)."""
    Off: kHvacMode
    Heat: kHvacMode
    Cool: kHvacMode
    HeatCool: kHvacMode
    ProgramHeat: kHvacMode
    ProgramCool: kHvacMode
    ProgramHeatCool: kHvacMode

class kFanMode(int):
    """Fan mode enumeration (indigo.kFanMode.*)."""
    Auto: kFanMode
    AlwaysOn: kFanMode

class kDateType(int):
    """Schedule date type enumeration (indigo.kDateType.*)."""
    Absolute: kDateType
    EveryDay: kDateType
    DaysOfWeek: kDateType
    DaysOfMonth: kDateType
    DaysOfMonthInterval: kDateType

class kTimeType(int):
    """Schedule time type enumeration (indigo.kTimeType.*)."""
    Absolute: kTimeType
    Countdown: kTimeType
    Sunrise: kTimeType
    Sunset: kTimeType

class kDeviceSourceType(int):
    """Trigger device source type enumeration (indigo.kDeviceSourceType.*)."""
    NoDevice: kDeviceSourceType
    DeviceId: kDeviceSourceType
    AnyDevice: kDeviceSourceType
    RawAddress: kDeviceSourceType

class kInterface(int):
    """Network interface enumeration (indigo.kInterface.*)."""
    All: kInterface
    InsteonX10: kInterface
    X10RF: kInterface
    Plugin: kInterface

class kTriggerKeyType(int):
    """Trigger state-change key type enumeration (indigo.kTriggerKeyType.*)."""
    Label: kTriggerKeyType
    BoolTrueFalse: kTriggerKeyType
    BoolOnOff: kTriggerKeyType
    BoolYesNo: kTriggerKeyType
    BoolOneZero: kTriggerKeyType
    Number: kTriggerKeyType
    Integer: kTriggerKeyType
    Real: kTriggerKeyType
    String: kTriggerKeyType
    Compound: kTriggerKeyType
    Enumeration: kTriggerKeyType

class kStateChange(int):
    """Device state change type enumeration (indigo.kStateChange.*)."""
    BecomesTrue: kStateChange
    BecomesFalse: kStateChange
    BecomesEqual: kStateChange
    BecomesNotEqual: kStateChange
    BecomesGreaterThan: kStateChange
    BecomesLessThan: kStateChange
    Changes: kStateChange

class kVarChange(int):
    """Variable change type enumeration (indigo.kVarChange.*)."""
    BecomesTrue: kVarChange
    BecomesFalse: kVarChange
    BecomesEqual: kVarChange
    BecomesNotEqual: kVarChange
    BecomesGreaterThan: kVarChange
    BecomesLessThan: kVarChange
    Changes: kVarChange

class kLicenseStatus(int):
    """License status enumeration (indigo.kLicenseStatus.*)."""
    Unknown: kLicenseStatus
    ActiveTrial: kLicenseStatus
    ActiveSubscription: kLicenseStatus
    ExpiredSubscription: kLicenseStatus

class kAcctCommResult(int):
    """Account communication result enumeration (indigo.kAcctCommResult.*)."""
    NoErr: kAcctCommResult
    Unknown: kAcctCommResult
    MiscErr: kAcctCommResult
    ConnectivityFailed: kAcctCommResult
    NeedCredentials: kAcctCommResult
    AuthenticationFailed: kAcctCommResult
    LoadFailed: kAcctCommResult

class kDeviceAction(int):
    """Device action type enumeration (indigo.kDeviceAction.*)."""
    On: kDeviceAction
    Off: kDeviceAction
    Toggle: kDeviceAction
    Lock: kDeviceAction
    Unlock: kDeviceAction
    Open: kDeviceAction
    Close: kDeviceAction
    SetBrightness: kDeviceAction
    BrightenBy: kDeviceAction
    DimBy: kDeviceAction
    SetColorLevels: kDeviceAction
    AllOff: kDeviceAction
    AllLightsOn: kDeviceAction
    AllLightsOff: kDeviceAction
    RequestStatus: kDeviceAction

class kDimmerRelayAction(int):
    """Dimmer/relay action type enumeration (indigo.kDimmerRelayAction.*)."""
    On: kDimmerRelayAction
    Off: kDimmerRelayAction
    Toggle: kDimmerRelayAction
    SetBrightness: kDimmerRelayAction
    BrightenBy: kDimmerRelayAction
    DimBy: kDimmerRelayAction
    SetColorLevels: kDimmerRelayAction
    AllOff: kDimmerRelayAction
    AllLightsOn: kDimmerRelayAction
    AllLightsOff: kDimmerRelayAction

class kSensorAction(int):
    """Sensor action type enumeration (indigo.kSensorAction.*)."""
    TurnOn: kSensorAction
    TurnOff: kSensorAction
    Toggle: kSensorAction
    RequestStatus: kSensorAction

class kSpeedControlAction(int):
    """Speed control action type enumeration (indigo.kSpeedControlAction.*)."""
    TurnOn: kSpeedControlAction
    TurnOff: kSpeedControlAction
    Toggle: kSpeedControlAction
    SetSpeedLevel: kSpeedControlAction
    SetSpeedIndex: kSpeedControlAction
    IncreaseSpeedIndex: kSpeedControlAction
    DecreaseSpeedIndex: kSpeedControlAction
    RequestStatus: kSpeedControlAction

class kSprinklerAction(int):
    """Sprinkler action type enumeration (indigo.kSprinklerAction.*)."""
    RunNewSchedule: kSprinklerAction
    RunPreviousSchedule: kSprinklerAction
    PauseSchedule: kSprinklerAction
    ResumeSchedule: kSprinklerAction
    StopSchedule: kSprinklerAction
    PreviousZone: kSprinklerAction
    NextZone: kSprinklerAction
    ZoneOn: kSprinklerAction
    AllZonesOff: kSprinklerAction
    RequestStatusAll: kSprinklerAction

class kThermostatAction(int):
    """Thermostat action type enumeration (indigo.kThermostatAction.*)."""
    SetHeatSetpoint: kThermostatAction
    SetCoolSetpoint: kThermostatAction
    IncreaseHeatSetpoint: kThermostatAction
    IncreaseCoolSetpoint: kThermostatAction
    DecreaseHeatSetpoint: kThermostatAction
    DecreaseCoolSetpoint: kThermostatAction
    SetHvacMode: kThermostatAction
    SetFanMode: kThermostatAction
    RequestStatusAll: kThermostatAction
    RequestMode: kThermostatAction
    RequestEquipmentState: kThermostatAction
    RequestTemperatures: kThermostatAction
    RequestHumidities: kThermostatAction
    RequestDeadbands: kThermostatAction
    RequestSetpoints: kThermostatAction

class kUniversalAction(int):
    """Universal device action type enumeration (indigo.kUniversalAction.*)."""
    RequestStatus: kUniversalAction
    Beep: kUniversalAction
    EnergyUpdate: kUniversalAction
    EnergyReset: kUniversalAction

class kInsteonCmd(int):
    """INSTEON command type enumeration (indigo.kInsteonCmd.*)."""
    On: kInsteonCmd
    InstantOn: kInsteonCmd
    Off: kInsteonCmd
    InstantOff: kInsteonCmd
    Brighten: kInsteonCmd
    Dim: kInsteonCmd
    AllOn: kInsteonCmd
    AllOff: kInsteonCmd
    AllBrighten: kInsteonCmd
    AllDim: kInsteonCmd
    AnyCommand: kInsteonCmd
    StatusChanged: kInsteonCmd
    AllInstantOn: kInsteonCmd
    AllInstantOff: kInsteonCmd

class kX10Cmd(int):
    """X10 command type enumeration (indigo.kX10Cmd.*)."""
    AllOff: kX10Cmd
    AllLightsOn: kX10Cmd
    AllLightsOff: kX10Cmd
    On: kX10Cmd
    Off: kX10Cmd
    Brighten: kX10Cmd
    Dim: kX10Cmd
    PresetDim: kX10Cmd
    ExtendedData: kX10Cmd
    StatusOnResponse: kX10Cmd
    StatusOffResponse: kX10Cmd
    AvButtonPressed: kX10Cmd
    AnyCommand: kX10Cmd

class kX10AvButton(int):
    """X10 AV button type enumeration (indigo.kX10AvButton.*)."""
    Power: kX10AvButton
    PC: kX10AvButton
    Display: kX10AvButton
    Menu: kX10AvButton
    Recall: kX10AvButton
    Enter: kX10AvButton
    Exit: kX10AvButton
    Title: kX10AvButton
    Right: kX10AvButton
    Left: kX10AvButton
    Down: kX10AvButton
    Up: kX10AvButton
    Return: kX10AvButton
    Mute: kX10AvButton
    AB: kX10AvButton
    ChannelUp: kX10AvButton
    ChannelDown: kX10AvButton
    VolumeUp: kX10AvButton
    VolumeDown: kX10AvButton
    Play: kX10AvButton
    Record: kX10AvButton
    Stop: kX10AvButton
    Pause: kX10AvButton
    Rewind: kX10AvButton
    Forward: kX10AvButton

class kEmailFilter(int):
    """Email filter type enumeration (indigo.kEmailFilter.*)."""
    AnyEmail: kEmailFilter
    MatchEmailFields: kEmailFilter

class kElemTypeId(int):
    """Element type ID enumeration (indigo.kElemTypeId.*)."""
    ActionGroup: kElemTypeId
    Device: kElemTypeId
    Schedule: kElemTypeId
    Trigger: kElemTypeId
    Variable: kElemTypeId
    ControlPage: kElemTypeId
    DeviceGroup: kElemTypeId

class kSubAtomicTypeId(int):
    """Sub-atomic element type ID enumeration (indigo.kSubAtomicTypeId.*)."""
    Device: kSubAtomicTypeId
    Trigger: kSubAtomicTypeId
    Schedule: kSubAtomicTypeId
    Condition: kSubAtomicTypeId
    Action: kSubAtomicTypeId
    Control: kSubAtomicTypeId

class kProgressDescType(int):
    """Progress description type enumeration (indigo.kProgressDescType.*)."""
    Unused: kProgressDescType
    Generic: kProgressDescType
    Generic_fail: kProgressDescType
    Sent: kProgressDescType
    Sent_fail: kProgressDescType
    Received: kProgressDescType
    Received_fail: kProgressDescType
    Processed: kProgressDescType
    Processed_fail: kProgressDescType
    Executed: kProgressDescType
    Executed_fail: kProgressDescType

class kDeprecatedTypeId(int):
    """Deprecated type ID enumeration (indigo.kDeprecatedTypeId.*)."""
    ExecuteEmbeddedAppleScript: kDeprecatedTypeId
    ExecuteLinkedAppleScript: kDeprecatedTypeId

# Device sub-type constant groups
class RelayDeviceSubTypes:
    """Type object for indigo.kRelayDeviceSubType instances (string-valued constants)."""
    DoorBell: str
    DoorController: str
    GarageController: str
    InLine: str
    Lock: str
    Outlet: str
    PlugIn: str
    Siren: str
    Switch: str

kRelayDeviceSubType: RelayDeviceSubTypes
"""String sub-type constants for relay devices (indigo.kRelayDeviceSubType.*)."""

class DimmerDeviceSubTypes:
    """Type object for indigo.kDimmerDeviceSubType instances (string-valued constants)."""
    Blind: str
    Bulb: str
    ColorBulb: str
    ColorDimmer: str
    Dimmer: str
    Fan: str
    InLine: str
    Outlet: str
    PlugIn: str
    Valve: str

kDimmerDeviceSubType: DimmerDeviceSubTypes
"""String sub-type constants for dimmer devices (indigo.kDimmerDeviceSubType.*)."""

class SensorDeviceSubTypes:
    """Type object for indigo.kSensorDeviceSubType instances (string-valued constants)."""
    Analog: str
    Binary: str
    CO: str
    DoorWindow: str
    GasLeak: str
    GlassBreak: str
    Humidity: str
    Illuminance: str
    Motion: str
    Presence: str
    Pressure: str
    Smoke: str
    Tamper: str
    Temperature: str
    UV: str
    Vibration: str
    Voltage: str
    WaterLeak: str
    Zone: str

kSensorDeviceSubType: SensorDeviceSubTypes
"""String sub-type constants for sensor devices (indigo.kSensorDeviceSubType.*)."""

class DeviceSubTypes:
    """Type object for indigo.kDeviceSubType instances (string-valued constants)."""
    AlarmSystem: str
    Amplifier: str
    Automobile: str
    Camera: str
    Keypad: str
    Mobile: str
    Remote: str
    Robot: str
    Security: str
    Speaker: str
    Streaming: str
    Television: str
    Weather: str
    Other: str

kDeviceSubType: DeviceSubTypes
"""String sub-type constants for generic devices (indigo.kDeviceSubType.*)."""


# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# Base element and collection classes
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

class Dict(dict):
    """
    Indigo dict wrapper. Behaves like a regular Python dict but may carry
    additional Indigo metadata. Used for pluginProps, globalProps, sharedProps, etc.
    """

    def get(self, key: str, default: Any = None) -> Any:
        """Return the value for *key* if present, else *default*."""
        ...

    def to_dict(self) -> dict:
        """Recursively convert to a plain Python dict, converting any nested
        indigo.Dict / indigo.List values and Indigo constants to their Python equivalents.
        Patched in by utils.py.
        """
        ...


class List(list):
    """
    Indigo list wrapper. Behaves like a regular Python list but may carry
    additional Indigo metadata.
    """

    def to_list(self) -> list:
        """Recursively convert to a plain Python list, converting any nested
        indigo.Dict / indigo.List values and Indigo constants to their Python equivalents.
        Patched in by utils.py.
        """
        ...


class BaseElem:
    """
    Base class for all Indigo database elements (devices, variables, triggers,
    schedules, action groups, control pages, folders).

    Exposed in Python as ``indigo.BaseElem``.
    Properties defined in CListElem_pyglue.cpp.
    """

    @property
    def id(self) -> int:
        """Unique integer ID of the element."""
        ...

    @property
    def name(self) -> str:
        """Display name of the element."""
        ...

    @name.setter
    def name(self, value: str) -> None: ...

    @property
    def description(self) -> str:
        """Description string of the element."""
        ...

    @description.setter
    def description(self, value: str) -> None: ...

    @property
    def remoteDisplay(self) -> bool:
        """Whether the element is displayed in remote UIs (Indigo Touch, web server)."""
        ...

    @remoteDisplay.setter
    def remoteDisplay(self, value: bool) -> None: ...

    @property
    def globalProps(self) -> "Dict":
        """Dict of all plugin-specific props (keyed by pluginId)."""
        ...

    @property
    def ownerProps(self) -> "Dict":
        """
        Dict of props owned by the plugin that owns this element
        (same as pluginProps for plugins, but accessible by all).
        """
        ...

    @property
    def pluginProps(self) -> "Dict":
        """
        Dict of props for the calling plugin (the plugin's own namespace
        within globalProps). Read-only; use replacePluginPropsOnServer()
        to persist changes.
        """
        ...

    @property
    def sharedProps(self) -> "Dict":
        """
        Dict of shared props visible to all plugins. Read-only; use
        replaceSharedPropsOnServer() to persist changes.
        """
        ...


# ---------------------------------------------------------------------------
# Folder element
# ---------------------------------------------------------------------------

class Folder(BaseElem):
    """
    A folder that can contain other elements.

    Exposed in Python as ``indigo.Folder``.
    Properties defined in CFolderElem_pyglue.cpp.
    """

    def refreshFromServer(self, waitUntilServerIdle: bool = False) -> None:
        """Refresh all folder properties from the server."""
        ...

    def replaceOnServer(self) -> None:
        """Push local changes to the server."""
        ...

    def __iter__(self) -> Iterator[tuple[str, Any]]:
        """Yields (key, value) pairs so dict(folder) works. Patched in by utils.py."""
        ...


class FolderCmds:
    """
    Command interface for folder operations, also behaves as a collection.
    Do not instantiate directly; use the pre-created instances
    (e.g. ``indigo.devices.folders``).
    """

    # --- collection interface ---
    def __getitem__(self, key: ElemKey) -> Folder: ...
    def __contains__(self, key: object) -> bool: ...
    def __iter__(self) -> Iterator[Folder]: ...
    def __len__(self) -> int: ...

    def get(self, key: ElemKey, default: Any = None) -> Folder | None:
        """Return folder by key, or *default* if not found."""
        ...

    def keys(self, filter: str = "") -> list[int]:
        """Return a list of folder IDs, optionally filtered."""
        ...

    def has_key(self, key: ElemKey) -> bool:
        """Return True if *key* exists in the folder collection."""
        ...

    def iter(self, filter: str = "") -> Iterator[Folder]:
        """Iterate folder objects with an optional filter expression."""
        ...

    def itervalues(self, filter: str = "") -> Iterator[Folder]:
        """Alias for iter()."""
        ...

    def iterkeys(self, filter: str = "") -> Iterator[int]:
        """Iterate folder IDs with an optional filter expression."""
        ...

    def len(self, filter: str = "") -> int:
        """Return the number of folders, optionally filtered."""
        ...

    def getName(self, key: int) -> str:
        """Return the name for folder *key* (ID), or '' if not found."""
        ...

    def getId(self, name: str) -> int:
        """Return the ID for folder *name*, or 0 if not found."""
        ...

    # --- command interface ---
    def create(self, name: str) -> Folder:
        """Add a new folder to the Indigo Server."""
        ...

    def duplicate(self, elem: ElemKey, duplicateName: str = "") -> Folder:
        """Duplicate an existing folder on the Indigo Server."""
        ...

    def delete(self, elem: ElemKey, deleteAllChildren: bool = False) -> None:
        """Delete an existing folder from the Indigo Server."""
        ...

    def displayInRemoteUI(self, elem: ElemKey, value: bool) -> None:
        """Change a folder's remote UI display visibility."""
        ...


# ---------------------------------------------------------------------------
# Dict-like collection with folder sub-interface
# ---------------------------------------------------------------------------

class _ElemCollection:
    """
    Base class for all Indigo element collection objects
    (indigo.devices, indigo.variables, etc.).

    Supports dict-like access by element ID (int) or name (str).
    Iteration yields element values (not keys).

    The optional *filter* argument accepted by iter(), itervalues(),
    iterkeys(), keys(), and len() is a Python expression string evaluated
    against each element; only elements for which it is truthy are included
    (e.g. ``filter="self.enabled"``).
    """

    folders: FolderCmds

    def __getitem__(self, key: ElemKey) -> Any: ...
    def __contains__(self, key: object) -> bool: ...
    def __iter__(self) -> Iterator[Any]:
        """Iterate values (elements), not keys."""
        ...
    def __len__(self) -> int: ...

    def get(self, key: ElemKey, default: Any = None) -> Any:
        """Return element by key, or *default* if not found."""
        ...

    def keys(self, filter: str = "") -> list[int]:
        """Return a list of element IDs, optionally filtered."""
        ...

    def has_key(self, key: ElemKey) -> bool:
        """Return True if *key* exists in the collection (alias for ``in``)."""
        ...

    def iter(self, filter: str = "") -> Iterator[Any]:
        """Iterate values (elements) with an optional filter expression."""
        ...

    def itervalues(self, filter: str = "") -> Iterator[Any]:
        """Alias for iter(). Iterate values with an optional filter expression."""
        ...

    def iterkeys(self, filter: str = "") -> Iterator[int]:
        """Iterate element IDs with an optional filter expression."""
        ...

    def len(self, filter: str = "") -> int:
        """Return the number of elements, optionally filtered."""
        ...

    def getName(self, key: int) -> str:
        """Return the name for element *key* (ID), or '' if not found."""
        ...

    def getId(self, name: str) -> int:
        """Return the ID for element *name*, or 0 if not found."""
        ...

    def subscribeToChanges(self) -> None:
        """Subscribe the calling plugin to change notifications for this collection."""
        ...


class DeviceList(_ElemCollection):
    """Collection of all Indigo devices (``indigo.devices``)."""

    def __getitem__(self, key: ElemKey) -> "Device": ...  # type: ignore[override]
    def __iter__(self) -> Iterator["Device"]: ...  # type: ignore[override]
    def iter(self, filter: str = "") -> Iterator["Device"]: ...  # type: ignore[override]
    def itervalues(self, filter: str = "") -> Iterator["Device"]: ...  # type: ignore[override]
    def iterkeys(self, filter: str = "") -> Iterator[int]: ...


class VariableList(_ElemCollection):
    """Collection of all Indigo variables (``indigo.variables``)."""

    def __getitem__(self, key: ElemKey) -> "Variable": ...  # type: ignore[override]
    def __iter__(self) -> Iterator["Variable"]: ...  # type: ignore[override]
    def iter(self, filter: str = "") -> Iterator["Variable"]: ...  # type: ignore[override]
    def itervalues(self, filter: str = "") -> Iterator["Variable"]: ...  # type: ignore[override]
    def iterkeys(self, filter: str = "") -> Iterator[int]: ...


class TriggerList(_ElemCollection):
    """Collection of all Indigo triggers (``indigo.triggers``)."""

    def __getitem__(self, key: ElemKey) -> "Trigger": ...  # type: ignore[override]
    def __iter__(self) -> Iterator["Trigger"]: ...  # type: ignore[override]
    def iter(self, filter: str = "") -> Iterator["Trigger"]: ...  # type: ignore[override]
    def itervalues(self, filter: str = "") -> Iterator["Trigger"]: ...  # type: ignore[override]
    def iterkeys(self, filter: str = "") -> Iterator[int]: ...


class ScheduleList(_ElemCollection):
    """Collection of all Indigo schedules (``indigo.schedules``)."""

    def __getitem__(self, key: ElemKey) -> "Schedule": ...  # type: ignore[override]
    def __iter__(self) -> Iterator["Schedule"]: ...  # type: ignore[override]
    def iter(self, filter: str = "") -> Iterator["Schedule"]: ...  # type: ignore[override]
    def itervalues(self, filter: str = "") -> Iterator["Schedule"]: ...  # type: ignore[override]
    def iterkeys(self, filter: str = "") -> Iterator[int]: ...


class ActionGroupList(_ElemCollection):
    """Collection of all Indigo action groups (``indigo.actionGroups``)."""

    def __getitem__(self, key: ElemKey) -> "ActionGroup": ...  # type: ignore[override]
    def __iter__(self) -> Iterator["ActionGroup"]: ...  # type: ignore[override]
    def iter(self, filter: str = "") -> Iterator["ActionGroup"]: ...  # type: ignore[override]
    def itervalues(self, filter: str = "") -> Iterator["ActionGroup"]: ...  # type: ignore[override]
    def iterkeys(self, filter: str = "") -> Iterator[int]: ...


class ControlPageList(_ElemCollection):
    """Collection of all Indigo control pages (``indigo.controlPages``)."""

    def __getitem__(self, key: ElemKey) -> "ControlPage": ...  # type: ignore[override]
    def __iter__(self) -> Iterator["ControlPage"]: ...  # type: ignore[override]
    def iter(self, filter: str = "") -> Iterator["ControlPage"]: ...  # type: ignore[override]
    def itervalues(self, filter: str = "") -> Iterator["ControlPage"]: ...  # type: ignore[override]
    def iterkeys(self, filter: str = "") -> Iterator[int]: ...


# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# Device classes
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

class Device(BaseElem):
    """
    Base class for all Indigo device types.

    Exposed in Python as ``indigo.Device``.
    Properties defined in CDeviceBase_pyglue.cpp.
    """

    # ---- Configuration / identity ----
    @property
    def configured(self) -> bool:
        """True if the device has been fully configured."""
        ...

    @configured.setter
    def configured(self, value: bool) -> None:
        """Owning plugin only: set the configured state directly on the local object,
        then call replaceOnServer() to persist."""
        ...

    @property
    def enabled(self) -> bool:
        """True if the device is enabled for Indigo processing."""
        ...

    @property
    def protocol(self) -> kProtocol:
        """Protocol used by this device (one of indigo.kProtocol.*)."""
        ...

    @property
    def model(self) -> str:
        """Model name string."""
        ...

    @property
    def subType(self) -> int:
        """Device sub-type integer."""
        ...

    @property
    def subModel(self) -> str:
        """Sub-model name string."""
        ...

    @property
    def version(self) -> str:
        """Device version string."""
        ...

    @property
    def address(self) -> str:
        """Protocol address string (e.g. INSTEON address "AA.BB.CC")."""
        ...

    @property
    def deviceTypeId(self) -> str:
        """Plugin-defined device type ID string."""
        ...

    @property
    def pluginId(self) -> str:
        """ID of the plugin that owns this device."""
        ...

    # ---- State / display ----
    @property
    def errorState(self) -> str:
        """
        Current error state string, or empty string if no error.
        Set via setErrorStateOnServer().
        """
        ...

    @property
    def displayStateId(self) -> str:
        """
        State key ID used for the primary display state. Read-only; set
        this locally (dev.displayStateId = "key") then call
        stateListOrDisplayStateIdChanged() to notify the server.
        """
        ...

    @property
    def displayStateValRaw(self) -> Any:
        """Raw value of the display state."""
        ...

    @property
    def displayStateValUi(self) -> str:
        """Human-readable UI string of the display state."""
        ...

    @property
    def displayStateImageSel(self) -> kStateImageSel:
        """Image selector for the display state (one of indigo.kStateImageSel.*)."""
        ...

    @property
    def states(self) -> dict:
        """
        Dict of all device states keyed by state name. Read/write locally;
        use updateStateOnServer() / updateStatesOnServer() to persist.
        """
        ...

    # ---- Hardware / timing ----
    @property
    def buttonGroupCount(self) -> int:
        """Number of button groups on this device."""
        ...

    @property
    def lastChanged(self) -> datetime.datetime:
        """Datetime of the last state change."""
        ...

    @property
    def lastSuccessfulComm(self) -> datetime.datetime:
        """Datetime of the last successful communication."""
        ...

    @property
    def batteryLevel(self) -> int | None:
        """Battery level (0-100), or None if not supported."""
        ...

    # ---- Energy monitoring ----
    @property
    def energyCurLevel(self) -> float | None:
        """Current energy consumption in watts, or None if not available."""
        ...

    @property
    def energyAccumTotal(self) -> float | None:
        """Accumulated energy total in watt-hours, or None if not available."""
        ...

    @property
    def energyAccumBaseTime(self) -> datetime.datetime | None:
        """Base time for energy accumulation, or None if not available."""
        ...

    @property
    def energyAccumTimeDelta(self) -> float | None:
        """Time delta for energy accumulation in seconds, or None."""
        ...

    # ---- Folder ----
    @property
    def folderId(self) -> int:
        """ID of the folder containing this device (0 = root)."""
        ...

    # ---- Capability flags ----
    @property
    def supportsOnState(self) -> bool:
        """True if the device supports an on/off state."""
        ...

    @property
    def supportsAllLightsOnOff(self) -> bool:
        """True if the device responds to All Lights On/Off commands."""
        ...

    @property
    def supportsAllOff(self) -> bool:
        """True if the device responds to All Off commands."""
        ...

    @property
    def supportsStatusRequest(self) -> bool:
        """True if the device supports status request commands."""
        ...

    # ---- Methods ----
    def refreshFromServer(self, waitUntilServerIdle: bool = False) -> None:
        """Refresh all device properties from the server."""
        ...

    def replaceOnServer(self) -> None:
        """Push local changes of the device to the server."""
        ...

    def replacePluginPropsOnServer(self, newProps: dict) -> None:
        """Replace the entire pluginProps dict on the server."""
        ...

    def replaceSharedPropsOnServer(self, newProps: dict) -> None:
        """Replace the shared props dict on the server."""
        ...

    def setErrorStateOnServer(self, errorState: str) -> None:
        """Set (or clear) the device error state on the server."""
        ...

    def stateListOrDisplayStateIdChanged(self) -> None:
        """
        Notify the server that the device's state list definition or
        displayStateId has changed. Called after modifying displayStateId locally.
        """
        ...

    def updateStateOnServer(
        self,
        key: str,
        value: Any,
        uiValue: str | None = None,
        clearErrorState: bool = True,
        decimalPlaces: int | None = None,
    ) -> None:
        """Update a single device state on the server."""
        ...

    def updateStatesOnServer(self, stateList: list[Dict]) -> None:
        """
        Update multiple device states on the server in a single call.
        Each dict in stateList should have keys: 'key', 'value', and optionally
        'uiValue', 'decimalPlaces'.
        """
        ...

    def updateStateImageOnServer(self, imageSelector: kStateImageSel) -> None:
        """Update the device's state image on the server (indigo.kStateImageSel.*)."""
        ...

    def updateTimeStampOnServer(self) -> None:
        """Update the lastSuccessfulComm timestamp on the server to now."""
        ...

    def __iter__(self) -> Iterator[tuple[str, Any]]:
        """Yields (key, value) pairs so dict(dev) works. Patched in by utils.py."""
        ...


class RelayDevice(Device):
    """
    A relay (on/off) device.

    Exposed in Python as ``indigo.RelayDevice``.
    Properties defined in CDeviceRelay_pyglue.cpp.
    """

    @property
    def onState(self) -> bool:
        """True if the relay is currently on. Read-only; use indigo.device.turnOn/Off/toggle() to change."""
        ...

    @property
    def buttonConfiguredCount(self) -> int:
        """Number of configured buttons on this device."""
        ...

    @property
    def ledStates(self) -> list[bool]:
        """List of boolean LED states."""
        ...


class DimmerDevice(RelayDevice):
    """
    A dimmer (variable brightness) device.

    Exposed in Python as ``indigo.DimmerDevice``.
    Properties defined in CDeviceDimmer_pyglue.cpp.
    """

    @property
    def brightness(self) -> int:
        """Current brightness level (0-100). Read-only; use indigo.dimmer.setBrightness() to change."""
        ...

    @property
    def defaultBrightness(self) -> int:
        """Default brightness level (0-100) when turned on. Read-only."""
        ...

    @property
    def onBrightensToDefaultToggle(self) -> bool:
        """True if turning on brightens to the default level. Read-only."""
        ...

    @property
    def onBrightensToLast(self) -> bool:
        """True if turning on brightens to the last brightness level. Read-only."""
        ...

    # ---- Color ----
    @property
    def supportsColor(self) -> bool:
        """True if the device supports color control."""
        ...

    @property
    def supportsRGB(self) -> bool:
        """True if the device supports RGB color."""
        ...

    @property
    def supportsWhite(self) -> bool:
        """True if the device supports a white channel."""
        ...

    @property
    def supportsTwoWhiteLevels(self) -> bool:
        """True if the device supports two independent white level channels."""
        ...

    @property
    def supportsWhiteTemperature(self) -> bool:
        """True if the device supports white color temperature."""
        ...

    @property
    def supportsRGBandWhiteSimultaneously(self) -> bool:
        """True if RGB and white channels can be active simultaneously."""
        ...

    @property
    def redLevel(self) -> int:
        """Red color channel level (0-100). Read-only; use indigo.dimmer.setColorLevels() to change."""
        ...

    @property
    def greenLevel(self) -> int:
        """Green color channel level (0-100). Read-only; use indigo.dimmer.setColorLevels() to change."""
        ...

    @property
    def blueLevel(self) -> int:
        """Blue color channel level (0-100). Read-only; use indigo.dimmer.setColorLevels() to change."""
        ...

    @property
    def whiteLevel(self) -> int:
        """White channel level (0-100). Read-only; use indigo.dimmer.setColorLevels() to change."""
        ...

    @property
    def whiteLevel2(self) -> int:
        """Second white channel level (0-100). Read-only; use indigo.dimmer.setColorLevels() to change."""
        ...

    @property
    def whiteTemperature(self) -> int:
        """White color temperature in Kelvin. Read-only; use indigo.dimmer.setColorLevels() to change."""
        ...


class SensorDevice(Device):
    """
    A sensor (read-only state) device.

    Exposed in Python as ``indigo.SensorDevice``.
    Properties defined in CDeviceSensor_pyglue.cpp.
    """

    @property
    def onState(self) -> bool | None:
        """Boolean on/off state of the sensor, or None if not applicable."""
        ...

    @property
    def allowOnStateChange(self) -> bool:
        """True if plugins are allowed to change the onState via updateStateOnServer."""
        ...

    @property
    def sensorValue(self) -> float | None:
        """Numeric sensor value, or None if not applicable."""
        ...

    @property
    def allowSensorValueChange(self) -> bool:
        """True if plugins are allowed to change the sensorValue via updateStateOnServer."""
        ...

    @property
    def supportsSensorValue(self) -> bool:
        """True if this sensor supports a numeric sensorValue."""
        ...


class SpeedControlDevice(Device):
    """
    A multi-speed fan/motor control device.

    Exposed in Python as ``indigo.SpeedControlDevice``.
    Properties defined in CDeviceSpeedControl_pyglue.cpp.
    """

    @property
    def onState(self) -> bool:
        """True if the speed control device is on (speedIndex > 0). Read-only; use indigo.speedcontrol.turnOn/Off() to change."""
        ...

    @property
    def speedLevel(self) -> int:
        """Current speed as a percentage (0-100). Read-only; use indigo.speedcontrol.setSpeedLevel() to change."""
        ...

    @property
    def speedIndex(self) -> int:
        """Current speed as an index (0 = off, 1-N = speed steps). Read-only; use indigo.speedcontrol.setSpeedIndex() to change."""
        ...

    @property
    def speedIndexCount(self) -> int:
        """Total number of speed steps (excluding off)."""
        ...


class ThermostatDevice(Device):
    """
    A thermostat device.

    Exposed in Python as ``indigo.ThermostatDevice``.
    Properties defined in CDeviceThermostat_pyglue.cpp.
    """

    @property
    def hvacMode(self) -> kHvacMode:
        """Current HVAC operating mode (one of indigo.kHvacMode.*). Read-only; use indigo.thermostat.setHvacMode() to change."""
        ...

    @property
    def fanMode(self) -> kFanMode:
        """Current fan mode (one of indigo.kFanMode.*). Read-only; use indigo.thermostat.setFanMode() to change."""
        ...

    @property
    def coolSetpoint(self) -> float:
        """Cool setpoint temperature. Read-only; use indigo.thermostat.setCoolSetpoint() to change."""
        ...

    @property
    def heatSetpoint(self) -> float:
        """Heat setpoint temperature. Read-only; use indigo.thermostat.setHeatSetpoint() to change."""
        ...

    @property
    def temperatures(self) -> list[float]:
        """List of current temperatures (one per sensor zone)."""
        ...

    @property
    def humidities(self) -> list[float]:
        """List of current humidity values (one per sensor)."""
        ...

    @property
    def coolSetpoints(self) -> list[float]:
        """List of cool setpoints (for multi-zone thermostats)."""
        ...

    @property
    def heatSetpoints(self) -> list[float]:
        """List of heat setpoints (for multi-zone thermostats)."""
        ...

    @property
    def hvacOperationModeIsOff(self) -> bool:
        """True if HVAC mode is Off."""
        ...

    @property
    def hvacOperationModeIsHeat(self) -> bool:
        """True if HVAC mode is Heat."""
        ...

    @property
    def hvacOperationModeIsCool(self) -> bool:
        """True if HVAC mode is Cool."""
        ...

    @property
    def hvacOperationModeIsHeatCool(self) -> bool:
        """True if HVAC mode is Heat/Cool."""
        ...

    @property
    def hvacOperationModeIsProgramHeat(self) -> bool:
        """True if HVAC mode is Program Heat."""
        ...

    @property
    def hvacOperationModeIsProgramCool(self) -> bool:
        """True if HVAC mode is Program Cool."""
        ...

    @property
    def hvacOperationModeIsProgramHeatCool(self) -> bool:
        """True if HVAC mode is Program Heat/Cool."""
        ...

    @property
    def hvacFanModeIsAuto(self) -> bool:
        """True if fan mode is Auto."""
        ...

    @property
    def hvacFanModeIsAlwaysOn(self) -> bool:
        """True if fan mode is Always On."""
        ...

    @property
    def fanIsOn(self) -> bool:
        """True if the fan is currently running (shortcut for dev.states['hvacFanIsOn'])."""
        ...

    @property
    def coolIsOn(self) -> bool:
        """True if the cooling system (compressor) is currently running (shortcut for dev.states['hvacCoolerIsOn'])."""
        ...

    @property
    def heatIsOn(self) -> bool:
        """True if the heater is currently running (shortcut for dev.states['hvacHeaterIsOn'])."""
        ...

    @property
    def temperatureInputsAll(self) -> list[float]:
        """All temperature input values."""
        ...

    @property
    def humidityInputsAll(self) -> list[float]:
        """All humidity input values."""
        ...

    @property
    def numTemperatureInputs(self) -> int:
        """Number of temperature inputs."""
        ...

    @property
    def numHumidityInputs(self) -> int:
        """Number of humidity inputs."""
        ...

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
        ...

    @property
    def zoneCount(self) -> int:
        """Number of zones on this device."""
        ...

    @property
    def zoneEnableList(self) -> list[bool]:
        """List of booleans indicating which zones are enabled."""
        ...

    @property
    def zoneNames(self) -> list[str]:
        """List of zone name strings."""
        ...

    @property
    def zoneMaxDurations(self) -> list[float | None]:
        """List of maximum zone durations in minutes (None if unlimited)."""
        ...

    @property
    def zoneScheduledDurations(self) -> list[float]:
        """List of scheduled zone durations in minutes."""
        ...

    @property
    def pausedScheduleZone(self) -> int | None:
        """1-based index of the paused zone, or None if not paused."""
        ...

    @property
    def pausedScheduleRemainingZoneDuration(self) -> float | None:
        """Remaining duration in minutes for the paused zone, or None."""
        ...


class MultiIODevice(Device):
    """
    A multi-I/O device (digital/analog inputs and outputs).

    Exposed in Python as ``indigo.MultiIODevice``.
    Properties defined in CDeviceMultiIO_pyglue.cpp.
    """

    @property
    def analogInputCount(self) -> int:
        """Number of analog inputs."""
        ...

    @property
    def binaryInputCount(self) -> int:
        """Number of binary (digital) inputs."""
        ...

    @property
    def sensorInputCount(self) -> int:
        """Number of sensor inputs."""
        ...

    @property
    def binaryOutputCount(self) -> int:
        """Number of binary (relay) outputs."""
        ...

    @property
    def analogInputs(self) -> list[int]:
        """List of current analog input values."""
        ...

    @property
    def binaryInputs(self) -> list[bool]:
        """List of current binary input states."""
        ...

    @property
    def sensorInputs(self) -> list[int]:
        """List of current sensor input values."""
        ...

    @property
    def binaryOutputs(self) -> list[bool]:
        """List of current binary output states."""
        ...


# ---------------------------------------------------------------------------
# Device command interfaces
# ---------------------------------------------------------------------------

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
        ...

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
        ...

    def duplicate(self, device: ElemKey, duplicateName: str = "") -> Device:
        """Duplicate an existing device."""
        ...

    def delete(self, device: ElemKey) -> None:
        """Delete a device from the Indigo Server."""
        ...

    def getDependencies(self, device: ElemKey | List | Tuple) -> Any:
        """Return all element dependencies for the given device(s)."""
        ...

    def getGroupList(self, device: ElemKey) -> list[int]:
        """Return a list of device IDs in the same group as the given device."""
        ...

    def groupWithDevice(self, device: ElemKey, groupWithDevice: ElemKey) -> None:
        """Add a device to the same group as another device."""
        ...

    def ungroupDevice(self, device: ElemKey) -> None:
        """Remove a device from its group."""
        ...

    def moveToFolder(self, device: ElemKey, value: ElemKey) -> None:
        """Move a device to a different folder."""
        ...

    def displayInRemoteUI(self, device: ElemKey, value: bool) -> None:
        """Change a device's remote UI display visibility."""
        ...

    def enable(self, device: ElemKey, value: bool, delay: int = 0, duration: int = 0) -> None:
        """Enable or disable a device with optional delay and duration (in seconds)."""
        ...

    def changeDeviceTypeId(self, device: ElemKey, deviceTypeId: str) -> None:
        """Change the device type ID of a device."""
        ...

    def x10ChangeAddress(self, device: ElemKey, address: str) -> None:
        """Change the X10 address of a device."""
        ...

    def x10ChangeModel(self, device: ElemKey, model: str) -> None:
        """Change the X10 model of a device."""
        ...

    def removeDelayedActions(self, device: ElemKey) -> None:
        """Remove all pending delayed actions for the given device."""
        ...

    def allOff(self, suppressLogging: bool = False, updateStatesOnly: bool = False) -> None:
        """Send All Off command."""
        ...

    def beep(self, device: ElemKey, suppressLogging: bool = False) -> None:
        """Send a beep command to the device."""
        ...

    def statusRequest(
        self,
        device: ElemKey,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
    ) -> None:
        """Request a status update from the device."""
        ...

    def ping(self, device: ElemKey, suppressLogging: bool = False) -> None:
        """Send a ping to the device."""
        ...

    def turnOn(
        self,
        device: ElemKey,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
        delay: int = 0,
    ) -> None:
        """Turn the device on."""
        ...

    def turnOff(
        self,
        device: ElemKey,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
        delay: int = 0,
    ) -> None:
        """Turn the device off."""
        ...

    def toggle(
        self,
        device: ElemKey,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
        delay: int = 0,
    ) -> None:
        """Toggle the device on/off state."""
        ...

    def lock(
        self,
        device: ElemKey,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
    ) -> None:
        """Send a lock command to the device."""
        ...

    def unlock(
        self,
        device: ElemKey,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
    ) -> None:
        """Send an unlock command to the device."""
        ...

    def open(
        self,
        device: ElemKey,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
    ) -> None:
        """Send an open command to the device."""
        ...

    def close(
        self,
        device: ElemKey,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
    ) -> None:
        """Send a close command to the device."""
        ...

    def energyResetTotal(self, device: ElemKey, suppressLogging: bool = False) -> None:
        """Reset the device's accumulated energy total."""
        ...

    def energyUpdate(self, device: ElemKey, suppressLogging: bool = False) -> None:
        """Request an energy update from the device."""
        ...


class RelayDeviceCmds(DeviceCmds):
    """
    Command interface for relay device operations (``indigo.relay``).
    Inherits all DeviceCmds methods.
    Defined in CDeviceRelay_pyglue.cpp.
    """

    def allLightsOff(self, suppressLogging: bool = False, updateStatesOnly: bool = False) -> None:
        """Send All Lights Off command."""
        ...

    def allLightsOn(self, suppressLogging: bool = False, updateStatesOnly: bool = False) -> None:
        """Send All Lights On command."""
        ...

    def setLedState(
        self,
        device: ElemKey,
        index: int,
        value: bool,
        suppressLogging: bool = False,
    ) -> None:
        """Set the state of a specific LED on the device."""
        ...


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
        ...

    def dim(
        self,
        device: ElemKey,
        dimBy: int = 0,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
        delay: int = 0,
    ) -> None:
        """Dim the device by a specified amount."""
        ...

    def setBrightness(
        self,
        device: ElemKey,
        value: int,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
        delay: int = 0,
    ) -> None:
        """Set the device's brightness to a specific level (0-100)."""
        ...

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
        ...


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
        ...


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
        ...

    def decreaseSpeedIndex(
        self,
        device: ElemKey,
        delta: int = 1,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
    ) -> None:
        """Decrease the device's speed index by delta steps."""
        ...

    def setSpeedLevel(
        self,
        device: ElemKey,
        value: int,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
    ) -> None:
        """Set the device's speed to a specific percentage (0-100)."""
        ...

    def setSpeedIndex(
        self,
        device: ElemKey,
        value: int,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
    ) -> None:
        """Set the device's speed to a specific index step."""
        ...


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
        ...

    def setFanMode(
        self,
        device: ElemKey,
        value: kFanMode,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
    ) -> None:
        """Set the fan mode (one of indigo.kFanMode.*)."""
        ...

    def setCoolSetpoint(
        self,
        device: ElemKey,
        value: float,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
    ) -> None:
        """Set the cool setpoint temperature."""
        ...

    def setHeatSetpoint(
        self,
        device: ElemKey,
        value: float,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
    ) -> None:
        """Set the heat setpoint temperature."""
        ...

    def increaseCoolSetpoint(
        self,
        device: ElemKey,
        delta: float = 1.0,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
    ) -> None:
        """Increase the cool setpoint by delta degrees."""
        ...

    def decreaseCoolSetpoint(
        self,
        device: ElemKey,
        delta: float = 1.0,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
    ) -> None:
        """Decrease the cool setpoint by delta degrees."""
        ...

    def increaseHeatSetpoint(
        self,
        device: ElemKey,
        delta: float = 1.0,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
    ) -> None:
        """Increase the heat setpoint by delta degrees."""
        ...

    def decreaseHeatSetpoint(
        self,
        device: ElemKey,
        delta: float = 1.0,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
    ) -> None:
        """Decrease the heat setpoint by delta degrees."""
        ...


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
        ...

    def previousZone(
        self,
        device: ElemKey,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
    ) -> None:
        """Advance to the previous zone."""
        ...

    def pause(
        self,
        device: ElemKey,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
    ) -> None:
        """Pause the current schedule."""
        ...

    def resume(
        self,
        device: ElemKey,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
    ) -> None:
        """Resume a paused schedule."""
        ...

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
        ...

    def stop(
        self,
        device: ElemKey,
        suppressLogging: bool = False,
        updateStatesOnly: bool = False,
    ) -> None:
        """Stop the current schedule."""
        ...

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
        ...

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
        ...


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
        ...


# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# Variable
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

class Variable(BaseElem):
    """
    An Indigo variable.

    Exposed in Python as ``indigo.Variable``.
    Properties defined in CVariableElem_pyglue.cpp.
    """

    @property
    def value(self) -> str:
        """The current string value of the variable."""
        ...

    @value.setter
    def value(self, v: str) -> None: ...

    @property
    def readOnly(self) -> bool:
        """True if the variable is read-only (set at creation via indigo.variable.create())."""
        ...

    @property
    def folderId(self) -> int:
        """ID of the folder containing this variable (0 = root)."""
        ...

    def refreshFromServer(self, waitUntilServerIdle: bool = False) -> None:
        """Refresh all variable properties from the server."""
        ...

    def replaceOnServer(self) -> None:
        """Push local changes of the variable to the server."""
        ...

    def replacePluginPropsOnServer(self, newProps: dict) -> None:
        """Replace the entire pluginProps dict on the server."""
        ...

    def replaceSharedPropsOnServer(self, newProps: dict) -> None:
        """Replace the shared props dict on the server."""
        ...

    def getValue(self, typeFunc: type) -> Any:
        """Return the variable value converted using the specified type function (e.g. int, float)."""
        ...

    def __iter__(self) -> Iterator[tuple[str, Any]]:
        """Yields (key, value) pairs so dict(var) works. Patched in by utils.py."""
        ...


class VariableCmds:
    """
    Command interface for variable operations (``indigo.variable``).
    Defined in CVariableElem_pyglue.cpp.
    """

    def create(
        self,
        name: str = "",
        value: str = "",
        readOnly: bool = False,
        folder: ElemKey | None = None,
    ) -> Variable:
        """Create a new variable on the Indigo Server."""
        ...

    def duplicate(self, elem: ElemKey, duplicateName: str = "") -> Variable:
        """Duplicate an existing variable."""
        ...

    def delete(self, elem: ElemKey) -> None:
        """Delete a variable from the Indigo Server."""
        ...

    def getDependencies(self, elem: ElemKey | List | Tuple) -> Any:
        """Return all element dependencies for the given variable(s)."""
        ...

    def moveToFolder(self, elem: ElemKey, value: ElemKey) -> None:
        """Move a variable to a different folder."""
        ...

    def updateValue(self, elem: ElemKey, value: str) -> None:
        """Update the value of a variable on the server."""
        ...

    def displayInRemoteUI(self, elem: ElemKey, value: bool) -> None:
        """Change a variable's remote UI display visibility."""
        ...


# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# Event / Trigger / Schedule base classes
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

class Event(BaseElem):
    """
    Base class for all Indigo event elements (triggers and schedules).

    Exposed in Python as ``indigo.Event``.
    Properties defined in CEventBase_pyglue.cpp.
    """

    @property
    def folderId(self) -> int:
        """ID of the folder containing this event (0 = root)."""
        ...

    @property
    def configured(self) -> bool:
        """True if the event has been fully configured."""
        ...

    @configured.setter
    def configured(self, value: bool) -> None:
        """Owning plugin only: set the configured state directly on the local object,
        then call replaceOnServer() to persist."""
        ...

    @property
    def enabled(self) -> bool:
        """True if the event is enabled for Indigo processing. Set locally then call replaceOnServer(); also use indigo.trigger.enable() / indigo.schedule.enable()."""
        ...

    @enabled.setter
    def enabled(self, value: bool) -> None: ...

    @property
    def upload(self) -> bool:
        """True if the event is uploaded to remote UI. Set locally then call replaceOnServer(). Always False for plugin triggers."""
        ...

    @upload.setter
    def upload(self, value: bool) -> None: ...

    @property
    def suppressLogging(self) -> bool:
        """True if event execution logging is suppressed. Set locally then call replaceOnServer()."""
        ...

    @suppressLogging.setter
    def suppressLogging(self, value: bool) -> None: ...

    def __iter__(self) -> Iterator[tuple[str, Any]]:
        """Yields (key, value) pairs so dict(trigger/schedule) works. Patched in by utils.py."""
        ...


class Trigger(Event):
    """
    Base class for all Indigo trigger types.

    Exposed in Python as ``indigo.Trigger``.
    Properties defined in CEventTrigger_pyglue.cpp.
    """

    def refreshFromServer(self, waitUntilServerIdle: bool = False) -> None:
        """Refresh all trigger properties from the server."""
        ...

    def replaceOnServer(self) -> None:
        """Push local changes of the trigger to the server."""
        ...

    def replacePluginPropsOnServer(self, newProps: dict) -> None:
        """Replace the entire pluginProps dict on the server."""
        ...

    def replaceSharedPropsOnServer(self, newProps: dict) -> None:
        """Replace the shared props dict on the server."""
        ...


class PluginEventTrigger(Trigger):
    """
    A plugin-defined custom trigger.

    Exposed in Python as ``indigo.PluginEventTrigger``.
    Defined in CEventPluginTrigger_pyglue.cpp.
    """

    @property
    def pluginId(self) -> str:
        """ID of the plugin that defines this trigger type."""
        ...

    @property
    def pluginTypeId(self) -> str:
        """Plugin-defined trigger type ID string."""
        ...


class DeviceStateChangeTrigger(Trigger):
    """
    A trigger that fires when a device state changes.

    Exposed in Python as ``indigo.DeviceStateChangeTrigger``.
    Defined in CEventDevStateChange_pyglue.cpp.
    """

    @property
    def deviceId(self) -> int:
        """ID of the device being watched."""
        ...

    @deviceId.setter
    def deviceId(self, value: int) -> None: ...

    @property
    def stateChangeType(self) -> kStateChange:
        """State change type (one of indigo.kStateChange.*)."""
        ...

    @stateChangeType.setter
    def stateChangeType(self, value: kStateChange) -> None: ...

    @property
    def stateSelector(self) -> str:
        """Base name of the device state being watched."""
        ...

    @stateSelector.setter
    def stateSelector(self, value: str) -> None: ...

    @property
    def stateSelectorIndex(self) -> int:
        """Index portion of the device state selector (0 if none)."""
        ...

    @stateSelectorIndex.setter
    def stateSelectorIndex(self, value: int) -> None: ...

    @property
    def stateValue(self) -> str:
        """Value to compare against for BecomesEqual / etc. change types."""
        ...

    @stateValue.setter
    def stateValue(self, value: str) -> None: ...


class VarValueChangeTrigger(Trigger):
    """
    A trigger that fires when a variable value changes.

    Exposed in Python as ``indigo.VarValueChangeTrigger``.
    Defined in CEventVarValChange_pyglue.cpp.
    """

    @property
    def variableId(self) -> int:
        """ID of the variable being watched."""
        ...

    @variableId.setter
    def variableId(self, value: int) -> None: ...

    @property
    def variableChangeType(self) -> kVarChange:
        """Variable change type (one of indigo.kVarChange.*)."""
        ...

    @variableChangeType.setter
    def variableChangeType(self, value: kVarChange) -> None: ...

    @property
    def variableValue(self) -> str:
        """Value to compare against for BecomesEqual / etc. change types."""
        ...

    @variableValue.setter
    def variableValue(self, value: str) -> None: ...


# ---------------------------------------------------------------------------
# Trigger command interfaces
# ---------------------------------------------------------------------------

class EventTriggerCmds:
    """
    Command interface for general trigger operations (``indigo.trigger``).
    Defined in CEventTrigger_pyglue.cpp.
    """

    def duplicate(self, elem: ElemKey, duplicateName: str = "") -> Trigger:
        """Duplicate an existing trigger."""
        ...

    def delete(self, elem: ElemKey) -> None:
        """Delete a trigger from the Indigo Server."""
        ...

    def getDependencies(self, elem: ElemKey | List | Tuple) -> Any:
        """Return all element dependencies for the given trigger(s)."""
        ...

    def moveToFolder(self, elem: ElemKey, value: ElemKey) -> None:
        """Move a trigger to a different folder."""
        ...

    def displayInRemoteUI(self, elem: ElemKey, value: bool) -> None:
        """Change a trigger's remote UI display visibility."""
        ...

    def enable(self, elem: ElemKey, value: bool, delay: int = 0, duration: int = 0) -> None:
        """Enable or disable a trigger with optional delay and duration (in seconds)."""
        ...

    def execute(
        self,
        elem: ElemKey,
        ignoreConditions: bool = False,
        trigger_data: Dict | dict | None = None,
    ) -> None:
        """
        Execute all actions in a trigger. Conditionals can optionally be ignored.
        trigger_data is an optional dict passed through the trigger pipeline.
        """
        ...

    def removeDelayedActions(self, elem: ElemKey) -> None:
        """Remove all pending delayed actions started by this trigger."""
        ...


class TriggerDevStateChangeCmds(EventTriggerCmds):
    """
    Command interface for device state change trigger operations.
    Defined in CEventDevStateChange_pyglue.cpp.
    """

    def create(
        self,
        name: str = "",
        description: str = "",
        folder: ElemKey | None = None,
    ) -> DeviceStateChangeTrigger:
        """Add a new device state change trigger to the Indigo Server."""
        ...


class TriggerVarValChangeCmds(EventTriggerCmds):
    """
    Command interface for variable value change trigger operations.
    Defined in CEventVarValChange_pyglue.cpp.
    """

    def create(
        self,
        name: str = "",
        description: str = "",
        folder: ElemKey | None = None,
    ) -> VarValueChangeTrigger:
        """Add a new variable value change trigger to the Indigo Server."""
        ...


class TriggerPluginEventCmds(EventTriggerCmds):
    """
    Command interface for plugin trigger operations.
    Defined in CEventPluginTrigger_pyglue.cpp.
    """

    def create(
        self,
        name: str = "",
        description: str = "",
        folder: ElemKey | None = None,
        pluginId: str = "",
        pluginTypeId: str = "",
        props: Dict | None = None,
        configured: bool = True,
    ) -> PluginEventTrigger:
        """Add a new plugin trigger to the Indigo Server."""
        ...


# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# Schedule
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

class Schedule(Event):
    """
    An Indigo time/date schedule.

    Exposed in Python as ``indigo.Schedule``.
    Properties defined in CEventSchedule_pyglue.cpp.
    """

    @property
    def dateType(self) -> kDateType:
        """Date type (one of indigo.kDateType.*)."""
        ...

    @dateType.setter
    def dateType(self, value: kDateType) -> None: ...

    @property
    def timeType(self) -> kTimeType:
        """Time type (one of indigo.kTimeType.*)."""
        ...

    @timeType.setter
    def timeType(self, value: kTimeType) -> None: ...

    @property
    def sunDelta(self) -> int:
        """Minutes offset from sunrise/sunset (positive = after, negative = before)."""
        ...

    @sunDelta.setter
    def sunDelta(self, value: int) -> None: ...

    @property
    def randomizeBy(self) -> int:
        """Maximum random offset in minutes applied to the trigger time."""
        ...

    @randomizeBy.setter
    def randomizeBy(self, value: int) -> None: ...

    @property
    def autoDelete(self) -> bool:
        """True if the schedule is automatically deleted after it fires."""
        ...

    @autoDelete.setter
    def autoDelete(self, value: bool) -> None: ...

    @property
    def absoluteTime(self) -> datetime.time | None:
        """Absolute time of day for the schedule (when timeType is Absolute)."""
        ...

    @absoluteTime.setter
    def absoluteTime(self, value: datetime.time) -> None: ...

    @property
    def absoluteDate(self) -> datetime.date | None:
        """Absolute date for the schedule (when dateType is Absolute)."""
        ...

    @absoluteDate.setter
    def absoluteDate(self, value: datetime.date) -> None: ...

    @property
    def absoluteDateTime(self) -> datetime.datetime | None:
        """Combined absolute date and time for the schedule."""
        ...

    @property
    def nextExecution(self) -> datetime.datetime | None:
        """Datetime of the next scheduled execution, or None."""
        ...

    def refreshFromServer(self, waitUntilServerIdle: bool = False) -> None:
        """Refresh all schedule properties from the server."""
        ...

    def replaceOnServer(self) -> None:
        """Push local changes of the schedule to the server."""
        ...

    def replacePluginPropsOnServer(self, newProps: dict) -> None:
        """Replace the entire pluginProps dict on the server."""
        ...

    def replaceSharedPropsOnServer(self, newProps: dict) -> None:
        """Replace the shared props dict on the server."""
        ...

    def __iter__(self) -> Iterator[tuple[str, Any]]:
        """Yields (key, value) pairs so dict(schedule) works. Patched in by utils.py."""
        ...


class EventScheduleCmds:
    """
    Command interface for schedule operations (``indigo.schedule``).
    Defined in CEventSchedule_pyglue.cpp.
    """

    def create(
        self,
        name: str = "",
        description: str = "",
        folder: ElemKey | None = None,
    ) -> Schedule:
        """Add a new schedule to the Indigo Server."""
        ...

    def duplicate(self, elem: ElemKey, duplicateName: str = "") -> Schedule:
        """Duplicate an existing schedule."""
        ...

    def delete(self, elem: ElemKey) -> None:
        """Delete a schedule from the Indigo Server."""
        ...

    def getDependencies(self, elem: ElemKey | List | Tuple) -> Any:
        """Return all element dependencies for the given schedule(s)."""
        ...

    def moveToFolder(self, elem: ElemKey, value: ElemKey) -> None:
        """Move a schedule to a different folder."""
        ...

    def displayInRemoteUI(self, elem: ElemKey, value: bool) -> None:
        """Change a schedule's remote UI display visibility."""
        ...

    def enable(self, elem: ElemKey, value: bool, delay: int = 0, duration: int = 0) -> None:
        """Enable or disable a schedule with optional delay and duration (in seconds)."""
        ...

    def execute(
        self,
        elem: ElemKey,
        schedule_data: Dict | dict | None = None,
    ) -> None:
        """
        Execute all actions in a schedule.
        schedule_data is an optional dict passed through the pipeline.
        """
        ...

    def removeDelayedActions(self, elem: ElemKey) -> None:
        """Remove all pending delayed actions started by this schedule."""
        ...


# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# Action group
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

class ActionGroup(BaseElem):
    """
    An Indigo action group.

    Exposed in Python as ``indigo.ActionGroup``.
    Properties defined in CActionGroup_pyglue.cpp.
    """

    @property
    def folderId(self) -> int:
        """ID of the folder containing this action group (0 = root)."""
        ...

    def refreshFromServer(self, waitUntilServerIdle: bool = False) -> None:
        """Refresh all action group properties from the server."""
        ...

    def replaceOnServer(self) -> None:
        """Push local changes of the action group to the server."""
        ...

    def replacePluginPropsOnServer(self, newProps: dict) -> None:
        """Replace the entire pluginProps dict on the server."""
        ...

    def replaceSharedPropsOnServer(self, newProps: dict) -> None:
        """Replace the shared props dict on the server."""
        ...

    def __iter__(self) -> Iterator[tuple[str, Any]]:
        """Yields (key, value) pairs so dict(action_group) works. Patched in by utils.py."""
        ...


class ActionGroupCmds:
    """
    Command interface for action group operations (``indigo.actionGroup``).
    Defined in CActionGroup_pyglue.cpp.
    """

    def create(
        self,
        name: str = "",
        description: str = "",
        folder: ElemKey | None = None,
    ) -> ActionGroup:
        """Add a new action group to the Indigo Server."""
        ...

    def duplicate(self, elem: ElemKey, duplicateName: str = "") -> ActionGroup:
        """Duplicate an existing action group."""
        ...

    def delete(self, elem: ElemKey) -> None:
        """Delete an action group from the Indigo Server."""
        ...

    def getDependencies(self, elem: ElemKey | List | Tuple) -> Any:
        """Return all element dependencies for the given action group(s)."""
        ...

    def moveToFolder(self, elem: ElemKey, value: ElemKey) -> None:
        """Move an action group to a different folder."""
        ...

    def displayInRemoteUI(self, elem: ElemKey, value: bool) -> None:
        """Change an action group's remote UI display visibility."""
        ...

    def execute(
        self,
        elem: ElemKey,
        event_data: Dict | dict | None = None,
    ) -> None:
        """
        Execute all actions in an action group.
        event_data is an optional dict passed through the pipeline.
        """
        ...


# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# Control page
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

class ControlPage(BaseElem):
    """
    An Indigo control page.

    Exposed in Python as ``indigo.ControlPage``.
    Properties defined in CControlPage_pyglue.cpp.
    """

    @property
    def folderId(self) -> int:
        """ID of the folder containing this control page (0 = root)."""
        ...

    @property
    def hideTabBar(self) -> bool:
        """True if the tab bar is hidden in Indigo Touch."""
        ...

    @hideTabBar.setter
    def hideTabBar(self, value: bool) -> None: ...

    @property
    def backgroundImage(self) -> str:
        """Background image file name."""
        ...

    @backgroundImage.setter
    def backgroundImage(self, value: str) -> None: ...

    @property
    def backgroundColor(self) -> str:
        """Background color as a space-delimited hex string."""
        ...

    @property
    def width(self) -> int:
        """Width of the control page in pixels."""
        ...

    @property
    def height(self) -> int:
        """Height of the control page in pixels."""
        ...

    def refreshFromServer(self, waitUntilServerIdle: bool = False) -> None:
        """Refresh all control page properties from the server."""
        ...

    def replaceOnServer(self) -> None:
        """Push local changes of the control page to the server."""
        ...

    def replacePluginPropsOnServer(self, newProps: dict) -> None:
        """Replace the entire pluginProps dict on the server."""
        ...

    def replaceSharedPropsOnServer(self, newProps: dict) -> None:
        """Replace the shared props dict on the server."""
        ...

    def __iter__(self) -> Iterator[tuple[str, Any]]:
        """Yields (key, value) pairs so dict(page) works. Patched in by utils.py."""
        ...


class ControlPageCmds:
    """
    Command interface for control page operations (``indigo.controlPage``).
    Defined in CControlPage_pyglue.cpp.
    """

    def create(
        self,
        name: str = "",
        description: str = "",
        folder: ElemKey | None = None,
    ) -> ControlPage:
        """Add a new control page to the Indigo Server."""
        ...

    def duplicate(self, elem: ElemKey, duplicateName: str = "") -> ControlPage:
        """Duplicate an existing control page."""
        ...

    def delete(self, elem: ElemKey) -> None:
        """Delete a control page from the Indigo Server."""
        ...

    def getDependencies(self, elem: ElemKey | List | Tuple) -> Any:
        """Return all element dependencies for the given control page(s)."""
        ...

    def moveToFolder(self, elem: ElemKey, value: ElemKey) -> None:
        """Move a control page to a different folder."""
        ...

    def displayInRemoteUI(self, elem: ElemKey, value: bool) -> None:
        """Change a control page's remote UI display visibility."""
        ...


# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# Action classes (passed to plugin action callbacks)
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

class BaseAction:
    """
    Base class for all Indigo action objects passed to plugin callbacks.
    Defined in CActionBase_pyglue.cpp.
    """

    @property
    def configured(self) -> bool:
        """True if the action has been fully configured."""
        ...

    @configured.setter
    def configured(self, value: bool) -> None:
        """Owning plugin only: set the configured state directly on the local object,
        then call replaceOnServer() to persist."""
        ...

    @property
    def description(self) -> str:
        """Human-readable description of the action."""
        ...

    @property
    def delayAmount(self) -> int:
        """Delay in seconds before the action executes."""
        ...

    @property
    def replaceExisting(self) -> bool:
        """True if this action replaces any existing delayed action."""
        ...

    @property
    def textToSpeak(self) -> str:
        """Text to speak when the action executes (if applicable)."""
        ...


class PluginAction(BaseAction):
    """
    A plugin-defined action. Passed to executeAction() callbacks.
    Defined in CActionPlugin_pyglue.cpp.
    """

    @property
    def deviceId(self) -> int:
        """ID of the device associated with this action. Read-only (received object)."""
        ...

    @property
    def props(self) -> dict:
        """Plugin-specific properties for this action."""
        ...

    @property
    def pluginId(self) -> str:
        """ID of the plugin that owns this action. Read-only (received object)."""
        ...

    @property
    def pluginTypeId(self) -> str:
        """Plugin-defined action type ID string. Read-only (received object)."""
        ...


class UniversalAction(BaseAction):
    """A universal (built-in) action. Passed to executeAction() callbacks."""
    ...


class DeviceAction(BaseAction):
    """A device control action. Passed to executeAction() callbacks."""
    ...


class ThermostatAction(BaseAction):
    """A thermostat control action. Passed to executeAction() callbacks."""
    ...


class SensorAction(BaseAction):
    """A sensor control action. Passed to executeAction() callbacks."""
    ...


class SprinklerAction(BaseAction):
    """A sprinkler control action. Passed to executeAction() callbacks."""
    ...


class SpeedControlAction(BaseAction):
    """A speed control action. Passed to executeAction() callbacks."""
    ...


# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# Protocol interfaces
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

class InsteonCmd:
    """
    Represents an INSTEON command (incoming or outgoing).
    Defined in CInstnInterfaceCmd_pyglue.cpp.
    """

    @property
    def address(self) -> str:
        """INSTEON device address string (e.g. "AA.BB.CC")."""
        ...

    @property
    def cmdSuccess(self) -> bool:
        """True if the command completed successfully."""
        ...

    @property
    def cmdFunc(self) -> int:
        """INSTEON command function byte."""
        ...

    @property
    def cmdValue(self) -> int:
        """INSTEON command value byte."""
        ...

    @property
    def cmdScene(self) -> int:
        """INSTEON scene number (0 if not a scene command)."""
        ...

    @property
    def cmdBytes(self) -> bytes:
        """Raw command bytes."""
        ...

    @property
    def ackValue(self) -> int:
        """ACK value returned by device."""
        ...

    @property
    def replyBytes(self) -> bytes:
        """Raw reply bytes from device."""
        ...


class InsteonCmdInterface:
    """
    INSTEON protocol command interface (``indigo.insteon``).
    Defined in CInstnInterfaceCmd_pyglue.cpp.
    """

    def subscribeToIncoming(self) -> None:
        """Subscribe to incoming INSTEON commands. Calls insteonCmdIncoming() on plugin."""
        ...

    def subscribeToOutgoing(self) -> None:
        """Subscribe to outgoing INSTEON commands. Calls insteonCmdOutgoing() on plugin."""
        ...

    def sendSceneOn(self, sceneNum: int, suppressLogging: bool = False) -> None:
        """Send Scene On command."""
        ...

    def sendSceneOff(self, sceneNum: int, suppressLogging: bool = False) -> None:
        """Send Scene Off command."""
        ...

    def sendSceneFastOn(self, sceneNum: int, suppressLogging: bool = False) -> None:
        """Send Scene Fast On command."""
        ...

    def sendSceneFastOff(self, sceneNum: int, suppressLogging: bool = False) -> None:
        """Send Scene Fast Off command."""
        ...

    def sendSceneIncrease(self, sceneNum: int, suppressLogging: bool = False) -> None:
        """Send Scene Increase (brighten) command."""
        ...

    def sendSceneDecrease(self, sceneNum: int, suppressLogging: bool = False) -> None:
        """Send Scene Decrease (dim) command."""
        ...

    def sendStatusRequest(self, deviceId: ElemKey, suppressLogging: bool = False) -> None:
        """Send status request to an INSTEON device."""
        ...

    def sendRaw(
        self,
        deviceId: ElemKey,
        cmd1: int,
        cmd2: int = 0,
        suppressLogging: bool = False,
    ) -> None:
        """Send a raw INSTEON standard-length command."""
        ...

    def sendRawExtended(
        self,
        deviceId: ElemKey,
        cmd1: int,
        cmd2: int = 0,
        extendedData: bytes | None = None,
        suppressLogging: bool = False,
    ) -> None:
        """Send a raw INSTEON extended-length command."""
        ...

    def sendRemotePeek(
        self,
        deviceId: ElemKey,
        address: int,
        suppressLogging: bool = False,
    ) -> None:
        """Send remote peek command to read INSTEON device memory."""
        ...

    def sendRemotePoke(
        self,
        deviceId: ElemKey,
        address: int,
        value: int,
        suppressLogging: bool = False,
    ) -> None:
        """Send remote poke command to write INSTEON device memory."""
        ...


class X10Cmd:
    """
    Represents an X10 command (incoming or outgoing).
    Defined in CX10InterfaceCmd_pyglue.cpp.
    """

    @property
    def address(self) -> str:
        """X10 device address string."""
        ...

    @property
    def cmdSuccess(self) -> bool:
        """True if the command succeeded."""
        ...

    @property
    def cmdType(self) -> int:
        """X10 command type."""
        ...

    @property
    def x10Func(self) -> int:
        """X10 function code."""
        ...

    @property
    def x10DimBrightenVal(self) -> int:
        """Dim/brighten amount value."""
        ...

    @property
    def x10PresetVal(self) -> int:
        """Preset dim value."""
        ...

    @property
    def x10ExtendedData(self) -> bytes:
        """Extended data bytes."""
        ...

    @property
    def avFunc(self) -> int:
        """AV function code."""
        ...

    @property
    def secFunc(self) -> int:
        """Security function code."""
        ...

    @property
    def secCodeId(self) -> int:
        """Security code ID."""
        ...


class X10CmdInterface:
    """
    X10 protocol command interface (``indigo.x10``).
    Defined in CX10InterfaceCmd_pyglue.cpp.
    """

    def subscribeToIncoming(self) -> None:
        """Subscribe to incoming X10 commands. Calls x10CmdIncoming() on plugin."""
        ...

    def subscribeToOutgoing(self) -> None:
        """Subscribe to outgoing X10 commands. Calls x10CmdOutgoing() on plugin."""
        ...

    def sendOn(self, deviceId: ElemKey, suppressLogging: bool = False) -> None:
        """Send X10 On command."""
        ...

    def sendOff(self, deviceId: ElemKey, suppressLogging: bool = False) -> None:
        """Send X10 Off command."""
        ...

    def sendBrighten(
        self, deviceId: ElemKey, brightenBy: int, suppressLogging: bool = False
    ) -> None:
        """Send X10 Brighten command."""
        ...

    def sendDim(
        self, deviceId: ElemKey, dimBy: int, suppressLogging: bool = False
    ) -> None:
        """Send X10 Dim command."""
        ...

    def sendPreset(
        self, deviceId: ElemKey, presetVal: int, suppressLogging: bool = False
    ) -> None:
        """Send X10 Preset Dim command."""
        ...

    def sendExtended(
        self,
        deviceId: ElemKey,
        extendedData: bytes,
        suppressLogging: bool = False,
    ) -> None:
        """Send X10 Extended command."""
        ...

    def sendStatusRequest(self, deviceId: ElemKey, suppressLogging: bool = False) -> None:
        """Send X10 status request."""
        ...

    def sendAllUnitsOff(self, houseCode: str, suppressLogging: bool = False) -> None:
        """Send X10 All Units Off command for the given house code."""
        ...

    def sendAllUnitsOn(self, houseCode: str, suppressLogging: bool = False) -> None:
        """Send X10 All Units On command for the given house code."""
        ...

    def sendAllLightsOff(self, houseCode: str, suppressLogging: bool = False) -> None:
        """Send X10 All Lights Off command for the given house code."""
        ...

    def sendAllLightsOn(self, houseCode: str, suppressLogging: bool = False) -> None:
        """Send X10 All Lights On command for the given house code."""
        ...


class ZWaveInterface:
    """
    Z-Wave protocol command interface (``indigo.zwave``).
    Defined in CZWaveInterface_pyglue.cpp.
    """

    def subscribeToIncoming(self) -> None:
        """Subscribe to incoming Z-Wave commands. Calls zwaveCmdIncoming() on plugin."""
        ...

    def subscribeToOutgoing(self) -> None:
        """Subscribe to outgoing Z-Wave commands. Calls zwaveCmdOutgoing() on plugin."""
        ...

    def isEnabled(self) -> bool:
        """Return True if the Z-Wave interface is enabled."""
        ...

    def sendConfigParm(
        self,
        deviceId: ElemKey,
        paramIndex: int,
        paramSize: int,
        paramValue: int,
        suppressLogging: bool = False,
    ) -> None:
        """Send a Z-Wave configuration parameter to a device."""
        ...

    def sendRaw(
        self,
        deviceId: ElemKey,
        cmdClass: int,
        cmd: int,
        cmdBytes: bytes | None = None,
        suppressLogging: bool = False,
    ) -> None:
        """Send a raw Z-Wave command to a device."""
        ...

    def enterInclusionMode(self, suppressLogging: bool = False) -> None:
        """Put the Z-Wave controller into inclusion mode."""
        ...

    def enterExclusionMode(self, suppressLogging: bool = False) -> None:
        """Put the Z-Wave controller into exclusion mode."""
        ...

    def exitInclusionExclusionMode(self, suppressLogging: bool = False) -> None:
        """Exit inclusion/exclusion mode."""
        ...

    def startNetworkOptimize(self, suppressLogging: bool = False) -> None:
        """Start Z-Wave network optimization."""
        ...

    def stopNetworkOptimize(self, suppressLogging: bool = False) -> None:
        """Stop Z-Wave network optimization."""
        ...


# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# Plugin info class
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

class PluginInfo:
    """
    Metadata about an installed Indigo plugin.
    Returned by indigo.server.getPlugin() and indigo.server.getPluginList().
    Defined in CPlugin_pyglue.cpp.
    """

    @property
    def pluginId(self) -> str:
        """Unique plugin ID string."""
        ...

    @property
    def pluginDisplayName(self) -> str:
        """Human-readable plugin name."""
        ...

    @property
    def pluginFolderPath(self) -> str:
        """POSIX path to the plugin bundle."""
        ...

    @property
    def pluginVersion(self) -> str:
        """Plugin version string."""
        ...

    @property
    def pluginBundleId(self) -> str:
        """Bundle ID string of the plugin."""
        ...

    @property
    def serverApiVersion(self) -> str:
        """Minimum required server API version string."""
        ...

    @property
    def apiVersion(self) -> str:
        """Plugin API version string."""
        ...

    @property
    def priority(self) -> int:
        """Plugin load priority."""
        ...

    @property
    def debuggingEnabled(self) -> bool:
        """True if debugging is enabled for the plugin."""
        ...

    @property
    def isLoaded(self) -> bool:
        """True if the plugin process is loaded."""
        ...

    @property
    def storeDescription(self) -> str:
        """Plugin Store description."""
        ...

    @property
    def storeReleaseNotesURL(self) -> str:
        """URL to plugin release notes."""
        ...

    @property
    def storeDownloadURL(self) -> str:
        """URL to download the plugin."""
        ...

    @property
    def storeChangelogURL(self) -> str:
        """URL to the plugin changelog."""
        ...

    @property
    def updateAvailable(self) -> bool:
        """True if a plugin update is available in the Plugin Store."""
        ...

    @property
    def latestVersion(self) -> str:
        """Latest version string available in the Plugin Store."""
        ...

    def isInstalled(self) -> bool:
        """Return True if the plugin is installed."""
        ...

    def isEnabled(self) -> bool:
        """Return True if the plugin is enabled."""
        ...

    def isRunning(self) -> bool:
        """Return True if the plugin process is currently running."""
        ...

    def restart(self, waitUntilDone: bool = True) -> None:
        """Restart the plugin process."""
        ...

    def restartAndDebug(self, waitUntilDone: bool = True) -> None:
        """Restart the plugin process in debug mode."""
        ...

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
        ...


# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# Callback handler
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

class CallbackCompleteHandler:
    """
    Passed to plugin callback methods that use the broadcastToSubscribers /
    returnResult pattern. Defined in CHandlerCompleteData_pyglue.cpp.
    """

    @property
    def messageName(self) -> str:
        """Name of the broadcast message."""
        ...

    @property
    def replyTarget(self) -> str:
        """Identifier of the reply target."""
        ...

    def returnResult(self, result: Any) -> None:
        """Return a result to the broadcast subscriber."""
        ...

    def returnException(self, exception: Exception) -> None:
        """Return an exception to the broadcast subscriber."""
        ...


# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# Server interface (indigo.server)
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

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
    def broadcastToSubscribers(self, messageName: str, props: Dict | dict | None = None) -> None:
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


# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# Host interface (indigo.host) - private/internal
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

class HostInfo:
    """
    Internal host interface (``indigo.host``). Used by the plugin host process.
    Not intended for use in plugin code.
    """

    debugMode: int
    """Current plugin debug mode (class-level static property). Compare to kPluginDebugMode_* constants."""

    @property
    def version(self) -> str:
        """Plugin host version string."""
        ...

    @property
    def resourcesFolderPath(self) -> str:
        """Path to the plugin host resources folder."""
        ...

    def browserOpen(self, url: str) -> None:
        """Open *url* in the system default browser."""
        ...


# ==============================================================================
# END SECTION: C++ Boost.Python bindings
# ==============================================================================

# ==============================================================================
# BEGIN SECTION: plugin_base.py
# Source: Py3 Libraries/plugin_base.py
# To update: read plugin_base.py and regenerate only this section.
# ==============================================================================

class IndigoLogger(logging.Logger):
    """
    Logger subclass registered via logging.setLoggerClass() in plugin_base.py.
    Adds the ``threaddebug`` method (level 5, below DEBUG) used by plugins.
    ``self.logger`` on PluginBase instances is always an IndigoLogger.
    """
    def threaddebug(self, msg: object, *args: object, **kwargs: object) -> None:
        """Log at level THREADDEBUG (5), below DEBUG. No-op if level is not enabled."""
        ...


class PluginBase:
    """
    Base class for all Indigo plugins. Plugin developers subclass this in plugin.py.
    Defined in Py3 Libraries/plugin_base.py and injected into the indigo namespace.

    Lifecycle methods are called by IndigoPluginHost3 at appropriate times.
    Override only the methods your plugin needs.
    """

    # ---- Nested exception classes ----
    class InterfaceError(Exception):
        """Raised when a hardware interface operation fails."""
        ...

    class PluginDisabled(Exception):
        """Raised when an operation requires a plugin that is installed but disabled."""
        ...

    class PluginNotInstalled(Exception):
        """Raised when an operation requires a plugin that is not installed."""
        ...

    class InvalidAction(Exception):
        """Raised when an action type ID is not valid for the target plugin."""
        ...

    class InvalidParameter(Exception):
        """Raised when a parameter passed to a plugin method is invalid."""
        ...

    class StopThread(Exception):
        """Raised internally to signal the plugin's concurrent thread to stop."""
        ...

    # ---- Instance attributes set during __init__ ----
    plugin_id: str
    """Plugin bundle identifier (e.g. 'com.example.myplugin')."""

    plugin_display_name: str
    """Human-readable plugin name as shown in the Indigo UI."""

    plugin_version: str
    """Plugin version string from Info.plist."""

    plugin_prefs: dict
    """Plugin preferences dict, automatically loaded and saved by the server."""

    pluginPrefs: dict
    """Camel-case alias for plugin_prefs (prefer plugin_prefs in new code)."""

    plugin_folder_path: str
    """Absolute path to the plugin bundle folder."""

    plugin_support_url: str
    """Support URL for the plugin (from Info.plist)."""

    logger: IndigoLogger
    """Standard Python logger for this plugin. Use instead of debugLog()/errorLog()."""

    indigo_log_handler: logging.Handler
    """Logging handler that writes to the Indigo log at INFO level and above."""

    plugin_file_handler: logging.Handler
    """Logging handler that writes all levels to the plugin's log file."""

    stop_thread: bool
    """Set to True by the framework to signal runConcurrentThread() to exit."""

    @property
    def debug(self) -> bool:
        """True when debug logging is enabled for this plugin."""
        ...

    @debug.setter
    def debug(self, value: bool) -> None: ...

    def __getattr__(self, name: str) -> Any:
        """Allows subclasses to define arbitrary instance attributes without type errors."""
        ...

    def __init__(
        self, pluginId: str, pluginDisplayName: str, pluginVersion: str, pluginPrefs: dict, **kwargs: Any
    ) -> None:
        """Initialize the plugin. Call super().__init__() in your subclass."""
        ...

    # ---- Plugin lifecycle ----
    def startup(self) -> None:
        """Called once when the plugin is loaded. Override to perform initialization."""
        ...

    def shutdown(self) -> None:
        """Called once when the plugin is unloaded. Override to perform cleanup."""
        ...

    def runConcurrentThread(self) -> None:
        """
        Override to run a continuous background thread.
        Use self.sleep() to wait and check self.stopThread for the stop signal.
        """
        ...

    def stopConcurrentThread(self) -> None:
        """
        Called when the plugin should stop its concurrent thread.
        The default implementation sets self.stopThread = True.
        """
        ...

    def update(self) -> None:
        """
        Called periodically by the concurrent thread infrastructure.
        Override in place of runConcurrentThread() for simpler polling loops.
        """
        ...

    def sleep(self, seconds: float) -> None:
        """Sleep for the specified number of seconds. Raises StopThread if stopping."""
        ...

    # ---- Plugin preferences UI ----
    def getPrefsConfigUiValues(self) -> Tuple[Dict, Dict]:
        """Return (valuesDict, errorsDict) for the plugin preferences UI."""
        ...

    def validatePrefsConfigUi(self, valuesDict: dict) -> Tuple[bool, Dict, Dict]:
        """Validate plugin preferences UI values."""
        ...

    def closedPrefsConfigUi(self, valuesDict: dict, userCancelled: bool) -> None:
        """Called after the plugin preferences dialog is closed."""
        ...

    # ---- Device lifecycle ----
    def deviceStartComm(self, device: Device) -> None:
        """Called when a device is started (enabled and communication begins)."""
        ...

    def deviceStopComm(self, device: Device) -> None:
        """Called when a device is stopped."""
        ...

    def deviceCreated(self, device: Device) -> None:
        """Called when a new device of this plugin's type is created."""
        ...

    def deviceDeleted(self, device: Device) -> None:
        """Called when a device of this plugin's type is deleted."""
        ...

    def deviceUpdated(self, origDev: Device, newDev: Device) -> None:
        """Called when a device's properties are updated on the server."""
        ...

    # ---- Device UI ----
    def getDeviceConfigUiValues(
        self, pluginProps: dict, typeId: str, devId: int
    ) -> Tuple[Dict, Dict]:
        """Return (valuesDict, errorsDict) for the device config UI."""
        ...

    def validateDeviceConfigUi(
        self, valuesDict: dict, typeId: str, devId: int
    ) -> Tuple[bool, Dict, Dict]:
        """Validate device config UI values."""
        ...

    def closedDeviceConfigUi(
        self, valuesDict: dict, userCancelled: bool, typeId: str, devId: int
    ) -> None:
        """Called after the device config dialog is closed."""
        ...

    def getDeviceStateList(self, device: Device) -> list[Dict]:
        """Return the list of state definitions for a dynamic device."""
        ...

    def getDeviceDisplayStateId(self, device: Device) -> str:
        """Return the state key ID to use as the primary display state."""
        ...

    # ---- Action execution ----
    def executeAction(
        self,
        pluginAction: PluginAction,
        device: Device,
        callerWaitingForResult: bool,
    ) -> None:
        """Execute a plugin-defined action."""
        ...

    # ---- Action UI ----
    def getActionConfigUiValues(
        self, pluginProps: dict, typeId: str, devId: int
    ) -> Tuple[Dict, Dict]:
        """Return (valuesDict, errorsDict) for the action config UI."""
        ...

    def validateActionConfigUi(
        self, valuesDict: dict, typeId: str, devId: int
    ) -> Tuple[bool, Dict, Dict]:
        """Validate action config UI values."""
        ...

    def closedActionConfigUi(
        self, valuesDict: dict, userCancelled: bool, typeId: str, devId: int
    ) -> None:
        """Called after the action config dialog is closed."""
        ...

    # ---- Trigger lifecycle ----
    def triggerCreated(self, trigger: Trigger) -> None:
        """Called when a new trigger of this plugin's type is created."""
        ...

    def triggerDeleted(self, trigger: Trigger) -> None:
        """Called when a trigger of this plugin's type is deleted."""
        ...

    def triggerUpdated(self, origTrigger: Trigger, newTrigger: Trigger) -> None:
        """Called when a trigger is updated."""
        ...

    def triggerStartProcessing(self, trigger: Trigger) -> None:
        """Called when a trigger is enabled and starts processing."""
        ...

    def triggerStopProcessing(self, trigger: Trigger) -> None:
        """Called when a trigger is disabled and stops processing."""
        ...

    def didTriggerProcessingPropertyChange(
        self, origTrigger: Trigger, newTrigger: Trigger
    ) -> bool:
        """Return True if a property change requires stopping/restarting trigger processing."""
        ...

    # ---- Trigger UI ----
    def getTriggerConfigUiValues(
        self, pluginProps: dict, typeId: str, triggerId: int
    ) -> Tuple[Dict, Dict]:
        """Return (valuesDict, errorsDict) for the trigger config UI."""
        ...

    def validateTriggerConfigUi(
        self, valuesDict: dict, typeId: str, triggerId: int
    ) -> Tuple[bool, Dict, Dict]:
        """Validate trigger config UI values."""
        ...

    def closedTriggerConfigUi(
        self, valuesDict: dict, userCancelled: bool, typeId: str, triggerId: int
    ) -> None:
        """Called after the trigger config dialog is closed."""
        ...

    # ---- Action group / control page / schedule / variable callbacks ----
    def actionGroupCreated(self, actionGroup: ActionGroup) -> None: ...
    def actionGroupDeleted(self, actionGroup: ActionGroup) -> None: ...
    def actionGroupUpdated(
        self, origActionGroup: ActionGroup, newActionGroup: ActionGroup
    ) -> None: ...

    def controlPageCreated(self, controlPage: ControlPage) -> None: ...
    def controlPageDeleted(self, controlPage: ControlPage) -> None: ...
    def controlPageUpdated(
        self, origControlPage: ControlPage, newControlPage: ControlPage
    ) -> None: ...

    def scheduleCreated(self, schedule: Schedule) -> None: ...
    def scheduleDeleted(self, schedule: Schedule) -> None: ...
    def scheduleUpdated(self, origSchedule: Schedule, newSchedule: Schedule) -> None: ...

    def variableCreated(self, variable: Variable) -> None: ...
    def variableDeleted(self, variable: Variable) -> None: ...
    def variableUpdated(self, origVariable: Variable, newVariable: Variable) -> None: ...

    # ---- Protocol callbacks ----
    def insteonCmdIncoming(self, origCmd: InsteonCmd) -> None:
        """Called for each incoming INSTEON command when subscribed."""
        ...

    def insteonCmdOutgoing(
        self, origCmd: InsteonCmd, newCmd: InsteonCmd, cmdSuccess: bool
    ) -> None:
        """Called for each outgoing INSTEON command when subscribed."""
        ...

    def x10CmdIncoming(self, origCmd: X10Cmd) -> None:
        """Called for each incoming X10 command when subscribed."""
        ...

    def x10CmdOutgoing(self, origCmd: X10Cmd, newCmd: X10Cmd, cmdSuccess: bool) -> None:
        """Called for each outgoing X10 command when subscribed."""
        ...

    # ---- Server broadcast ----
    def broadcastReceived(self, messageName: str) -> None:
        """Called when a subscribed broadcast message is received."""
        ...

    def logBroadcast(self, message: str) -> None:
        """Called for each event log entry when subscribed via subscribeToLogBroadcasts()."""
        ...

    # ---- Dynamic UI menu callbacks ----
    def getMenuActionConfigUiValues(self, menuId: str) -> Tuple[Dict, Dict]:
        """Return (valuesDict, errorsDict) for a menu action UI."""
        ...

    def validateMenuActionConfigUi(
        self, valuesDict: dict, menuId: str
    ) -> Tuple[bool, Dict, Dict]:
        """Validate menu action UI values."""
        ...

    def closedMenuActionConfigUi(
        self, valuesDict: dict, userCancelled: bool, menuId: str
    ) -> None:
        """Called after a menu action config dialog is closed."""
        ...

    # ---- Dynamic UI list/field callbacks ----
    def getDeviceGroupList(
        self, filter: str, valuesDict: dict, typeId: str, targetId: int
    ) -> list[Tuple[str, str]]:
        """Return a list of (value, label) tuples for a dynamicGroupList UI control."""
        ...

    def getDeviceList(
        self, filter: str, valuesDict: dict, typeId: str, targetId: int
    ) -> list[Tuple[str, str]]:
        """Return a list of (value, label) tuples for a dynamicList UI control."""
        ...

    def menuChanged(self, valuesDict: dict, typeId: str, devId: int) -> dict:
        """Called when a menu/select UI control changes. Return updated valuesDict."""
        ...


# ==============================================================================
# END SECTION: plugin_base.py
# ==============================================================================

# ==============================================================================
# BEGIN SECTION: C++ Boost.Python bindings (module-level instances and constants)
# Source: source/Common Util/CPythonMgr.cpp, source/Common Db/*_pyglue.cpp
# To update: read CPythonMgr.cpp and regenerate only this section.
# ==============================================================================

# ---- Collections ----
devices: DeviceList
"""Dict-like collection of all Indigo devices, keyed by device ID or name."""

variables: VariableList
"""Dict-like collection of all Indigo variables, keyed by variable ID or name."""

triggers: TriggerList
"""Dict-like collection of all Indigo triggers, keyed by trigger ID or name."""

schedules: ScheduleList
"""Dict-like collection of all Indigo schedules, keyed by schedule ID or name."""

actionGroups: ActionGroupList
"""Dict-like collection of all Indigo action groups, keyed by ID or name."""

controlPages: ControlPageList
"""Dict-like collection of all Indigo control pages, keyed by ID or name."""

# ---- Device command interfaces ----
device: DeviceCmds
"""General device command interface."""

relay: RelayDeviceCmds
"""Relay device command interface."""

dimmer: DimmerDeviceCmds
"""Dimmer device command interface."""

sensor: SensorDeviceCmds
"""Sensor device command interface."""

speedcontrol: SpeedControlDeviceCmds
"""Speed control device command interface."""

thermostat: ThermostatDeviceCmds
"""Thermostat device command interface."""

sprinkler: SprinklerDeviceCmds
"""Sprinkler device command interface."""

iodevice: MultiIODeviceCmds
"""Multi-I/O device command interface."""

# ---- Other command interfaces ----
variable: VariableCmds
"""Variable command interface."""

trigger: EventTriggerCmds
"""Trigger command interface."""

schedule: EventScheduleCmds
"""Schedule command interface."""

actionGroup: ActionGroupCmds
"""Action group command interface."""

controlPage: ControlPageCmds
"""Control page command interface."""

# ---- Protocol interfaces ----
insteon: InsteonCmdInterface
"""INSTEON protocol command interface."""

x10: X10CmdInterface
"""X10 protocol command interface."""

zwave: ZWaveInterface
"""Z-Wave protocol command interface."""

# ---- Server / host interfaces ----
server: ServerInfo
"""Indigo server properties and commands."""

host: HostInfo
"""Internal host interface (not for plugin use)."""

# ---- Active plugin instance ----
activePlugin: PluginBase
"""The currently running plugin instance. Set by IndigoPluginHost3 at startup."""

# ---- Debug / plugin mode constants ----
kPluginDebugMode_none: int
"""Plugin debug mode: no debugging."""

kPluginDebugMode_debugPdb: int
"""Plugin debug mode: use pdb debugger."""

kPluginDebugMode_debugPudb: int
"""Plugin debug mode: use pudb debugger."""

kPluginDebugMode_debugPyCharm: int
"""Plugin debug mode: use PyCharm remote debugger."""

# ==============================================================================
# END SECTION: C++ Boost.Python bindings (module-level instances and constants)
# ==============================================================================

# ==============================================================================
# BEGIN SECTION: indigo_base.py
# Source: Py3 Libraries/indigo_base.py
# To update: read indigo_base.py and regenerate only this section.
# ==============================================================================

def debugger() -> None:
    """
    Drop into the configured Python debugger (pdb, pudb, or PyCharm remote debugger)
    based on the current debug mode. No-op if debug mode is none.
    Defined in indigo_base.py.
    """
    ...

# ==============================================================================
# END SECTION: indigo_base.py
# ==============================================================================

# ==============================================================================
# BEGIN SECTION: C++ Boost.Python bindings (module-level functions)
# Source: source/Common Util/CPythonMgr.cpp
# To update: read CPythonMgr.cpp and regenerate only this section.
# ==============================================================================

def _resolvePluginFuncFromName(instance: Any, funcname: str) -> Any:
    """internal method."""
    ...


def rawServerCommand(name: str, args: Any = None) -> None:
    """
    Sends the raw named command to the server. Optional argument
    args can be: boolean, integer, float, string, or dict.
    Only use if directed by developer support.
    """
    ...


def rawServerRequest(name: str, args: Any = None) -> Any:
    """
    Sends the raw named request to the server. Optional argument
    args can be: boolean, integer, float, string, or dict.
    Only use if directed by developer support.
    """
    ...

# ==============================================================================
# END SECTION: C++ Boost.Python bindings (module-level functions)
# ==============================================================================
