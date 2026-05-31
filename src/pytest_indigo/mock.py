from pytest_indigo.indigo import Dict, List
from types import ModuleType


class IndigoMock(ModuleType):
    def __init__(self):
        self.reset()

    def reset(self):
        self.Dict = Dict
        self.List = List
