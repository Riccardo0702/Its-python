#come andrebbe fatto l'esercizio
'''def sum(n:int) -> None:
    if n < 0:
        print("Errore! Il valore n deve essere positivo!")
        return None
    else:
        sum:int = 0
        while n > 0:
            sum += n
            n -=1
        return int(sum)

print(sum(9))'''

#come viene svolto col metodo ricorsivo
def recursiveSum(n:int) -> int:
    if n < 0:
        print("Errore! Il valore n deve essere positivo!")
        return None
    elif n == 0:
        return 0
    else:
        return int(n + recursiveSum(n-1))

print(recursiveSum(9))
