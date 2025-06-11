A:int = int(input("Inserisci il valore per A: "))
B:int = int(input("Inserisci il valore per B: "))

if A < B:
    if A > 0 and B > 0:
        if A % 1 == 0 and B % 1 == 0:
            sum = 0
            i = A
            while i <= B:
                sum += i
                i += 1
            print(f"La somma è {sum}")
        else:
            print("A e B devono essere interi")
    else:
        print("A e B devono essere positivi")
else:
    print("A deve essere minore di B")

