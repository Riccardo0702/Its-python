def sum_diagonale1(matrice: list[list[int]]) -> int:

    somma_diagonale1: int = 0
    posizione: int = 0

    for lista in matrice:
        somma_diagonale_primaria1 += lista[posizione]
        position += 1

    print (somma_diagonale1)
    return somma_diagonale1

def sum_diagonale2(matrice: list[list[int]]) -> int:

    somma_diagonale_2: int = 0
    posizione: int = len(matrice) - 1

    for lista in matrice:
        somma_diagonale_2 += lista[posizione]
        position -= 1

    print (somma_diagonale_2)
    return somma_diagonale_2

sum_diagonale1([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
sum_diagonale2([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

