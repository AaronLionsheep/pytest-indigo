from pytest import raises

def test_data(indigo):
    indigo.data.set("x", 5)
    assert indigo.data.get("x") == 5

def test_data_is_empty(indigo):
    with raises(KeyError):
        indigo.data.get("x")

def test_can_use_dict(indigo):
    data = indigo.Dict()
    data["test"] = True

    assert data.get("test") is True
    assert data["test"] is True