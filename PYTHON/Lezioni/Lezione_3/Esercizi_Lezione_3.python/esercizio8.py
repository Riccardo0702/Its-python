def count_isolated(numeri:int) -> int:
    count = 0
    for n in range(len(numeri)):
        if (n==0 or numeri[n]!= numeri[n-1]) and (n == len(numeri)-1 or numeri[n] != numeri[n+1]):
            count += 1
    return count


print(count_isolated([1, 2, 2, 3, 3, 3, 4]))













