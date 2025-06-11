soglia = int(input("Inserisci un valore soglia: "))

CONT = 0
for CONT in range(7):
    n = int(input("Inserisci un valore numerico: "))
    if n > soglia:
        print(f"Il numero {n} è maggiore della soglia")
    
    CONT += 1


