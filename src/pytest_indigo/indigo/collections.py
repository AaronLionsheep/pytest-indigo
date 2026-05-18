import string
from typing import Any
from copy import deepcopy


class List(list):
    pass

class Dict(dict):
    def get(self, key: str, default: Any = None) -> Any:
        return super().get(key, default)

    def __setitem__(self, key: str, value) -> None:
        if key[0] in string.digits or key[0] in string.punctuation or " " in key:
            raise RuntimeError("LowLevelBadParameterError -- illegal XML tag name character")

        super().__setitem__(key, value)

    def __getitem__(self, key: str) -> Any:
        value = super().__getitem__(key)
        return deepcopy(value)

    def to_dict(self) -> dict:
        return dict(self)