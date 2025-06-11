G = int(input("Inserisci il giorno: "))
M = str(input("Inserisci il mese: "))
data = (G, M)

match data:
    case data if G == 1 and M == "Gennaio":
        print("E' Capodanno!")
    case data if G == 14 and M == "Febbraio":
        print("E' San Valentino!")
    case data if G == 2 and M == "Giugno":
        print("E' festa della Repubblica Italiana")
    case data if G == 15 and M == "Agosto":
        print("E' Ferragosto!")
    case data if G == 31 and M == "Ottobre":
        print("E' Halloween!")
    case data if G == 25 and M == "Dicembre":
        print("E' Natale!")
    case _:
        print("Nessuna festività importante in questa data.")