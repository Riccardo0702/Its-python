def sumInRange(a:int, b:int) -> int:
    if a > b:
        c = a
        a = b
        b = c
    sum:int = 0
    while b>=a:
        sum = sum + b
        b = b -1
        return int(sum)
        
        

print(sumInRange(10, 15))
print(sumInRange(15, 10))