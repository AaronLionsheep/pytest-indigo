import pytest
import string

from pytest_indigo.indigo import Dict, List

def test_dict_get_key():
    d = Dict()
    d["key"] = 5

    assert d.get("key") == 5

def test_dict_get_missing_key_returns_none_by_default():
    d = Dict()

    assert d.get("key") is None

def test_dict_get_missing_key_returns_default():
    d = Dict()

    assert d.get("key", 5) == 5

@pytest.mark.parametrize("key", ["abc123", "one23", "a/2", "A-_m!@"])
def test_dict_accepts_valid_keys(key):
    d = Dict()
    d[key] = "PYTEST"

    assert d[key] == "PYTEST"

@pytest.mark.parametrize("key", [1, None, list()])
def test_dict_rejects_non_string_key(key):
    with pytest.raises(Exception):
        d = Dict()
        d[key] = "PYTEST"

@pytest.mark.parametrize("key", [" ", "ab c"])
def test_dict_rejects_key_with_space(key):
    with pytest.raises(RuntimeError, match="LowLevelBadParameterError -- illegal XML tag name character"):
        d = Dict()
        d[key] = "PYTEST"

@pytest.mark.parametrize("key_start", list(string.digits + string.punctuation))
def test_dict_rejects_key_starting_with_number_or_character(key_start):
    with pytest.raises(RuntimeError, match="LowLevelBadParameterError -- illegal XML tag name character"):
        d = Dict()
        d[key_start + "key"] = "PYTEST"

@pytest.mark.xfail(reason="IndigoServer doesn't enforce this")
@pytest.mark.parametrize("key", ["XML", "xml", "Xml"])
def test_dict_rejects_xml_key(key):
    with pytest.raises(RuntimeError, match="LowLevelBadParameterError -- illegal XML tag name character"):
        d = Dict()
        d[key] = "PYTEST"

def test_dict_to_dict():
    d = Dict()
    d["key"] = 5
    result = d.to_dict()

    assert result == {"key": 5}

def test_dict_values_return_copy():
    d1 = Dict()
    d1["a"] = 1

    d2 = Dict()
    d2["a"] = 1
    d2["b"] = 2

    d1["d2"] = d2

    assert d1["d2"] is not d2