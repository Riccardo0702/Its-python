def condizioni(x, y, z):
    if x > 0 and (y > 10 or z % 2 == 0):
        return "Azione permessa"
    else:
        return "Azione negata"
    
print(condizioni(2, 8, 3))
