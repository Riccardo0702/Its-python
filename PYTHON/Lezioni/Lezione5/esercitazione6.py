def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
    if conditionA == True or (conditionB == True and conditionC == True):
        return "Operazione permessa"
    else:
        return "Operazione negata"

print(check_combination(True, False, True))