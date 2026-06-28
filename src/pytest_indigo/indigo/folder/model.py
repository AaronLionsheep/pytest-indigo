from typing import Iterator, Any

from ..base import BaseElem


class Folder(BaseElem):
    """
    A folder that can contain other elements.

    Exposed in Python as ``indigo.Folder``.
    Properties defined in CFolderElem_pyglue.cpp.
    """

    def refreshFromServer(self, waitUntilServerIdle: bool = False) -> None:
        """Refresh all folder properties from the server."""
        refreshed = self._BaseElem__server_ref._copy_from_server()
        self.__dict__.update(refreshed.__dict__)

    def replaceOnServer(self) -> None:
        """Push local changes to the server."""
        copy = self._copy_from_server()

        self._BaseElem__server_ref.name = copy.name
        self._BaseElem__server_ref.description = copy.description
        self._BaseElem__server_ref.remoteDisplay = copy.remoteDisplay

    def __iter__(self) -> Iterator[tuple[str, Any]]:
        """Yields (key, value) pairs so dict(folder) works. Patched in by utils.py."""
        return [
            ("class", "indigo.Folder"),
            ("id", self.id),
            ("name", self.name),
            ("remoteDisplay", self.remoteDisplay),
        ].__iter__()
