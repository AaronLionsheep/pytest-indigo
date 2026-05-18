from pytest_indigo import indigo
from pytest_indigo.indigo.data import Data

def test_data():
    data = Data()
    data.set("x", 5)

    assert data.get("x") == 5

def test_data_is_attr():
    assert isinstance(indigo.data, Data)