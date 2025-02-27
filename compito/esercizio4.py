numeri:list = []
somma:int = 0
i:int = 0
media:float = 0

while True:
    n:float = float(input("Inserisci un numero: "))
    if n < 0:
        print("Numero negativo inserito. Fine esecuzione")
        break
    else:
        if n.is_integer() == True:
            somma = n + somma
            i = i + 1
        
        numeri.append(n)

media = somma / i
print(f"Il numero maggiore è {max(numeri)}, il numero minore è {min(numeri)} la media degli interi è {media}")