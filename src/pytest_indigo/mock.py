from pytest_indigo.indigo import Data, Dict, List

class IndigoMock:
    def __init__(self):
        self.reset()

    def reset(self):
        self.Dict = Dict
        self.List = List

        self.data = Data()