#Esercizio 3-10
Ilike = ["Books", "Nature", "Animals", "Astronomy", "Juventus", "Fortine", "Sunflower", "Travel"]
print (*Ilike, sep = "\n")


Ilike.insert(3, "Food")
print(*Ilike)

Ilike.append("Marvel")
print(*Ilike)

Ilike.pop(3)
print(*Ilike)

del Ilike [5]
print(*Ilike)

Ilike1 = sorted (Ilike)
print(*Ilike1)
print (*Ilike [::-1])

Ilike.reverse()
print(*Ilike)

Ilike.sort()
print(*Ilike)

Ilike.sort(reverse = True)
print(*Ilike)