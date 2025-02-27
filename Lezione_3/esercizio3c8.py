frase = str(input("Inserisci la frase: "))
lfrase = len(frase)

match frase:
    case frase if frase[-1] == "?" and lfrase % 2 == 0:
        print("si")
    case frase if frase[-1] == "?" and lfrase % 2 == 1:
        print("no")
    case frase if frase[-1] == "!":
        print("wow")
    case _:
        print(f"Tu dici {frase}")
