def countdown(n:int) -> None:
    if n >= 0:
        while n:
            print(n)
            n -= 1
            
    else:
        print("Errore! Il valore n deve essere positivo.")

countdown(5)
countdown(-5)

