import pytest

from collections.abc import Iterator

from pytest_indigo.indigo.ids import IndigoIds
from pytest_indigo.indigo.folder import FolderCmds, Folder


@pytest.fixture()
def ids() -> IndigoIds:
    return IndigoIds()


@pytest.fixture()
def folder(ids) -> FolderCmds:
    return FolderCmds(ids=ids)


# MARK: __getitem__()
class TestDunderGetitem:
    def test_by_id(self, folder: FolderCmds):
        f = folder.create("pytest")
        result = folder[f.id]

        assert result.id == f.id

    def test_by_id_raises_key_error(self, folder: FolderCmds):
        with pytest.raises(KeyError, match="'key id 5 not found in database'"):
            folder[5]

    def test_by_name(self, folder: FolderCmds):
        f = folder.create("pytest")
        f = folder.create("pytest 2")
        result = folder["pytest 2"]

        assert result.id == f.id

    def test_by_name_raises_key_error(self, folder: FolderCmds):
        with pytest.raises(KeyError, match="'key name five not found in database'"):
            folder["five"]

    def test_by_folder(self, folder: FolderCmds):
        f = folder.create("pytest")
        result = folder[f]

        assert result.id == f.id

    def test_by_folder_raises_key_error(self, folder: FolderCmds):
        f = Folder.__create__(5, "new folder")
        with pytest.raises(KeyError, match="'key id 5 not found in database'"):
            folder[f]

    def test_by_none_raises_type_error(self, folder: FolderCmds):
        with pytest.raises(KeyError, match="'required elem or key type was None'"):
            folder[None]

    @pytest.mark.parametrize("key", [True, False, dict(), set(), object()])
    def test_raise_type_error_on_bad_elem_key(self, folder: FolderCmds, key):
        with pytest.raises(
            TypeError,
            match="elem or key type must be either an elem integer ID, elem string name, or elem instance",
        ):
            folder.get(key)

    def test_returns_copy(self, folder: FolderCmds):
        f = folder.create("pytest")
        f_name = folder[f.name]
        f_id = folder[f.id]
        f_folder = folder[f]

        assert f_name is not folder._FolderCmds__folders[f.id]
        assert f_id is not folder._FolderCmds__folders[f.id]
        assert f_folder is not folder._FolderCmds__folders[f.id]


# MARK: __contains__()
class TestDunderContains:
    @pytest.mark.parametrize("key", [2, "pytest 2", Folder.__create__(2, "pytest 2")])
    def test_in(self, folder: FolderCmds, key):
        folder.create("pytest 1")
        folder.create("pytest 2")

        assert folder.__contains__(key)

    @pytest.mark.parametrize(
        "key", [None, 2, "pytest 2", Folder.__create__(2, "pytest 2")]
    )
    def test_not_in(self, folder: FolderCmds, key):
        folder.create("pytest")

        assert not folder.__contains__(key)

    @pytest.mark.parametrize("key", [True, False, dict(), set(), object()])
    def test_raise_type_error(self, folder: FolderCmds, key):
        with pytest.raises(
            TypeError,
            match="elem or key type must be either an elem integer ID, elem string name, or elem instance",
        ):
            folder.__contains__(key)


# MARK: __iter__()
class TestDunderIter: ...


# MARK: __len__()
class TestDunderLen:
    def test_empty(self, folder: FolderCmds):
        assert len(folder) == 0

    def test_items(self, folder: FolderCmds):
        folder.create("pytest")
        assert len(folder) == 1


# MARK: get()
class TestGet:
    def test_by_id(self, folder: FolderCmds):
        f = folder.create("pytest")
        result = folder.get(f.id)

        assert result.id == f.id

    def test_by_name(self, folder: FolderCmds):
        f = folder.create("pytest")
        result = folder.get("pytest")

        assert result.id == f.id

    def test_by_folder(self, folder: FolderCmds):
        f = folder.create("pytest")
        result = folder.get(f)

        assert result.id == f.id

    def test_by_none_returns_default(self, folder: FolderCmds):
        assert folder.get(None, default=123) == 123

    @pytest.mark.parametrize("key", [True, False, dict(), set(), object()])
    def test_raise_type_error_on_bad_elem_key(self, folder: FolderCmds, key):
        with pytest.raises(
            TypeError,
            match="elem or key type must be either an elem integer ID, elem string name, or elem instance",
        ):
            folder.get(key)

    def test_returns_copy(self, folder: FolderCmds):
        f = folder.create("pytest")
        f_name = folder.get(f.name)
        f_id = folder.get(f.id)
        f_folder = folder.get(f)

        assert f_name is not folder._FolderCmds__folders[f.id]
        assert f_id is not folder._FolderCmds__folders[f.id]
        assert f_folder is not folder._FolderCmds__folders[f.id]


