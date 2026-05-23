from pytest import raises


def test_can_use_dict(indigo):
    data = indigo.Dict()
    data["test"] = True

    assert data.get("test") is True
    assert data["test"] is True