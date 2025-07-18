class Frazione:
    def __init__(self, numeratore:int, denominatore:int):
        self.set_numeratore(numeratore)
        self.set_denominatore(denominatore)

    def set_numeratore(self, numeratore):
        if isinstance(numeratore, int):
            self.__numeratore = numeratore
        else:
            self.__numeratore = 13
    
    def set_denominatore(self, denominatore):
        if isinstance(denominatore, int):
            self.__denominatore = denominatore
        else:
            self.__denominatore = 13
    
    def get_numeratore(self):
        return self.__numeratore
    
    def get_denominatore(self):
        return self.__denominatore
        
    def __str__(self) ->str:
        return f"{self.__numeratore}/{self.__denominatore}"

    def value(self) -> int:
        return round(self.__numeratore / self.__denominatore, 3)


    #esercizio 2
    def mcd(x:int, y:int) -> int:
        

f1 = Frazione(6, 3)

print(f1)
print(f1.value())

f2 = Frazione('c', 0)
print(f2)
print(f2.value())


    