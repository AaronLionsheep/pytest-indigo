import pytest

from pytest_indigo import IndigoMock
from pytest_indigo.exceptions import NotImplementedException
from pytest_indigo.warnings import PartiallyImplementedWarning


# MARK: Partially implemented
@pytest.mark.parametrize("method", ["getDependencies", "getGroupList"])
def test_partially_implemented(indigo: IndigoMock, method):
    with pytest.warns(
        PartiallyImplementedWarning,
        match=(
            rf"^indigo\.device\.commands\.{method} has only been partially implemented "
            r"by pytest-indigo! An empty list is always returned\.$"
        ),
    ):
        assert getattr(indigo.device, method)(1) == []


# MARK: Not implemented
@pytest.mark.parametrize("method", ["x10ChangeAddress", "x10ChangeModel"])
def test_not_implemented(indigo: IndigoMock, method):
    with pytest.raises(
        NotImplementedException,
        match=rf"^indigo\.device\.commands\.{method} has not been implemented by pytest-indigo!$",
    ):
        getattr(indigo.device, method)(1, "A1")
