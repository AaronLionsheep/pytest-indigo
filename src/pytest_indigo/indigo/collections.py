import string
from typing import Any
from copy import deepcopy


def _validate_value(value: Any) -> None:
    """Validate collection values against documented rules"""
    if isinstance(value, (bool, float, int, str)):
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
    pass

class Dict(dict):
    def get(self, key: str, default: Any = None) -> Any:
        return super().get(key, default)
    
    @staticmethod
    def __validate_key(key: str):
        """Validate keys against documented rules"""
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
        return dict(self)