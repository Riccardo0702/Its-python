numeri:list = []
frequenza_numeri:dict = {}
numeri_max_frequenza:list = []
somma_p:int = 0
somma_d:int = 0
max_frequenza:int = 0
x:int = 0

while True:
    n:int = int(input("Inserisci un numero intero(0 per terminare): "))
    if n == 0:
        print("Inserimento finito")
        break
    else:
        numeri.append(n)

for i in numeri:
    if i % 2 == 0:
        somma_p += i
    else:
        somma_d += i
    x += 1
    if i in frequenza_numeri:
        frequenza_numeri[i] += 1
    else:
        frequenza_numeri[i] = 1

print(frequenza_numeri)

for key, value in frequenza_numeri.items():
    print(value)
    if value > max_frequenza:
        max_frequenza = value
        numeri_max_frequenza = [key]
    elif value == max_frequenza:
        numeri_max_frequenza.append(key)

media_d = somma_d / x
print(f"La somma dei numeri pari è {somma_p}")
print(f"La media dei numeri dispari è {media_d}")
print(f"Numero o numeri con più frequenza sono: {numeri_max_frequenza} ripetuti {max_frequenza}")