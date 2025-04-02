max_posti = int(input("inserisci il numero massimo dei posti: "))
liberi = max_posti
while True:
    opzione = input("Scegli un opzione tra: ingresso, uscita, stato, esci ")

    match opzione:
        case "ingresso":
            if liberi > 0:
                liberi -= 1
                print(f"Il numero dei liberi è diminuito a: {liberi}")
            else:
                print("Non ci sono posti disponibili")
        case "uscita":
            if liberi < max_posti:
                liberi += 1
            else:
                print("Tutti i posti sono già disponibili")
        case "visualizza":
            print(liberi)
            print(max_posti - liberi)
        case "esci":
            print("Uscita dal sistema")
            break
        case _:
            print("Opzione inserita non valida")
        