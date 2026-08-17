import pytest

from pytest_indigo.indigo.folder import FolderCmds
from pytest_indigo.indigo.ids import IndigoIds


@pytest.fixture()
def ids() -> IndigoIds:
    return IndigoIds()


@pytest.fixture()
def folder(ids) -> FolderCmds:
    return FolderCmds(ids=ids)


# MARK: refreshFromServer()
class TestRefreshFromServer:
    def test_refresh_name(self, folder: FolderCmds):
        f = folder.create("pytest")

        folder._FolderCmds__folders[f.id].name = "UPDATED"
        f.refreshFromServer()

        assert f.name == "UPDATED"

    def test_refresh_description(self, folder: FolderCmds):
        f = folder.create("pytest")

        folder._FolderCmds__folders[f.id].description = "UPDATED"
        f.refreshFromServer()

        assert f.description == "UPDATED"

    def test_refresh_remote_display(self, folder: FolderCmds):
        f = folder.create("pytest")

        folder.displayInRemoteUI(f, value=False)
        f.refreshFromServer()

        assert f.remoteDisplay is False


# MARK: refreshFromServer()
class TestReplaceOnServer:
    def test_replace_name(self, folder: FolderCmds):
        f = folder.create("pytest")
        f.name = "UPDATED"
        f.replaceOnServer()

        assert folder._FolderCmds__folders[f.id].name == "UPDATED"

    def test_replace_description(self, folder: FolderCmds):
        f = folder.create("pytest")
        f.description = "UPDATED"
        f.replaceOnServer()

        assert folder._FolderCmds__folders[f.id].description == "UPDATED"

    def test_replace_remote_display(self, folder: FolderCmds):
        f = folder.create("pytest")
        f.remoteDisplay = False
        f.replaceOnServer()

        assert folder._FolderCmds__folders[f.id].remoteDisplay is False


# MARK: __iter__()
class TestIter:
    def test_returns_primary_attributes(self, folder: FolderCmds):
        f = folder.create("pytest")

        assert list(f.__iter__()) == [
            ("class", "indigo.Folder"),
            ("id", f.id),
            ("name", f.name),
            ("remoteDisplay", f.remoteDisplay),
        ]
