from pytest_indigo.indigo import Dict, List
from pytest_indigo.indigo.ids import IndigoIds

from types import ModuleType


class IndigoMock(ModuleType):
    Dict = Dict
    List = List

    ids: IndigoIds

    def __init__(self):
        self.reset()

    def reset(self):
        self.ids = IndigoIds()
