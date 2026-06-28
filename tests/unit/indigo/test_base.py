import pytest

from pytest_indigo.indigo.base import BaseElem


def get_element() -> BaseElem:
    return BaseElem.__create__(1, "Element")


def test_init_raises_runtime_error():
    with pytest.raises(
        RuntimeError, match="This class cannot be instantiated from Python"
    ):
        BaseElem()


def test_new_initializes_instance_data():
    element = get_element()

    assert element.id == 1
    assert element.name == "Element"
    assert element.description == ""
    assert element.remoteDisplay is True


def test_get_name():
    assert get_element().name == "Element"


def test_set_name():
    element = get_element()
    element.name = "New Element"
    assert element.name == "New Element"


def test_get_id():
    assert get_element().id == 1


def test_get_description():
    assert get_element().description == ""


def test_set_description():
    element = get_element()
    element.description = "New description"
    assert element.description == "New description"


def test_get_remote_display():
    assert get_element().remoteDisplay is True


def test_set_remote_display():
    element = get_element()
    element.remoteDisplay = False
    assert element.remoteDisplay is False


def test_get_global_props():
    assert get_element().globalProps == {}


def test_get_shared_props():
    assert get_element().sharedProps == {}


def test_get_owner_props():
    assert get_element().ownerProps == {}


def test_get_plugin_props():
    assert get_element().pluginProps == {}


def test_copy_from_server_sets_server_ref_when_none():
    element = BaseElem.__create__(1, "Element")
    copy = element._copy_from_server()

    # element is the "server", so it should not have a server ref
    # assert element._BaseElem__server_ref is None
    # copy should have a full reference to the server element
    assert copy._BaseElem__server_ref is element

    # Make sure everything else is copied
    assert element is not copy
    assert element._BaseElem__global_props is not copy._BaseElem__global_props
    assert element._BaseElem__shared_props is not copy._BaseElem__shared_props


def test_copy_from_server_preserves_server_ref():
    element = BaseElem.__create__(1, "Element")
    copy1 = element._copy_from_server()
    copy2 = copy1._copy_from_server()

    assert copy1 is not copy2
    assert copy1._BaseElem__server_ref is element
    assert copy2._BaseElem__server_ref is element
