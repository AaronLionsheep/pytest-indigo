import pytest
import string

from pytest_indigo import IndigoMock


PRIMITIVE_VALUES = [None, True, False, 1.8, -7.5, 10, "", "pytest", list(), dict()]
COMPLEX_VALUES = [Exception("PYTEST"), object(), set([1, 2, 3])]


def test_list_init_primitive_values(indigo: IndigoMock):
    l = indigo.List(PRIMITIVE_VALUES)

    assert l == PRIMITIVE_VALUES

def test_list_get_by_index(indigo: IndigoMock):
    l = indigo.List("abcdefghijklmnopqrstuvwxyz")

    assert l[0] == "a"
    assert l[25] == "z"
    
@pytest.mark.parametrize("value", PRIMITIVE_VALUES)
def test_list_appends_primitive_values(indigo: IndigoMock, value):
    l = indigo.List(PRIMITIVE_VALUES)
    l.append(value)

    assert l == [*PRIMITIVE_VALUES, value]

def test_list_extends_primitive_values(indigo: IndigoMock):
    l = indigo.List(PRIMITIVE_VALUES)
    l.extend(PRIMITIVE_VALUES)

    assert l == [*PRIMITIVE_VALUES, *PRIMITIVE_VALUES]

@pytest.mark.parametrize("value", PRIMITIVE_VALUES)
def test_list_set_primitive_value(indigo: IndigoMock, value):
    l = indigo.List(["PYTEST"])
    l[0] = value

    assert l == [value]

def test_list_init_complex_values_raises_type_error(indigo: IndigoMock):
    with pytest.raises(TypeError):
        indigo.List(COMPLEX_VALUES)

@pytest.mark.parametrize("value", COMPLEX_VALUES)
def test_list_append_complex_values_raises_type_error(indigo: IndigoMock, value):
    l = indigo.List()
    with pytest.raises(TypeError):
        l.append(value)

def test_list_set_by_slice_raises_not_implemented_error(indigo: IndigoMock):
    l = indigo.List()
    with pytest.raises(NotImplementedError):
        l[5:] = [1, 2, 3, 4, 5, 6] # type: ignore

def test_list_get_by_slice_raises_not_implemented_error(indigo: IndigoMock):
    l = indigo.List()
    with pytest.raises(NotImplementedError):
        l[5:] # type: ignore

def test_list_to_list_simple(indigo: IndigoMock):
    l = indigo.List([1, 2, 3, 4, 5])

    assert l.to_list() == [1, 2, 3, 4, 5]

def test_list_to_list_converts_nested_lists_and_dicts(indigo: IndigoMock):
    l = indigo.List(
        [
            1,
            2,
            indigo.List([3, 4]),
            indigo.Dict({"5": 5, "6": 6, "7": indigo.List([8, 9])}),
            indigo.List([
                indigo.Dict({"10": 10, "11": 11}),
                indigo.Dict({"12": 12, "13": 13})
            ])
        ]
    )

    assert l.to_list() == [
        1,
        2,
        [3, 4],
        {"5": 5, "6": 6, "7": [8, 9]},
        [{"10": 10, "11": 11}, {"12": 12, "13": 13}]
    ]

def test_list_values_return_copy(indigo: IndigoMock):
    outer = indigo.List()
    inner = indigo.List([1, 2, 3])
    outer.append(inner)

    assert outer[0] == inner
    assert outer[0] is not inner

def test_dict_get_key(indigo: IndigoMock):
    d = indigo.Dict()
    d["key"] = 5

    assert d.get("key") == 5

def test_dict_get_missing_key_returns_none_by_default(indigo: IndigoMock):
    d = indigo.Dict()

    assert d.get("key") is None

def test_dict_get_missing_key_returns_default(indigo: IndigoMock):
    d = indigo.Dict()

    assert d.get("key", 5) == 5

@pytest.mark.parametrize("key", ["abc123", "one23", "a/2", "A-_m!@"])
def test_dict_keys(indigo: IndigoMock, key):
    d = indigo.Dict()
    d[key] = "PYTEST"

    assert d[key] == "PYTEST"

@pytest.mark.parametrize("key", [1, None, list()])
def test_dict_non_string_key_raises_type_error(indigo: IndigoMock, key):
    with pytest.raises(TypeError):
        d = indigo.Dict()
        d[key] = "PYTEST"

@pytest.mark.parametrize("key", [" ", "ab c"])
def test_dict_key_with_space_raises_runtime_error(indigo: IndigoMock, key):
    with pytest.raises(RuntimeError, match="LowLevelBadParameterError -- illegal XML tag name character"):
        d = indigo.Dict()
        d[key] = "PYTEST"

@pytest.mark.parametrize("key_start", list(string.digits + string.punctuation))
def test_dict_key_starting_with_number_or_character_raises_runtime_error(indigo: IndigoMock, key_start):
    with pytest.raises(RuntimeError, match="LowLevelBadParameterError -- illegal XML tag name character"):
        d = indigo.Dict()
        d[key_start + "key"] = "PYTEST"

@pytest.mark.xfail(reason="IndigoServer doesn't enforce this")
@pytest.mark.parametrize("key", ["XML", "xml", "Xml"])
def test_dict_xml_key_raises_runtime_error(indigo: IndigoMock, key):
    with pytest.raises(RuntimeError, match="LowLevelBadParameterError -- illegal XML tag name character"):
        d = indigo.Dict()
        d[key] = "PYTEST"

@pytest.mark.parametrize("value", PRIMITIVE_VALUES)
def test_dict_set_primitive_value(indigo: IndigoMock, value):
    d = indigo.Dict()
    d["test"] = value

    assert d["test"] == value

@pytest.mark.parametrize(
    "value",
    [
        [],
        [1, "two", False],
        {"one": 1, "two": [1, 2, 3]}
    ]
)
def test_dict_set_container_values(indigo: IndigoMock, value):
    d = indigo.Dict()
    d["test"] = value

    assert d["test"] == value

@pytest.mark.parametrize(
    "value",
    [
        [Exception(), "two", False],
        {"one": 1, "two": [1, Exception(), 3]},
        [[[[[Exception()]]]]],
        {"key": {"key": {"key": Exception()}}}
    ]
)
def test_dict_complex_container_values_raises_type_error(indigo: IndigoMock, value):
    d = indigo.Dict()
    with pytest.raises(TypeError):
        d["test"] = value

def test_dict_to_dict(indigo: IndigoMock):
    d = indigo.Dict()
    d["key"] = 5
    result = d.to_dict()

    assert result == {"key": 5}

def test_dict_values_return_copy(indigo: IndigoMock):
    d1 = indigo.Dict()
    d1["a"] = 1

    d2 = indigo.Dict()
    d2["a"] = 1
    d2["b"] = 2

    d1["d2"] = d2

    assert d1["d2"] is not d2