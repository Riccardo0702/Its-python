a:list = [5, 11, 18, 16, 6]
b:list = [7, 21, 1, 33, 8]
c:list = []

for i in range(len(a)):
    c.append(a[i] + b[(len(b) - 1) - i])

print(c)