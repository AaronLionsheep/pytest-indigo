from typing import TypeAlias, Union, Self
from copy import deepcopy
from .collections import Dict


ElemKey: TypeAlias = Union[int, str, "BaseElem"]


class BaseElem:
    """
    Base class for all Indigo database elements (devices, variables, triggers,
    schedules, action groups, control pages, folders).

    Exposed in Python as ``indigo.BaseElem``.
    Properties defined in CListElem_pyglue.cpp.
    """

    __id: int
    __name: str
    __description: str
    __remote_display: bool
    __global_props: Dict
    __shared_props: Dict
    __server_ref: Self | None

    def __init__(self, *args, **kwargs):
        raise RuntimeError("This class cannot be instantiated from Python")

    @classmethod
    def __create__(cls, id: int, name: str, server_ref: Self | None = None):
        instance = super().__new__(cls)

        # Fake our __init__ and initialize the instance
        instance.__id = id
        instance.__name = name
        instance.__description = ""
        instance.__remote_display = True
        instance.__global_props = Dict()
        instance.__shared_props = Dict()
        instance.__server_ref = server_ref

        return instance

    def _copy_from_server(self) -> Self:
        """Returns a copy of this object with a reference to the server object."""
        copy = deepcopy(self)
        copy.__server_ref = self.__server_ref or self

        return copy

    @property
    def id(self) -> int:
        """Unique integer ID of the element."""
        return self.__id

    @property
    def name(self) -> str:
        """Display name of the element."""
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value

    @property
    def description(self) -> str:
        """Description string of the element."""
        return self.__description

    @description.setter
    def description(self, value: str) -> None:
        self.__description = value

    @property
    def remoteDisplay(self) -> bool:
        """Whether the element is displayed in remote UIs (Indigo Touch, web server)."""
        return self.__remote_display

    @remoteDisplay.setter
    def remoteDisplay(self, value: bool) -> None:
        self.__remote_display = value

    @property
    def globalProps(self) -> Dict:
        """Dict of all plugin-specific props (keyed by pluginId)."""
        return self.__global_props

    @property
    def ownerProps(self) -> Dict:
        """
        Dict of props owned by the plugin that owns this element
        (same as pluginProps for plugins, but accessible by all).
        """
        return Dict()

    @property
    def pluginProps(self) -> Dict:
        """
        Dict of props for the calling plugin (the plugin's own namespace
        within globalProps). Read-only; use replacePluginPropsOnServer()
        to persist changes.
        """
        return Dict()

    @property
    def sharedProps(self) -> Dict:
        """
        Dict of shared props visible to all plugins. Read-only; use
        replaceSharedPropsOnServer() to persist changes.
        """
        return self.__shared_props
