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
        ...

    def replaceOnServer(self) -> None:
        """Push local changes to the server."""
        ...

    def __iter__(self) -> Iterator[tuple[str, Any]]:
        """Yields (key, value) pairs so dict(folder) works. Patched in by utils.py."""
        ...