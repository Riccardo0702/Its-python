def numero_magico(num:int) -> bool:
    if num%4=0 and num%6!=0:
        print(f"Il numero {num} è magico!")
    else:
        print(f"Il numero {num} non è magico")


print(numero_magico(8))