from custom_types import *
from impiegato import *

class progetto:
    _nome: str
    _budget: RealGEZ
    _coinvolto: set[Impiegato]

    def __init__(self, _nome: str, _budget: RealGEZ):
        self.set_nome(_nome)
        self.set_budget(_budget)
        

    def set_nome(self, n: str) -> None:
        self._nome = n
        
    def set_budget(self, b:str) -> None:
        self._budget = b

    def set_coinvolto(self, c: set[Impiegato]) -> None:
        self._coinvolto = frozenset[c]

    def get_nome(self):
        return self._nome
    
    def get_budget(self):
        return self._budget
    
    def get_coinvolto(self):
        return set[self._coinvolto]