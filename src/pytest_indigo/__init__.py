import sys
from collections.abc import Generator

from pytest import fixture

from .mock import IndigoMock

indigo_mock = IndigoMock()
sys.modules["indigo"] = indigo_mock


@fixture(name="indigo")
def fixture_indigo() -> Generator[IndigoMock, None, None]:
    yield indigo_mock
    indigo_mock.reset()
