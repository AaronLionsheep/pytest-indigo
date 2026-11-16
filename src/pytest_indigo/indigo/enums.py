class kProtocol(int):
    """Device protocol type enumeration (indigo.kProtocol.*)."""

    Insteon: "kProtocol"
    X10: "kProtocol"
    ZWave: "kProtocol"
    Plugin: "kProtocol"


class kAllDeviceSel(int):
    """All-device selector enumeration (indigo.kAllDeviceSel.*)."""

    All: "kAllDeviceSel"
    Insteon: "kAllDeviceSel"
    ZWave: "kAllDeviceSel"
    X10: "kAllDeviceSel"
    HouseCodeA: "kAllDeviceSel"
    HouseCodeB: "kAllDeviceSel"
    HouseCodeC: "kAllDeviceSel"
    HouseCodeD: "kAllDeviceSel"
    HouseCodeE: "kAllDeviceSel"
    HouseCodeF: "kAllDeviceSel"
    HouseCodeG: "kAllDeviceSel"
    HouseCodeH: "kAllDeviceSel"
    HouseCodeI: "kAllDeviceSel"
    HouseCodeJ: "kAllDeviceSel"
    HouseCodeK: "kAllDeviceSel"
    HouseCodeL: "kAllDeviceSel"
    HouseCodeM: "kAllDeviceSel"
    HouseCodeN: "kAllDeviceSel"
    HouseCodeO: "kAllDeviceSel"
    HouseCodeP: "kAllDeviceSel"


class kStateImageSel(int):
    """State image selector enumeration (indigo.kStateImageSel.*)."""

    Auto: "kStateImageSel"
    NoImage: "kStateImageSel"  # also accessible as kStateImageSel.None (Python keyword workaround)
    Error: "kStateImageSel"
    Custom: "kStateImageSel"
    PowerOff: "kStateImageSel"
    PowerOn: "kStateImageSel"
    Unlocked: "kStateImageSel"
    Locked: "kStateImageSel"
    Closed: "kStateImageSel"
    Opened: "kStateImageSel"
    DimmerOff: "kStateImageSel"
    DimmerOn: "kStateImageSel"
    FanOff: "kStateImageSel"
    FanLow: "kStateImageSel"
    FanMedium: "kStateImageSel"
    FanHigh: "kStateImageSel"
    SprinklerOff: "kStateImageSel"
    SprinklerOn: "kStateImageSel"
    HvacOff: "kStateImageSel"
    HvacCoolMode: "kStateImageSel"
    HvacHeatMode: "kStateImageSel"
    HvacAutoMode: "kStateImageSel"
    HvacFanOn: "kStateImageSel"
    HvacCooling: "kStateImageSel"
    HvacHeating: "kStateImageSel"
    SensorOff: "kStateImageSel"
    SensorOn: "kStateImageSel"
    SensorTripped: "kStateImageSel"
    EnergyMeterOff: "kStateImageSel"
    EnergyMeterOn: "kStateImageSel"
    LightSensor: "kStateImageSel"
    LightSensorOn: "kStateImageSel"
    MotionSensor: "kStateImageSel"
    MotionSensorTripped: "kStateImageSel"
    DoorSensorClosed: "kStateImageSel"
    DoorSensorOpened: "kStateImageSel"
    WindowSensorClosed: "kStateImageSel"
    WindowSensorOpened: "kStateImageSel"
    TemperatureSensor: "kStateImageSel"
    TemperatureSensorOn: "kStateImageSel"
    HumiditySensor: "kStateImageSel"
    HumiditySensorOn: "kStateImageSel"
    HumidifierOff: "kStateImageSel"
    HumidifierOn: "kStateImageSel"
    DehumidifierOff: "kStateImageSel"
    DehumidifierOn: "kStateImageSel"
    WindSpeedSensor: "kStateImageSel"
    WindSpeedSensorLow: "kStateImageSel"
    WindSpeedSensorMedium: "kStateImageSel"
    WindSpeedSensorHigh: "kStateImageSel"
    WindDirectionSensor: "kStateImageSel"
    WindDirectionSensorNorth: "kStateImageSel"
    WindDirectionSensorNorthEast: "kStateImageSel"
    WindDirectionSensorEast: "kStateImageSel"
    WindDirectionSensorSouthEast: "kStateImageSel"
    WindDirectionSensorSouth: "kStateImageSel"
    WindDirectionSensorSouthWest: "kStateImageSel"
    WindDirectionSensorWest: "kStateImageSel"
    WindDirectionSensorNorthWest: "kStateImageSel"
    BatteryCharger: "kStateImageSel"
    BatteryChargerOn: "kStateImageSel"
    BatteryLevel: "kStateImageSel"
    BatteryLevelLow: "kStateImageSel"
    BatteryLevel25: "kStateImageSel"
    BatteryLevel50: "kStateImageSel"
    BatteryLevel75: "kStateImageSel"
    BatteryLevelHigh: "kStateImageSel"
    TimerOff: "kStateImageSel"
    TimerOn: "kStateImageSel"
    AvStopped: "kStateImageSel"
    AvPaused: "kStateImageSel"
    AvPlaying: "kStateImageSel"


