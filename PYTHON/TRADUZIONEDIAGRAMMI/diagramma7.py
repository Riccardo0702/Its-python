pari = 0
dispari = 0
CONT = 0
for CONT in range(10):
    n = int(input("Inserisci un numero: "))
    if n % 2 == 0:
        pari += 1
    else:
        dispari += 1
    CONT += 1

print(f"I numeri pari sono: {pari}, mentre quelli dispari sono: {dispari}")
