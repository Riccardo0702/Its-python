#while

'''MAX = int(input("Inserisci un valore massimo: "))
cont = 1

while cont < 4:
    cont += 1
    n = int(input("Inserisci un valore n: "))
    if n > MAX:
        MAX = n
    else:
        continue
print(f"Il valore massimo è: {MAX}")'''

#repeat

MAX = int(input("Inserisci un valore massimo: "))
cont = 1

while True:
    n = int(input("Inserisci un valore n: "))
    if n > MAX:
        MAX = n
    cont += 1
    if cont == 4:
        break
print(f"Il valore massimo è: {MAX}")
     

#ciclo for

'''MAX = int(input("Inserisci un valore massimo: "))

for i in range (3):
    n = int(input("Inserisci un valore n: "))
    if n > MAX:
        MAX = n
    else:
        continue
print(f"Il valore massimo è: {MAX}")'''