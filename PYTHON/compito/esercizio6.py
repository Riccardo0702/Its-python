n1:int = int(input("inserisci il primo numero: "))
n2:int = int(input("inserisci il secondo numero: "))
prodotto1:int = 1
prodotto2:int = 1

if n1 > n2:
    for i in range(n2, n1 + 1):
        prodotto1 *= i
    print(f"il prodotto tra i numeri tra {n2} e {n1} è {prodotto1}")
else:
    for i in range(n1, n2 + 1):
        prodotto2 *= i
    print(f"il prodotto tra i numeri tra {n1} e {n2} è {prodotto2}")