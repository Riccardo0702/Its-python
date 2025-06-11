
a = int(input("Inserisci un valore numerico per a: "))
b = int(input("Inserisci un valore numerico per b: "))

if a > b:
    c = (a**2-b**2)**0.5
    print(f"Il valore di c è: {c}")
else:
    print("Errore")