# MARK: keys()
class TestKeys:
    def test_empty(self, folder: FolderCmds):
        assert folder.keys() == []

    def test_items(self, folder: FolderCmds):
        f1 = folder.create("pytest 1")
        f2 = folder.create("pytest 2")
        f3 = folder.create("pytest 3")

        assert folder.keys() == [f1.id, f2.id, f3.id]


# MARK: has_key()
class TestHasKey:
    def test_by_id(self, folder: FolderCmds):
        f = folder.create("pytest")

        assert folder.has_key(f)

    def test_by_name(self, folder: FolderCmds):
        f = folder.create("pytest")

        assert folder.has_key(f)

    def test_by_folder(self, folder: FolderCmds):
        f = folder.create("pytest")

        assert folder.has_key(f)

    @pytest.mark.parametrize("key", [True, False, dict(), set(), object()])
    def test_raise_type_error(self, folder: FolderCmds, key):
        with pytest.raises(
            TypeError,
            match="elem or key type must be either an elem integer ID, elem string name, or elem instance",
        ):
            folder.has_key(key)


# MARK: iter()
class TestIter:
    def test_returns_iterator(self, folder: FolderCmds):
        result = folder.iter()

        assert isinstance(result, Iterator)

    def test_has_folders(self, folder: FolderCmds):
        folder.create("1")
        folder.create("2")
        folder.create("3")

        iter = folder.iter()
        assert next(iter).name == "1"
        assert next(iter).name == "2"
        assert next(iter).name == "3"

        with pytest.raises(StopIteration):
            next(iter)

    def test_returns_copies(self, folder: FolderCmds):
        f1 = folder.create("1")
        f2 = folder.create("2")

        iter = folder.iter()
        assert next(iter) is not f1
        assert next(iter) is not f2


# MARK: itervalues()
class TestItervalues:
    def test_returns_iterator(self, folder: FolderCmds):
        result = folder.itervalues()

        assert isinstance(result, Iterator)

    def test_has_folders(self, folder: FolderCmds):
        folder.create("1")
        folder.create("2")
        folder.create("3")

        iter = folder.itervalues()
        assert next(iter).name == "1"
        assert next(iter).name == "2"
        assert next(iter).name == "3"

        with pytest.raises(StopIteration):
            next(iter)

    def test_returns_copies(self, folder: FolderCmds):
        f1 = folder.create("1")
        f2 = folder.create("2")

        iter = folder.itervalues()
        assert next(iter) is not f1
        assert next(iter) is not f2


# MARK: iterkeys()
class TestIterkeys:
    def test_returns_iterator(self, folder: FolderCmds):
        result = folder.iterkeys()

        assert isinstance(result, Iterator)

    def test_has_folders(self, folder: FolderCmds):
        folder.create("folder 1")
        folder.create("folder 2")
        folder.create("folder 3")

        iter = folder.iterkeys()
        assert next(iter) == 1
        assert next(iter) == 2
        assert next(iter) == 3

        with pytest.raises(StopIteration):
            next(iter)


# MARK: len()
class TestLen:
    def test_empty(self, folder: FolderCmds):
        assert folder.len() == 0

    def test_items(self, folder: FolderCmds):
        folder.create("pytest")
        assert folder.len() == 1


# MARK: getName()
class TestGetName:
    def test_returns_name(self, folder: FolderCmds):
        f = folder.create("pytest")

        assert folder.getName(f.id) == "pytest"

    def test_not_found_returns_empty_string(self, folder: FolderCmds):
        assert folder.getName(0) == ""

    @pytest.mark.parametrize("key", [True, False, dict(), set(), object()])
    def test_raise_type_error(self, folder: FolderCmds, key):
        with pytest.raises(
            TypeError,
            match="elem or key type must be either an elem integer ID, elem string name, or elem instance",
        ):
            folder.getName(key)


# MARK: getId()
class TestGetId:
    def test_returns_id(self, folder: FolderCmds):
        f = folder.create("pytest")

        assert folder.getId("pytest") == f.id

    def test_not_found_returns_0(self, folder: FolderCmds):
        assert folder.getId("pytest") == 0

    @pytest.mark.parametrize("key", [True, False, dict(), set(), object()])
    def test_raise_type_error(self, folder: FolderCmds, key):
        with pytest.raises(
            TypeError,
            match="elem or key type must be either an elem integer ID, elem string name, or elem instance",
        ):
            folder.getId(key)


