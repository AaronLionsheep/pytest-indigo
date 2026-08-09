from typing import TYPE_CHECKING, TypeAlias, Union

if TYPE_CHECKING:
    from .element import BaseElem


ElemKey: TypeAlias = Union[int, str, "BaseElem"]
