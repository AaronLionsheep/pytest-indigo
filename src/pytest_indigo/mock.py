from pytest_indigo.indigo import Data

class IndigoMock:
    def __init__(self):
        self.reset()

    def reset(self):
        self.data = Data()