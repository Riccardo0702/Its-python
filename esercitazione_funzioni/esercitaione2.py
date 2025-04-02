def rounded_average(numbers: list[int]) -> int:
    somma_n = 0
    for n in numbers:
        somma_n += n
    media = (somma_n)/ len(numbers)
    return round(media) 

print(rounded_average([1, 1, 2, 2]))