import pytest

from pytest_indigo import IndigoMock


def test_fixture_returns_indigo_mock(indigo: IndigoMock):
    assert isinstance(indigo, IndigoMock)


@pytest.mark.xfail("indigo.devices not implemented yet")
def test_fixture_returns_clean_indigo(indigo: IndigoMock):
    # ids should start at 1
    assert indigo.ids.peek() == 1

    assert len(indigo.devices) == 0
