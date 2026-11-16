import pytest

import pytest_indigo
from pytest_indigo.exceptions import (
    ApiVersionException,
    NotImplementedException,
    PytestIndigoException,
)
from pytest_indigo.warnings import PartiallyImplementedWarning


@pytest.mark.parametrize("exception", [ApiVersionException, NotImplementedException])
def test_exceptions_are_pytest_indigo_exceptions(exception):
    assert issubclass(exception, PytestIndigoException)


def test_pytest_indigo_exception_exported():
    assert pytest_indigo.PytestIndigoException is PytestIndigoException


def test_partially_implemented_warning_is_user_warning():
    assert issubclass(PartiallyImplementedWarning, UserWarning)
