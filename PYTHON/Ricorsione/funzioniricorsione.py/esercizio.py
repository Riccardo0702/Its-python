def countdown(n:int) -> None:
    if n < 0:
        print("Errore! Il valore n deve essere positivo!")
    elif n == 0:
        print(0)
    else:
        print(n)
        countdown(n-1)
        
countdown(5)
