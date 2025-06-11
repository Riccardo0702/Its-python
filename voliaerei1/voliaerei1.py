from enum import * 
from custom_types import IntGZ

class IntGg(int):

    def __new__(cls, v: int | float | str | bool | Self) -> Self:

        n: float = super().__new__(cls, v)

        if n > 1900:
            return n

        raise ValueError(f"Il numero inserito {v} è negativo!")
    
