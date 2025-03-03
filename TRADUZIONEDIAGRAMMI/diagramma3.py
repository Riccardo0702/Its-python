sum = 0
cont = 0

while True:
    n = float(input("Inserisci un valore n: "))
    if n > 0:
        sum = sum + n
    cont += 1
    if cont == 5:
        print(f"La somma dei numeri è: {sum}")