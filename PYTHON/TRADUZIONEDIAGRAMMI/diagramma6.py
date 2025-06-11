while True: 
    n = int(input("Inserisci un numero: "))
    if n < 0:
        print("Hai inserito un numero negativo. Inserisci un numero positivo")
    else: 
        fattoriale = 1
    i = 1

    fattoriale = 1
    for i in range(1, n + 1):
        fattoriale *= i

    print(f"Il fattoriale di {n} è: {fattoriale}")
    
    

