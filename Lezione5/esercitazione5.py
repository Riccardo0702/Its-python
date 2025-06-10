def sum_above_threshold(numbers: list[int], threshold: int) -> int:
    if threshold % 1 == 0: 
        for n in numbers:
            if n > threshold:
                sum = 0
                sum += n
        return sum
            

 	