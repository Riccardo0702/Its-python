n:int = int(input("Inserisci un valore numerico n: "))
if n > 0:
    if n % 1 == 0:
        cont = 0
        i = 0
        while i <= 10:
            x:int = int(input("Inserisci un numero x: "))
            if x % n == 0:
                cont += 1
            i += 1
        print(f"Il contatore è {cont}")
    