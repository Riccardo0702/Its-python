#esercizio 3c 00a
numnero_neonati = int(input("Il numero di neonati sono: "))
match numnero_neonati:
    case 1:
        print("Congratulazioni!")
    case 2:
        print("Wow! Gemelli!")
    case 3:
        print("Wow! Tre!")
    case 4:
        print("Mamma mia Quattro! Wow!")
    case 5:
        print("Incredibile! Cinque!")
    case _:
        print(f"Non ci credo! {numnero_neonati} bambini!")

