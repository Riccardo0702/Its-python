from mytypes import *
from enum import *
from typing import Any
from typing import Self
from datetime import *

class Facoltà():
    _nome: str #noto alla nascita
    _tipo_facoltà: str #noto alla nascita

    def __init__(self, _nome: str, _tipo_facoltà: str):
        self.set_nome(_nome)
        self.set_tipo_facoltà(_tipo_facoltà)
    
    def set_nome(self, _nome):
        self._nome = _nome

    def set_tipo_facoltà(self, _tipo_facoltà):
        self._tipo_facoltà = _tipo_facoltà

    def get_nome(self):
        return self._nome 

    def get_tipo_facoltà(self):
        return self._tipo_facoltà

class Corsi():
    _nome: str #noto alla nascita
    _durata_in_ore: RealGEZ #noto alla nascita
    _codice: str #noto alla nascita

    def __init__(self, _nome: str, _durata_in_ore: RealGEZ, _codice: str):
        self.set_nome(_nome)
        self.set_durata_in_ore(_durata_in_ore)
        self.set_codice(_codice)

    def set_nome(self, _nome):
        self._nome = _nome

    def set_durata_in_ore(self, _durata_in_ore):
        self._durata_in_ore = _durata_in_ore

    def set_codice(self, _codice):
        self._codice = _codice

    def get_nome(self):
        return self._nome 
    
    def get_durata_in_ore(self, _durata_in_ore):
        return self._durata_in_ore
    
    def get_codice(self, _codice):
        return _codice

class Studente:
    _nome: str #noto alla nascita
    _cod_Fisc: Cf #noto alla nascita
    _data_nascita: datetime #noto alla nascita <<immutable>>
    _anno_iscr: datetime #noto alla nascita <<immutable>>
    _num_matricola: str #noto alla nascita <<immutable>>
    _corsi_studenti: Corsi 

    def __init__(self, _nome: str, _cod_Fisc: Cf, _data_nascita: datetime, _anno_iscr: datetime, _num_matricola: str, _corsi_studenti: Corsi ):
        self.set_nome(_nome)
        self.set_cod_Fisc(_cod_Fisc)
        self._data_nascita = _data_nascita
        self._anno_iscr = _anno_iscr
        self._num_matricola = _num_matricola
        self.set_corsi_studenti(_corsi_studenti)
    
    def set_nome(self, _nome: str):
        self._nome = _nome

    def set_cod_Fisc(self, _cod_Fisc: str):
        self._cod_Fisc = _cod_Fisc

    def set_corsi_studenti(self, _corsi_studenti: Corsi):
        self._corsi_studenti = _corsi_studenti
    
    def get_nome(self):
        return self._nome 
    
    def get_cod_Fisc(self):
        return self._cod_Fisc
    
    def get_anno_iscr(self):
        return self._anno_iscr
    
    def get_num_matricola(self):
        return self._num_matricola
    
    def get_corsi_studenti(self):
        return self._corsi_studenti
    
class Professori:
    _nome: str #noto alla nascita
    _cod_Fisc: Cf #noto alla nascita
    _data_nascita: datetime #noto alla nascita <<immutable>>
    _corsi_prof: Corsi

    def __init__(self, _nome: str, _cod_Fisc: Cf, _data_nascita: datetime, _corsi_prof: Corsi):
        self.set_nome(_nome)
        self.set_cod_Fisc(_cod_Fisc)
        self._data_nascita = _data_nascita
        self.set_corsi_prof = _corsi_prof
    
    def set_nome(self, _nome: str):
        self._nome = _nome

    def set_cod_Fisc(self, _cod_Fisc: str):
        self._cod_Fisc = _cod_Fisc
    
    def set_corsi_prof(self, _corsi_prof: Corsi):
        self._corsi_prof = _corsi_prof
    
    def get_nome(self):
        return self._nome 
    
    def get_cod_Fisc(self):
        return self._cod_Fisc
    
    def get_corsi_prof(self):
        return self._corsi_prof
    
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

class Regione:
    _nome:str #noto alla nascità

    def __init__(self, nome:str) -> None:
        self.set_nome(nome)

    def nome(self) -> str:
        return self._nome
    
    def set_nome(self, nome:str) -> None:
        self._nome:str = nome

class corso_superato_studente:
    _voto: Voto #noto alla nascita <<immutable>>

    def __init__(self, _voto: Voto):
        self._voto = _voto

    def get_voto(self):
        return self._voto