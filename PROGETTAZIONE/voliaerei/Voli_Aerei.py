from mytypes import IntGEZ, IntGC, IntGZ

class Compagnia:
    _nome:str #noto alla nascità
    _anno:IntGC #noto alla nascità <<immutable>>

    def __init__(self, nome:str, anno:IntGC) -> None:
        self.set_nome(nome)
        self._anno = anno

    def nome(self) -> str:
        return self._nome
    
    def anno(self) -> IntGC:
        return self._anno
    
    def set_nome(self, nome:str) -> None:
        self._nome:str = nome

class Volo:
    _codice:str #noto alla nascità <<immutable>>
    _durata:IntGZ #noto alla nascità <<immutable>>

    def __init__(self, codice:str, durata:IntGZ) -> None:
        self._codice = codice
        self._durata = durata

    def codice(self) -> str:
        return self._codice
    
    def durata(self) -> IntGZ:
        return self._durata
    
class Aeroporto:
    _codice:str #noto alla nascità
    _nome:str #noto alla nascità

    def __init__(self, codice:str, nome:str) -> None:
        self.set_codice(codice)
        self.set_nome(nome)

    def codice(self) -> str:
        return self._codice
    
    def nome(self) -> str:
        return self._nome
    
    def set_codice(self, codice:str) -> None:
        self._codice:str = codice

    def set_nome(self, nome:str) ->None:
        self._nome:str = nome

class Città:
    _nome:str #noto alla nascità
    _abitanti:IntGEZ #noto alla nascità

    def __init__(self, nome:str, abitanti:IntGEZ) -> None:
        self.set_nome(nome)
        self.set_abitanti(abitanti)

    def nome(self) -> str:
        return self._nome
    
    def abitanti(self) -> IntGEZ:
        return self._abitanti
    
    def set_nome(self, nome:str) -> None:
        self._nome:str = nome

    def set_abitanti(self, abitanti:IntGEZ) -> None:
        self._abitanti:IntGEZ = abitanti

class Nazione:
    _nome:str #noto alla nascità

    def __init__(self, nome:str) -> None:
        self.set_nome(nome)

    def nome(self) -> str:
        return self._nome
    
    def set_nome(self, nome:str) -> None:
        self._nome:str = nome



