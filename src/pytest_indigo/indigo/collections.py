import string
from typing import Any, SupportsIndex, overload, override, TypeAlias, Iterable, TypeVar, Generic
from copy import deepcopy


CollectionValue: TypeAlias = None | bool | float | int | str | list["CollectionValue"] | dict[str, "CollectionValue"]

type_strings = {
    None: "empty",
    int: "integer",
    float: "real",
    str: "string",
    bool: "bool",
    list: "list",
    dict: "dict"
}

def _validate_value(value: Any) -> None:
    """Validate collection values against documented rules"""
    if value is None or isinstance(value, (bool, float, int, str)):
        return

    if isinstance(value, list):
        for value_item in value:
            _validate_value(value_item)
    elif isinstance(value, dict):
        for value_item in value.values():
            _validate_value(value_item)
    else:
        raise TypeError(
            f"No registered converter was able to produce a C++ rvalue of type CCString from this Python object of type {type(value)}"
        )

class List(list):
    """
    Indigo list wrapper. Behaves like a regular Python list but may carry
    additional Indigo metadata.
    """
    def __init__(self, iterable: Iterable[CollectionValue] | None = None, /) -> None:
        if iterable is None:
            super().__init__()
        else:
            _validate_value(iterable)
            super().__init__(iterable)

    def __setitem__(self, key: SupportsIndex, value: CollectionValue, /) -> None: # type: ignore
        if isinstance(key, slice):
            raise NotImplementedError()
        
        _validate_value(value)
        super().__setitem__(key, value)

    def __getitem__(self, key: SupportsIndex, /) -> CollectionValue: # type: ignore
        if isinstance(key, slice):
            raise NotImplementedError()

        value = super().__getitem__(key)
        return deepcopy(value)
    
    def append(self, object: CollectionValue, /) -> None:
        _validate_value(object)
        super().append(object)

    def extend(self, iterable: Iterable[CollectionValue], /) -> None:
        for item in iterable: _validate_value(item)
        super().extend(iterable)

    def to_list(self) -> list:
        """Recursively convert to a plain Python list, converting any nested
        indigo.Dict / indigo.List values and Indigo constants to their Python equivalents.
        Patched in by utils.py.
        """
        return list(self)

class Dict(dict):
    """
    Indigo dict wrapper. Behaves like a regular Python dict but may carry
    additional Indigo metadata. Used for pluginProps, globalProps, sharedProps, etc.
    """

    def get(self, key: str, default: Any = None) -> Any:
        return super().get(key, default)
    
    @staticmethod
    def __validate_key(key: str):
        """Validate keys against documented rules"""
        if not isinstance(key, str):
            raise TypeError(
                f"No registered converter was able to produce a C++ rvalue of type CCString from this Python object of type {type(key)}"
            )

        if key[0] in string.digits or key[0] in string.punctuation or " " in key:
            raise RuntimeError("LowLevelBadParameterError -- illegal XML tag name character")
    
    def __setitem__(self, key: str, value: bool | float | int | str | list | dict) -> None:
        # Validate the key and value
        self.__validate_key(key)
        _validate_value(value)

        super().__setitem__(key, value)

    def __getitem__(self, key: str) -> Any:
        value = super().__getitem__(key)
        return deepcopy(value)

    def to_dict(self) -> dict:
        """Recursively convert to a plain Python dict, converting any nested
        indigo.Dict / indigo.List values and Indigo constants to their Python equivalents.
        Patched in by utils.py.
        """
        return dict(self)