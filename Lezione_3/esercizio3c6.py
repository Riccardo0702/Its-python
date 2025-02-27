''' Modificare il codice dell'esercizio 3C-4, affinchè si possa scrivere un codice python che consenta all'utente di inserire il nome di un animale ed un habitat. Quando il codice dell'esercizo 3C-4 classifica l'animale inserito in una delle categorie tra mammiferi, rettili, uccelli o pesci, oltre a mostrare un messaggio a schermo, deve salvare tale categoria in una variabile animal_type. Se l'animale inserito non è classificabile in una delle quattro categorie proposte, il valore di animal_type sarà ' "unknown".

Inserire, poi, in un dizionario il nome dell'animale, la categoria a cui esso appartiene (animal_type) e l'habitat.

Verificare con un match statement se l'animale e la categoria a cui esso appartiene possano vivere nell'habitat inserito; dunque, verificare:
- se l'animale può vivere nell'habitat specificato, stampare un messaggio appropriato.
- se l'habitat non è compatibile con l'habitat specificato, stampare un avviso.
- Se l'animale o l'habitat non sono riconosciuti, stampare un messaggio di errore.

Le categorie di classificazione devono essere:
- Mammiferi: cane, gatto, cavallo, elefante, leone, balena, delfino.
- Rettili: serpente, lucertola, tartaruga, coccodrillo.
- Uccelli: aquila, pappagallo, gufo, falco, cigno, anatra, gallina, tacchino.
- Pesci: squalo, trota, salmone, carpa.

Categorie di habitat:
- acqua
- aria
- terra'''


'''animale = str(input("Inserisci un animale: "))
habitat = str(input("Inserisci habitat: "))

mammiferi = ["cane", "gatto", "cavallo", "elefante", "leone", "balena", "delfino"]
rettili = ["serpente", "lucertola", "tartaruga", "coccodrillo"]
uccelli = ["aquila", "pappagallo", "gufo", "falco", "cigno", "anatra", "gallina", "tacchino"]
pesci = ["squalo", "trota", "salmone", "carpa"]

terra = ["cane", "gatto", "cavallo", "elefante", "leone", "serpente", "lucertola", "tartaruga", "coccodrillo", "gallina", "tacchino"]
aria = ["aquila", "pappagallo", "gufo", "falco"]
acqua = ["squalo", "trota", "salmone", "carpa", "cigno", "anatra", "balena", "delfino"]

info_animale = {"nome": animale, "categoria dell'animale": animal_type, "habitat": habitat}
match animale:
    case animale if animale in mammiferi:
        print("Questo animale appartiene alla categoria dei mammiferi.")
        animal_type = "mammiferi"
    case animale if animale in rettili:
        print("Questo animale appartiene alla categoria dei rettili.")
        animal_type = "rettili"
    case animale if animale in uccelli:
        print("Questo animale appartiene alla categoria degli uccelli.")
        animal_type = "uccelli"
    case animale if animale in pesci:
        print("Questo animale appartiene alla categoria dei pesci.")
        animal_type = "pesci"
    case _:
        print(f"Non so dire in quale categoria classificare l'animale {animale}")
        animal_type = "unknown"

match animale:
    case animale if animale in mammiferi and terra:
        print(f"Il mammifero {animale} vive sulla terra")
    case animale if animale in mammiferi and acqua:
        print(f"Il mammifero {animale} vive in acqua")
    case animale if animale in rettili and terra:
        print(f"Il rettile {animale} vive sulla terra")
    case animale if animale in rettili and acqua:
        print(f"Il rettile {animale} vive in acqua")
    case animale if animale in uccelli and terra:
        print(f"L'uccello {animale} vive sulla terra")
    case animale if animale in uccelli and aria:
        print(f"L'uccello {animale} vive nell'aria")
    case animale if animale in pesci and acqua:
        print(f"Il pesce {animale} vive nell'acqua")
    case _:
        print("Non riesco ad associare questo animale ad un habitat specifico") '''


mammiferi:list =["cane", "gatto", "cavallo", "elefante", "leone", "balena", "delfino"]
rettili:list =["serpente", "lucertola", "tartaruga", "coccodrillo"]
uccelli:list =["aquila", "pappagallo", "gufo", "falco", "cigno", "anatra", "gallina", "tacchino"]
pesci:list =["squalo", "trota", "salmone", "carpa", "delfino"]
acqua: list =["squalo", "trota", "salmone", "carpa", "delfino"]
terra: list =["cane", "gatto", "cavallo", "elefante", "leone", "serpente", "lucertola", "tartaruga", "coccodrillo", "aquila", "pappagallo", "gufo", "falco", "cigno", "anatra", "gallina", "tacchino"]
aria: list =["aquila", "pappagallo", "gufo", "falco",  "anatra"]

animal_type = "Unknown"

animale= str(input("Inserisci animale "))
habitat= str(input("Inserisci habitat "))

match animale:
    case animale if animale in mammiferi:
        animal_type = "mammiferi"
    case animale if animale in rettili:
        animal_type = "rettili"
    case animale if animale in uccelli:
        animal_type = "uccelli"
    case animale if animale in pesci:
        animal_type = "pesci"
    case _:
        print("non va bene")

animale_info: dict ={"nome": animale, "tipo_animale": animal_type, "habitat": habitat}

match animale_info:
    case animale_info if animale_info["habitat"]=="terra" and animale_info["nome"] in terra and animale_info["tipo_animale"] == "mammiferi":
        print(f"{animale} è uno dei mammiferi che vive sulla terra")
    case animale_info if animale_info["habitat"]=="aria" and animale_info["nome"] in aria and animale_info["tipo_animale"] == "uccelli":
        print(f"{animale} è uno dei uccelli che vive in aria")
    case animale_info if animale_info["habitat"]=="acqua" and animale_info["nome"] in acqua and animale_info["tipo_animale"] == "pesci":
        print(f"{animale} è uno dei pesci che vive nell'acqua")
    case animale_info if animale_info["habitat"]=="terra" and animale_info["nome"] in terra and animale_info["tipo_animale"] == "rettili":
        print(f"{animale} è uno dei rettili che vive sulla terra")
    case animale_info if animale_info["habitat"]=="terra" and animale_info["nome"] in terra and animale_info["tipo_animale"] == "uccelli":
        print(f"{animale} è uno degli uccelli che vive sulla terra")
    case animale_info if animale_info["habitat"]=="acqua" and animale_info["nome"] in acqua and animale_info["tipo_animale"] == "mammiferi":
        print(f"{animale} è uno dei mammiferi che vive in acqua")
    case _:
        print("Non sono in grado di associare questo animale ad un habitat specifico")