class kHvacMode(int):
    """HVAC operating mode enumeration (indigo.kHvacMode.*)."""

    Off: "kHvacMode"
    Heat: "kHvacMode"
    Cool: "kHvacMode"
    HeatCool: "kHvacMode"
    ProgramHeat: "kHvacMode"
    ProgramCool: "kHvacMode"
    ProgramHeatCool: "kHvacMode"


class kFanMode(int):
    """Fan mode enumeration (indigo.kFanMode.*)."""

    Auto: "kFanMode"
    AlwaysOn: "kFanMode"


class kDateType(int):
    """Schedule date type enumeration (indigo.kDateType.*)."""

    Absolute: "kDateType"
    EveryDay: "kDateType"
    DaysOfWeek: "kDateType"
    DaysOfMonth: "kDateType"
    DaysOfMonthInterval: "kDateType"


class kTimeType(int):
    """Schedule time type enumeration (indigo.kTimeType.*)."""

    Absolute: "kTimeType"
    Countdown: "kTimeType"
    Sunrise: "kTimeType"
    Sunset: "kTimeType"


class kDeviceSourceType(int):
    """Trigger device source type enumeration (indigo.kDeviceSourceType.*)."""

    NoDevice: "kDeviceSourceType"
    DeviceId: "kDeviceSourceType"
    AnyDevice: "kDeviceSourceType"
    RawAddress: "kDeviceSourceType"


class kInterface(int):
    """Network interface enumeration (indigo.kInterface.*)."""

    All: "kInterface"
    InsteonX10: "kInterface"
    X10RF: "kInterface"
    Plugin: "kInterface"


class kTriggerKeyType(int):
    """Trigger state-change key type enumeration (indigo.kTriggerKeyType.*)."""

    Label: "kTriggerKeyType"
    BoolTrueFalse: "kTriggerKeyType"
    BoolOnOff: "kTriggerKeyType"
    BoolYesNo: "kTriggerKeyType"
    BoolOneZero: "kTriggerKeyType"
    Number: "kTriggerKeyType"
    Integer: "kTriggerKeyType"
    Real: "kTriggerKeyType"
    String: "kTriggerKeyType"
    Compound: "kTriggerKeyType"
    Enumeration: "kTriggerKeyType"


class kStateChange(int):
    """Device state change type enumeration (indigo.kStateChange.*)."""

    BecomesTrue: "kStateChange"
    BecomesFalse: "kStateChange"
    BecomesEqual: "kStateChange"
    BecomesNotEqual: "kStateChange"
    BecomesGreaterThan: "kStateChange"
    BecomesLessThan: "kStateChange"
    Changes: "kStateChange"


class kVarChange(int):
    """Variable change type enumeration (indigo.kVarChange.*)."""

    BecomesTrue: "kVarChange"
    BecomesFalse: "kVarChange"
    BecomesEqual: "kVarChange"
    BecomesNotEqual: "kVarChange"
    BecomesGreaterThan: "kVarChange"
    BecomesLessThan: "kVarChange"
    Changes: "kVarChange"


class kLicenseStatus(int):
    """License status enumeration (indigo.kLicenseStatus.*)."""

    Unknown: "kLicenseStatus"
    ActiveTrial: "kLicenseStatus"
    ActiveSubscription: "kLicenseStatus"
    ExpiredSubscription: "kLicenseStatus"


