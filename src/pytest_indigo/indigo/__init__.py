from .base import ElemKey as ElemKey
from .collections import Dict as Dict
from .collections import List as List


class kProtocol(int):
    Insteon: "kProtocol"
    X10 = 1
    ZWave = 2
    Plugin = 3
