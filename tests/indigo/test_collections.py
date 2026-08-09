import string

import pytest

from pytest_indigo.indigo.collections import Dict, List

PRIMITIVE_VALUES = [None, True, False, 1.8, -7.5, 10, "", "pytest", [], {}]
COMPLEX_VALUES = [Exception("PYTEST"), object(), {1, 2, 3}]


def test_list_init_primitive_values():
    ilist = List(PRIMITIVE_VALUES)

    assert ilist == PRIMITIVE_VALUES


def test_list_get_by_index():
    ilist = List("abcdefghijklmnopqrstuvwxyz")

    assert ilist[0] == "a"
    assert ilist[25] == "z"


@pytest.mark.parametrize("value", PRIMITIVE_VALUES)
def test_list_appends_primitive_values(value):
    ilist = List(PRIMITIVE_VALUES)
    ilist.append(value)

    assert ilist == [*PRIMITIVE_VALUES, value]


def test_list_extends_primitive_values():
    ilist = List(PRIMITIVE_VALUES)
    ilist.extend(PRIMITIVE_VALUES)

    assert ilist == [*PRIMITIVE_VALUES, *PRIMITIVE_VALUES]


@pytest.mark.parametrize("value", PRIMITIVE_VALUES)
def test_list_set_primitive_value(value):
    ilist = List(["PYTEST"])
    ilist[0] = value

    assert ilist == [value]


def test_list_init_complex_values_raises_type_error():
    with pytest.raises(TypeError):
        List(COMPLEX_VALUES)


@pytest.mark.parametrize("value", COMPLEX_VALUES)
def test_list_append_complex_values_raises_type_error(value):
    ilist = List()
    with pytest.raises(TypeError):
        ilist.append(value)


def test_list_set_by_slice_raises_not_implemented_error():
    ilist = List()
    with pytest.raises(NotImplementedError):
        ilist[5:] = [1, 2, 3, 4, 5, 6]  # type: ignore


def test_list_get_by_slice_raises_not_implemented_error():
    ilist = List()
    with pytest.raises(NotImplementedError):
        ilist[5:]  # type: ignore


def test_list_to_list_simple():
    ilist = List([1, 2, 3, 4, 5])

    assert ilist.to_list() == [1, 2, 3, 4, 5]


def test_list_to_list_converts_nested_lists_and_dicts():
    ilist = List(
        [
            1,
            2,
            List([3, 4]),
            Dict({"5": 5, "6": 6, "7": List([8, 9])}),
            List([Dict({"10": 10, "11": 11}), Dict({"12": 12, "13": 13})]),
        ]
    )

    assert ilist.to_list() == [
        1,
        2,
        [3, 4],
        {"5": 5, "6": 6, "7": [8, 9]},
        [{"10": 10, "11": 11}, {"12": 12, "13": 13}],
    ]


def test_list_values_return_copy():
    outer = List()
    inner = List([1, 2, 3])
    outer.append(inner)

    assert outer[0] == inner
    assert outer[0] is not inner


@pytest.mark.parametrize("value", PRIMITIVE_VALUES)
def test_dict_init_primitive_value(value):
    idict = Dict({"value": value})

    assert idict["value"] == value


@pytest.mark.parametrize("value", COMPLEX_VALUES)
def test_dict_init_complex_value_raises_type_error(value):
    with pytest.raises(TypeError):
        Dict({"value": value})


def test_dict_get_key():
    idict = Dict()
    idict["key"] = 5

    assert idict.get("key") == 5


def test_dict_get_missing_key_returns_none_by_default():
    idict = Dict()

    assert idict.get("key") is None


def test_dict_get_missing_key_returns_default():
    idict = Dict()

    assert idict.get("key", 5) == 5


@pytest.mark.parametrize("key", ["abc123", "one23", "a/2", "A-_m!@"])
def test_dict_keys(key):
    idict = Dict()
    idict[key] = "PYTEST"

    assert idict[key] == "PYTEST"


@pytest.mark.parametrize("key", [1, None, []])
def test_dict_non_string_key_raises_type_error(key):
    with pytest.raises(TypeError):
        idict = Dict()
        idict[key] = "PYTEST"


@pytest.mark.parametrize("key", [" ", "ab c"])
def test_dict_key_with_space_raises_runtime_error(key):
    with pytest.raises(
        RuntimeError,
        match="LowLevelBadParameterError -- illegal XML tag name character",
    ):
        idict = Dict()
        idict[key] = "PYTEST"


@pytest.mark.parametrize("key_start", list(string.digits + string.punctuation))
def test_dict_key_starting_with_number_or_character_raises_runtime_error(key_start):
    with pytest.raises(
        RuntimeError,
        match="LowLevelBadParameterError -- illegal XML tag name character",
    ):
        idict = Dict()
        idict[key_start + "key"] = "PYTEST"


@pytest.mark.xfail(reason="IndigoServer doesn't enforce this")
@pytest.mark.parametrize("key", ["XML", "xml", "Xml"])
def test_dict_xml_key_raises_runtime_error(key):
    with pytest.raises(
        RuntimeError,
        match="LowLevelBadParameterError -- illegal XML tag name character",
    ):
        idict = Dict()
        idict[key] = "PYTEST"


@pytest.mark.parametrize("value", PRIMITIVE_VALUES)
def test_dict_set_primitive_value(value):
    idict = Dict()
    idict["test"] = value

    assert idict["test"] == value


@pytest.mark.parametrize("value", [[], [1, "two", False], {"one": 1, "two": [1, 2, 3]}])
def test_dict_set_container_values(value):
    idict = Dict()
    idict["test"] = value

    assert idict["test"] == value


@pytest.mark.parametrize(
    "value",
    [
        [Exception(), "two", False],
        {"one": 1, "two": [1, Exception(), 3]},
        [[[[[Exception()]]]]],
        {"key": {"key": {"key": Exception()}}},
    ],
)
def test_dict_complex_container_values_raises_type_error(value):
    idict = Dict()
    with pytest.raises(TypeError):
        idict["test"] = value


def test_dict_to_dict():
    idict = Dict()
    idict["key"] = 5
    result = idict.to_dict()

    assert result == {"key": 5}


def test_dict_values_return_copy():
    outer = Dict()
    outer["a"] = 1

    inner = Dict()
    inner["a"] = 1
    inner["b"] = 2

    outer["d2"] = inner

    assert outer["d2"] is not inner
