numeri:list = []
i:int = 0
x:int = 0
asterisco:str = ""

while i < 5:
    n:int = int(input("Inserisci un numero compreso tra 1 e 30: "))
    if n < 1 and n > 30:
        print("Devi inserire un numero compreso tra 1 e 30")
        continue
    else:
        numeri.append(n)
        i += 1

for n in numeri:
    while x < n:
        asterisco = asterisco + "*"
        x += 1
    print(asterisco)