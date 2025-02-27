x = int(input("Inserisci il valore di x: "))
y = int(input("Inserisci il valore di y: "))

punto = (x, y)
match punto:
    case (0, 0):
        print("Il punto si trova nell'origine.")
    case (x, 0):
        print("Il punto si trova sull'asse delle y")
    case (0, y):
        print("Il punto si trova sull'asse delle x")
    case (x, y) if x > 0 and y >0:
        print("Il punto si trova nel primo quadrante")
    case (x, y) if x < 0 and y >0:
        print("Il punto si trova nel secondo quadrante")
    case (x, y) if x < 0 and y <0:
        print("Il punto si trova nel terzo quadrante")
    case _:
        print("Il punto si trova nel quarto quadrante")


