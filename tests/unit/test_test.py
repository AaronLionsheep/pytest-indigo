from pytest_indigo import IndigoMock


def test_can_use_dict(indigo: IndigoMock):
    data = indigo.Dict()
    data["test"] = True

    assert data.get("test") is True
    assert data["test"] is True