class kAcctCommResult(int):
    """Account communication result enumeration (indigo.kAcctCommResult.*)."""

    NoErr: "kAcctCommResult"
    Unknown: "kAcctCommResult"
    MiscErr: "kAcctCommResult"
    ConnectivityFailed: "kAcctCommResult"
    NeedCredentials: "kAcctCommResult"
    AuthenticationFailed: "kAcctCommResult"
    LoadFailed: "kAcctCommResult"


class kDeviceAction(int):
    """Device action type enumeration (indigo.kDeviceAction.*)."""

    On: "kDeviceAction"
    Off: "kDeviceAction"
    Toggle: "kDeviceAction"
    Lock: "kDeviceAction"
    Unlock: "kDeviceAction"
    Open: "kDeviceAction"
    Close: "kDeviceAction"
    SetBrightness: "kDeviceAction"
    BrightenBy: "kDeviceAction"
    DimBy: "kDeviceAction"
    SetColorLevels: "kDeviceAction"
    AllOff: "kDeviceAction"
    AllLightsOn: "kDeviceAction"
    AllLightsOff: "kDeviceAction"
    RequestStatus: "kDeviceAction"


class kDimmerRelayAction(int):
    """Dimmer/relay action type enumeration (indigo.kDimmerRelayAction.*)."""

    On: "kDimmerRelayAction"
    Off: "kDimmerRelayAction"
    Toggle: "kDimmerRelayAction"
    SetBrightness: "kDimmerRelayAction"
    BrightenBy: "kDimmerRelayAction"
    DimBy: "kDimmerRelayAction"
    SetColorLevels: "kDimmerRelayAction"
    AllOff: "kDimmerRelayAction"
    AllLightsOn: "kDimmerRelayAction"
    AllLightsOff: "kDimmerRelayAction"


class kSensorAction(int):
    """Sensor action type enumeration (indigo.kSensorAction.*)."""

    TurnOn: "kSensorAction"
    TurnOff: "kSensorAction"
    Toggle: "kSensorAction"
    RequestStatus: "kSensorAction"


class kSpeedControlAction(int):
    """Speed control action type enumeration (indigo.kSpeedControlAction.*)."""

    TurnOn: "kSpeedControlAction"
    TurnOff: "kSpeedControlAction"
    Toggle: "kSpeedControlAction"
    SetSpeedLevel: "kSpeedControlAction"
    SetSpeedIndex: "kSpeedControlAction"
    IncreaseSpeedIndex: "kSpeedControlAction"
    DecreaseSpeedIndex: "kSpeedControlAction"
    RequestStatus: "kSpeedControlAction"


class kSprinklerAction(int):
    """Sprinkler action type enumeration (indigo.kSprinklerAction.*)."""

    RunNewSchedule: "kSprinklerAction"
    RunPreviousSchedule: "kSprinklerAction"
    PauseSchedule: "kSprinklerAction"
    ResumeSchedule: "kSprinklerAction"
    StopSchedule: "kSprinklerAction"
    PreviousZone: "kSprinklerAction"
    NextZone: "kSprinklerAction"
    ZoneOn: "kSprinklerAction"
    AllZonesOff: "kSprinklerAction"
    RequestStatusAll: "kSprinklerAction"


class kThermostatAction(int):
    """Thermostat action type enumeration (indigo.kThermostatAction.*)."""

    SetHeatSetpoint: "kThermostatAction"
    SetCoolSetpoint: "kThermostatAction"
    IncreaseHeatSetpoint: "kThermostatAction"
    IncreaseCoolSetpoint: "kThermostatAction"
    DecreaseHeatSetpoint: "kThermostatAction"
    DecreaseCoolSetpoint: "kThermostatAction"
    SetHvacMode: "kThermostatAction"
    SetFanMode: "kThermostatAction"
    RequestStatusAll: "kThermostatAction"
    RequestMode: "kThermostatAction"
    RequestEquipmentState: "kThermostatAction"
    RequestTemperatures: "kThermostatAction"
    RequestHumidities: "kThermostatAction"
    RequestDeadbands: "kThermostatAction"
    RequestSetpoints: "kThermostatAction"


class kUniversalAction(int):
    """Universal device action type enumeration (indigo.kUniversalAction.*)."""

    RequestStatus: "kUniversalAction"
    Beep: "kUniversalAction"
    EnergyUpdate: "kUniversalAction"
    EnergyReset: "kUniversalAction"


