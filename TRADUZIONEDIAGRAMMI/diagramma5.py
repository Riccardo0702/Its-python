#div < n
'''n = float(input("Inserisci un valore n: "))
if n < 2:
    print(f"Il numero {n} non è primo")
else:
    div = 2
    while div < n:
        if n % div == 0:
            print(f"Il numero {n} non è primo")
            break
        else:
            div += 1
    else:
        print(f"Il numero {n} è primo")'''


#div < radn
n = float(input("Inserisci un valore n: "))
if n < 2:
    print(f"Il numero {n} non è primo")
else:
    div = 2
    while div <= n**0.5:
        if n % div == 0:
            print(f"Il numero {n} non è primo")
            break
        else:
            div += 1
    else:
        print(f"Il numero {n} è primo")

