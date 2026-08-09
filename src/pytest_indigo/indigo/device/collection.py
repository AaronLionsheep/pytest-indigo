from collections.abc import Iterator
from typing import TYPE_CHECKING

from ..base import ElemKey
from ..base.collection import _ElemCollection

if TYPE_CHECKING:
    from .models import Device


class DeviceList(_ElemCollection):
    """Collection of all Indigo devices (``indigo.devices``)."""

    def __getitem__(self, key: ElemKey) -> "Device": ...  # type: ignore[override]
    def __iter__(self) -> Iterator["Device"]: ...  # type: ignore[override]
    def iter(self, filter: str = "") -> Iterator["Device"]: ...  # type: ignore[override]
    def itervalues(self, filter: str = "") -> Iterator["Device"]: ...  # type: ignore[override]
    def iterkeys(self, filter: str = "") -> Iterator[int]: ...