# MARK: create()
class TestCreate:
    def test_makes_new_folder(self, folder: FolderCmds, ids: IndigoIds):
        expected_id = ids.peek()
        folder.create("pytest")

        assert folder._FolderCmds__folders.keys() == {expected_id}

    def test_returns_a_folder(self, folder: FolderCmds, ids: IndigoIds):
        expected_id = ids.peek()
        f = folder.create("pytest")

        assert isinstance(f, Folder)
        assert f.id == expected_id
        assert f.name == "pytest"

    def test_returns_copy(self, folder: FolderCmds):
        f = folder.create("pytest")

        assert folder._FolderCmds__folders[f.id] is not f

    def test_raises_value_error_on_duplicate_name(self, folder: FolderCmds):
        folder.create("pytest")

        with pytest.raises(ValueError, match="NameNotUniqueError"):
            folder.create("pytest")

    def test_default_name(self, folder: FolderCmds):
        f = folder.create()

        assert f.name == "new folder"

    def test_default_name_sequence(self, folder: FolderCmds):
        assert folder.create("").name == "new folder"
        assert folder.create("").name == "new folder 1"
        assert folder.create("").name == "new folder 2"
        assert folder.create("").name == "new folder 3"
        assert folder.create("").name == "new folder 4"

    def test_default_name_sequence_existing(self, folder: FolderCmds):
        folder.create("new folder 2")
        folder.create("new folder 3")

        assert folder.create("").name == "new folder"
        assert folder.create("").name == "new folder 1"
        assert folder.create("").name == "new folder 4"


# MARK: duplicate()
class TestDuplicate:
    def test_makes_new_folder(self, folder: FolderCmds, ids: IndigoIds):
        f1 = folder.create("pytest")
        f2 = folder.duplicate("pytest", "duplicate")

        assert folder._FolderCmds__folders.keys() == {f1.id, f2.id}

    def test_returns_a_folder(self, folder: FolderCmds, ids: IndigoIds):
        folder.create("pytest")
        expected_id = ids.peek()
        duplicate = folder.duplicate("pytest", "duplicate")

        assert isinstance(duplicate, Folder)
        assert duplicate.id == expected_id
        assert duplicate.name == "duplicate"

    def test_returns_copy(self, folder: FolderCmds):
        folder.create("pytest")
        duplicate = folder.duplicate("pytest", "duplicate")

        assert folder._FolderCmds__folders[duplicate.id] is not duplicate

    def test_raises_value_error_on_duplicate_name(self, folder: FolderCmds):
        folder.create("pytest")

        with pytest.raises(ValueError, match="NameNotUniqueError"):
            folder.duplicate("pytest", "pytest")


# MARK: delete()
class TestDelete:
    def test_by_id(self, folder: FolderCmds):
        f = folder.create("pytest")
        folder.delete(f.id)

        assert f not in folder

    def test_by_id_not_found_raises_value_error(self, folder: FolderCmds):
        with pytest.raises(
            ValueError,
            match="ElementNotFoundError -- could not find device with element ID 123",
        ):
            folder.delete(123)

    def test_by_name(self, folder: FolderCmds):
        f = folder.create("pytest")
        folder.delete("pytest")

        assert f not in folder

    def test_by_name_not_found_raises_value_error(self, folder: FolderCmds):
        with pytest.raises(
            ValueError, match='ElementNotFoundError -- could not find device "test"'
        ):
            folder.delete("test")

    def test_by_folder(self, folder: FolderCmds):
        f = folder.create("pytest")
        folder.delete(f)

        assert f not in folder

    def test_by_folder_not_found_raises_value_error(self, folder: FolderCmds):
        with pytest.raises(
            ValueError,
            match="ElementNotFoundError -- could not find device with element ID 1",
        ):
            folder.delete(Folder.__create__(1, "folder"))

    @pytest.mark.xfail(reason="NotImplemented")
    def test_delete_children(self, folder: FolderCmds):
        folder.create("pytest")
        folder.delete("pytest", deleteAllChildren=True)


# MARK: displayInRemoteUI()
class TestDisplayInRemoteUI:
    def test_hide(self, folder: FolderCmds):
        f = folder.create("pytest")
        folder.displayInRemoteUI("pytest", False)

        assert f.remoteDisplay is True
        assert folder["pytest"].remoteDisplay is False

    def test_by_id_not_found_raises_value_error(self, folder: FolderCmds):
        with pytest.raises(
            ValueError,
            match="ElementNotFoundError -- could not find device with element ID 123",
        ):
            folder.displayInRemoteUI(123, False)

    def test_by_name_not_found_raises_value_error(self, folder: FolderCmds):
        with pytest.raises(
            ValueError, match='ElementNotFoundError -- could not find device "test"'
        ):
            folder.displayInRemoteUI("test", False)

    def test_by_folder_not_found_raises_value_error(self, folder: FolderCmds):
        with pytest.raises(
            ValueError,
            match="ElementNotFoundError -- could not find device with element ID 1",
        ):
            folder.displayInRemoteUI(Folder.__create__(1, "folder"), False)
