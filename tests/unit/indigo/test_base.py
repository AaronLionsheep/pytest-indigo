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
