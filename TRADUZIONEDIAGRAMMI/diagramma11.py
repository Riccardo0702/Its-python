liberi = 20
opzione = input("Scegli un opzione tra: prenota, libera, visualizza, esci ")
while True:
    match opzione:
        case "prenota":
            if liberi > 0:
                liberi -= 1
                print(f"Il numero dei liberi è diminuito a: {liberi}")
            else:
                print("Non ci sono posti disponibili")
        case "libera":
            if liberi < 20:
                liberi += 1
            else:
                print("Tutti i posti sono già disponibili")
        case "visualizza":
            print(liberi)
            print(20 - liberi)
        case "esci":
            print("Uscita dal sistema")
            break
        case _:
            print("Opzione inserita non valida")

            