class kInsteonCmd(int):
    """INSTEON command type enumeration (indigo.kInsteonCmd.*)."""

    On: "kInsteonCmd"
    InstantOn: "kInsteonCmd"
    Off: "kInsteonCmd"
    InstantOff: "kInsteonCmd"
    Brighten: "kInsteonCmd"
    Dim: "kInsteonCmd"
    AllOn: "kInsteonCmd"
    AllOff: "kInsteonCmd"
    AllBrighten: "kInsteonCmd"
    AllDim: "kInsteonCmd"
    AnyCommand: "kInsteonCmd"
    StatusChanged: "kInsteonCmd"
    AllInstantOn: "kInsteonCmd"
    AllInstantOff: "kInsteonCmd"


class kX10Cmd(int):
    """X10 command type enumeration (indigo.kX10Cmd.*)."""

    AllOff: "kX10Cmd"
    AllLightsOn: "kX10Cmd"
    AllLightsOff: "kX10Cmd"
    On: "kX10Cmd"
    Off: "kX10Cmd"
    Brighten: "kX10Cmd"
    Dim: "kX10Cmd"
    PresetDim: "kX10Cmd"
    ExtendedData: "kX10Cmd"
    StatusOnResponse: "kX10Cmd"
    StatusOffResponse: "kX10Cmd"
    AvButtonPressed: "kX10Cmd"
    AnyCommand: "kX10Cmd"


class kX10AvButton(int):
    """X10 AV button type enumeration (indigo.kX10AvButton.*)."""

    Power: "kX10AvButton"
    PC: "kX10AvButton"
    Display: "kX10AvButton"
    Menu: "kX10AvButton"
    Recall: "kX10AvButton"
    Enter: "kX10AvButton"
    Exit: "kX10AvButton"
    Title: "kX10AvButton"
    Right: "kX10AvButton"
    Left: "kX10AvButton"
    Down: "kX10AvButton"
    Up: "kX10AvButton"
    Return: "kX10AvButton"
    Mute: "kX10AvButton"
    AB: "kX10AvButton"
    ChannelUp: "kX10AvButton"
    ChannelDown: "kX10AvButton"
    VolumeUp: "kX10AvButton"
    VolumeDown: "kX10AvButton"
    Play: "kX10AvButton"
    Record: "kX10AvButton"
    Stop: "kX10AvButton"
    Pause: "kX10AvButton"
    Rewind: "kX10AvButton"
    Forward: "kX10AvButton"


class kEmailFilter(int):
    """Email filter type enumeration (indigo.kEmailFilter.*)."""

    AnyEmail: "kEmailFilter"
    MatchEmailFields: "kEmailFilter"


class kElemTypeId(int):
    """Element type ID enumeration (indigo.kElemTypeId.*)."""

    ActionGroup: "kElemTypeId"
    Device: "kElemTypeId"
    Schedule: "kElemTypeId"
    Trigger: "kElemTypeId"
    Variable: "kElemTypeId"
    ControlPage: "kElemTypeId"
    DeviceGroup: "kElemTypeId"


class kSubAtomicTypeId(int):
    """Sub-atomic element type ID enumeration (indigo.kSubAtomicTypeId.*)."""

    Device: "kSubAtomicTypeId"
    Trigger: "kSubAtomicTypeId"
    Schedule: "kSubAtomicTypeId"
    Condition: "kSubAtomicTypeId"
    Action: "kSubAtomicTypeId"
    Control: "kSubAtomicTypeId"


class kProgressDescType(int):
    """Progress description type enumeration (indigo.kProgressDescType.*)."""

    Unused: "kProgressDescType"
    Generic: "kProgressDescType"
    Generic_fail: "kProgressDescType"
    Sent: "kProgressDescType"
    Sent_fail: "kProgressDescType"
    Received: "kProgressDescType"
    Received_fail: "kProgressDescType"
    Processed: "kProgressDescType"
    Processed_fail: "kProgressDescType"
    Executed: "kProgressDescType"
    Executed_fail: "kProgressDescType"


class kDeprecatedTypeId(int):
    """Deprecated type ID enumeration (indigo.kDeprecatedTypeId.*)."""

    ExecuteEmbeddedAppleScript: "kDeprecatedTypeId"
    ExecuteLinkedAppleScript: "kDeprecatedTypeId"


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
