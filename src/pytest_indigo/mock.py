from types import ModuleType

from pytest_indigo.indigo import Dict, List
from pytest_indigo.indigo.device.collection import DeviceList
from pytest_indigo.indigo.device.commands import (
    DeviceCmds,
    DimmerDeviceCmds,
    MultiIODeviceCmds,
    RelayDeviceCmds,
    SensorDeviceCmds,
    SpeedControlDeviceCmds,
    SprinklerDeviceCmds,
    ThermostatDeviceCmds,
)
from pytest_indigo.indigo.device.models import (
    Device,
    DimmerDevice,
    MultiIODevice,
    RelayDevice,
    SensorDevice,
    SpeedControlDevice,
    SprinklerDevice,
    ThermostatDevice,
)
from pytest_indigo.indigo.ids import IndigoIds


class IndigoMock(ModuleType):
    Dict = Dict
    List = List

    ids: IndigoIds

    Device = Device
    RelayDevice = RelayDevice
    DimmerDevice = DimmerDevice
    SensorDevice = SensorDevice
    SpeedControlDevice = SpeedControlDevice
    ThermostatDevice = ThermostatDevice
    SprinklerDevice = SprinklerDevice
    MultiIODevice = MultiIODevice

    # ---- Collections ----
    devices: DeviceList
    """Dict-like collection of all Indigo devices, keyed by device ID or name."""
    # variables: VariableList
    """Dict-like collection of all Indigo variables, keyed by variable ID or name."""
    # triggers: TriggerList
    """Dict-like collection of all Indigo triggers, keyed by trigger ID or name."""
    # schedules: ScheduleList
    """Dict-like collection of all Indigo schedules, keyed by schedule ID or name."""
    # actionGroups: ActionGroupList
    """Dict-like collection of all Indigo action groups, keyed by ID or name."""
    # controlPages: ControlPageList
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
    # variable: VariableCmds
    """Variable command interface."""
    # trigger: EventTriggerCmds
    """Trigger command interface."""
    # schedule: EventScheduleCmds
    """Schedule command interface."""
    # actionGroup: ActionGroupCmds
    """Action group command interface."""
    # controlPage: ControlPageCmds
    """Control page command interface."""

    # ---- Protocol interfaces ----
    # insteon: InsteonCmdInterface
    """INSTEON protocol command interface."""
    # x10: X10CmdInterface
    """X10 protocol command interface."""
    # zwave: ZWaveInterface
    """Z-Wave protocol command interface."""

    # ---- Server / host interfaces ----
    # server: ServerInfo
    """Indigo server properties and commands."""
    # host: HostInfo
    """Internal host interface (not for plugin use)."""

    # ---- Active plugin instance ----
    # activePlugin: PluginBase
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

    def __init__(self):
        self.reset()

    def reset(self):
        self.ids = IndigoIds()

        # ---- Collections ----
        self.devices = DeviceList(ids=self.ids)
        # self.variables = VariableList(ids=self.ids)
        # self.triggers = TriggerList(ids=self.ids)
        # self.schedules = ScheduleList(ids=self.ids)
        # self.actionGroups = ActionGroupList(ids=self.ids)
        # self.controlPages = ControlPageList(ids=self.ids)

        # ---- Device command interfaces ----
        self.device = DeviceCmds()
        self.relay = RelayDeviceCmds()
        self.dimmer = DimmerDeviceCmds()
        self.sensor = SensorDeviceCmds()
        self.speedcontrol = SpeedControlDeviceCmds()
        self.thermostat = ThermostatDeviceCmds()
        self.sprinkler = SprinklerDeviceCmds()
        self.iodevice = MultiIODeviceCmds()

        # ---- Other command interfaces ----
        # self.variable = VariableCmds()
        # self.trigger = EventTriggerCmds()
        # self.schedule = EventScheduleCmds()
        # self.actionGroup = ActionGroupCmds()
        # self.controlPage = ControlPageCmds()

        # ---- Protocol interfaces ----
        # self.insteon = InsteonCmdInterface()
        # self.x10 = X10CmdInterface()
        # self.zwave = ZWaveInterface()

        # ---- Server / host interfaces ----
        # self.server = ServerInfo()

        # ---- Active plugin instance ----
        # self.activePlugin: PluginBase
