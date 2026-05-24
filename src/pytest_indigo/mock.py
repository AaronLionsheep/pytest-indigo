from pytest_indigo.indigo import Dict, List


class IndigoMock:
    def __init__(self):
        self.reset()

    def reset(self):
        self.Dict = Dict
        self.List = List
