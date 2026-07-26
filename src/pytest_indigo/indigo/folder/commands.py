from collections.abc import Iterator
from typing import Any

from ..base import ElemKey
from ..ids import IndigoIds
from .model import Folder


class FolderCmds:
    """
    Command interface for folder operations, also behaves as a collection.
    Do not instantiate directly; use the pre-created instances
    (e.g. ``indigo.devices.folders``).
    """

    def __init__(self, ids: IndigoIds):
        self.__ids = ids
        self.__folders: dict[int, Folder] = {}

    # --- collection interface ---
    def __getitem__(self, key: ElemKey) -> Folder:
        if isinstance(key, int) and not isinstance(key, bool):
            try:
                return self.__folders[key]._copy_from_server()
            except KeyError:
                raise KeyError(f"'key id {key} not found in database'")
        elif isinstance(key, str):
            for folder in self:
                if folder.name == key:
                    return folder._copy_from_server()

            raise KeyError(f"'key name {key} not found in database'")
        elif isinstance(key, Folder):
            try:
                return self.__folders[key.id]._copy_from_server()
            except KeyError:
                raise KeyError(f"'key id {key.id} not found in database'")
        elif key is None:
            raise KeyError("required elem or key type was None")
        else:
            raise TypeError(
                "elem or key type must be either an elem integer ID, elem string name, or elem instance"
            )

    def __contains__(self, key: object) -> bool:
        if key is None:
            return False

        if isinstance(key, bool) or not isinstance(key, (int, str, Folder)):
            raise TypeError(
                "elem or key type must be either an elem integer ID, elem string name, or elem instance"
            )

        for folder in self:
            if (
                isinstance(key, int)
                and folder.id == key
                or isinstance(key, str)
                and folder.name == key
                or isinstance(key, Folder)
                and folder.name == key.name
            ):
                return True

        return False

    def __iter__(self) -> Iterator[Folder]:
        return self.__folders.values().__iter__()

    def __len__(self) -> int:
        return len(self.__folders)

    def get(self, key: ElemKey, default: Any = None) -> Folder | None:
        """Return folder by key, or *default* if not found."""
        try:
            return self[key]
        except KeyError:
            return default

    def keys(self, filter: str = "") -> list[int]:
        """Return a list of folder IDs, optionally filtered."""
        return list(self.__folders.keys())

    def has_key(self, key: ElemKey) -> bool:
        """Return True if *key* exists in the folder collection."""
        return key in self

    def iter(self, filter: str = "") -> Iterator[Folder]:
        """Iterate folder objects with an optional filter expression."""
        folders = [folder._copy_from_server() for folder in self.__folders.values()]
        return folders.__iter__()

    def itervalues(self, filter: str = "") -> Iterator[Folder]:
        """Alias for iter()."""
        return self.iter()

    def iterkeys(self, filter: str = "") -> Iterator[int]:
        """Iterate folder IDs with an optional filter expression."""
        return self.__folders.keys().__iter__()

    def len(self, filter: str = "") -> int:
        """Return the number of folders, optionally filtered."""
        return len(self)

    def getName(self, key: int) -> str:
        """Return the name for folder *key* (ID), or '' if not found."""
        if folder := self.get(key):
            return folder.name

        return ""

    def getId(self, name: str) -> int:
        """Return the ID for folder *name*, or 0 if not found."""
        if folder := self.get(name):
            return folder.id

        return 0

    # --- command interface ---
    def create(self, name: str = "") -> Folder:
        """Add a new folder to the Indigo Server."""
        # Create a folder with a default name
        if name == "":
            try:
                return self.create("new folder")
            except ValueError:
                pass

            i = 1
            while True:
                try:
                    return self.create(f"new folder {i}")
                except ValueError:
                    i += 1

        # Ensure the desired name is unique
        for folder in self:
            if folder.name == name:
                raise ValueError("NameNotUniqueError")

        id = next(self.__ids)
        folder = Folder.__create__(id=id, name=name)

        self.__folders[id] = folder

        return folder._copy_from_server()

    def duplicate(self, elem: ElemKey, duplicateName: str = "") -> Folder:
        """Duplicate an existing folder on the Indigo Server."""
        return self.create(duplicateName)

    def delete(self, elem: ElemKey, deleteAllChildren: bool = False) -> None:
        """Delete an existing folder from the Indigo Server."""
        folder = self.get(elem)
        if folder is None:
            if isinstance(elem, int):
                raise ValueError(
                    f"ElementNotFoundError -- could not find device with element ID {elem}"
                )
            elif isinstance(elem, str):
                raise ValueError(
                    f'ElementNotFoundError -- could not find device "{elem}"'
                )
            else:
                raise ValueError(
                    f"ElementNotFoundError -- could not find device with element ID {elem.id}"
                )

        if deleteAllChildren:
            # TODO: Delete children?
            raise NotImplementedError()

        del self.__folders[folder.id]

    def displayInRemoteUI(self, elem: ElemKey, value: bool) -> None:
        """Change a folder's remote UI display visibility."""
        folder = self.get(elem)
        if folder is None:
            if isinstance(elem, int):
                raise ValueError(
                    f"ElementNotFoundError -- could not find device with element ID {elem}"
                )
            elif isinstance(elem, str):
                raise ValueError(
                    f'ElementNotFoundError -- could not find device "{elem}"'
                )
            else:
                raise ValueError(
                    f"ElementNotFoundError -- could not find device with element ID {elem.id}"
                )

        self.__folders[folder.id].remoteDisplay = value
