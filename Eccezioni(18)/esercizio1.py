import math


def safe_sqrt(number:int):
    square = math.sqrt(number)
    if number < 0:
        raise Exception("ValueError: il numero inserito è negativo")
    print(square)


safe_sqrt(9)