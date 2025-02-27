nome = str(input("Inserisci il tuo nome:"))
genere = str(input("Inserisci il tuo genere. Digitare 'm' per Maschio o 'f' per Femmina: "))
match genere:
    case "m":
        print(f"Nome: {nome}, Genere: Maschio")
    case "f":
        print(f"Nome: {nome}, Genere: Femmina")
    case _:
        print("Errore nell'inserimento del genere. Impossibile generare un documento.")