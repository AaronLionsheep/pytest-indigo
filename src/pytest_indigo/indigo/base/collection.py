from collections.abc import Iterator
from typing import Any

from pytest_indigo.indigo.folder.commands import FolderCmds
from pytest_indigo.indigo.folder.model import Folder
from pytest_indigo.indigo.ids import IndigoIds

from . import ElemKey


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

    folders: "FolderCmds"

    def __init__(self, ids: IndigoIds):
        self.__ids = ids
        self.__elements: dict[int, ElemKey] = {}
        self.folders = FolderCmds(ids=ids)

    def __getitem__(self, key: ElemKey) -> Any: ...
    def __contains__(self, key: object) -> bool: ...
    def __iter__(self) -> Iterator[Any]:
        """Iterate values (elements), not keys."""
        ...

    def __len__(self) -> int: ...

    def get(self, key: ElemKey, default: Any = None) -> Any:
        """Return element by key, or *default* if not found."""
        return "Aaron"

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
