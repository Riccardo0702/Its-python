'''  Scrivere un programma in Python che memorizzi il nome, il ruolo e l'età di un utente in un dizionario. 
Il nome, il ruolo e l'età devono essere inseriti in input dall'utente stesso. 
Il programma deve determinare il livello di accesso ai servizi in base al ruolo e all'età dell'utente secondo questo schema:

- Admin → "Accesso completo a tutte le funzionalità."
- Moderatore → "Può gestire i contenuti ma non modificare le impostazioni."
- Utente adulto (età ≥ 18) → "Accesso standard a tutti i servizi."
- Utente minorenne (età < 18) → "Accesso limitato! Alcune funzionalità sono bloccate."
- Ospite → "Accesso ristretto! Solo visualizzazione dei contenuti."
- Ruolo non riconosciuto → "Attenzione! Ruolo non riconsciuto! Accesso Negato!"


nome = str(input("Inserisci il nome: "))
ruolo = str(input("Inserisci il ruolo: "))
età = int(input("Inserisci l'età: "))

match ruolo:
    case ruolo if ruolo == "Admin":
        print(f"L'utente {nome} ha accesso completo a tutte le funzionalità")
    case ruolo if ruolo == "Moderatore":
        print(f"L'utente {nome} può gestire i contenuti ma non modificare le impostazioni")
    case ruolo if ruolo == "Ospite":
        print(f"L'utente {nome} ha accesso ristretto! Solo visualizzazione dei contenuti.")
    case ruolo if ruolo == "Utente":
        if età >= 18:
            print(f"L'utente {nome} ha accesso standard a tutti i servizi.")
        else:
            print(f"L'utente {nome} ha accesso limitato! Alcune funzionalità sono bloccate.")
    case _:
        print("Attenzione! Ruolo non riconsciuto! Accesso Negato!")'''

utente: dict= { "nome":str(input("Inserire il nome utente: ")), "ruolo" : str(input("Inserire il ruolo: ")), "età" : int(input("Inserite l'età: "))} 

match utente:


    case utente if utente["ruolo"] == "admin":
        print("Accesso completo a tutte le funzionalità")
    
    case utente if utente["ruolo"] == "moderatore":
        print("Può gestire i contenuti ma non modificare le impostazioni")
    
    case utente if utente["ruolo"] == "ospite":
        print("Accesso ristretto! Solo visualizzazione dei contenuti")
    
    case utente if utente["ruolo"] != ["admin", "moderatore","ospite"]:
        print ("Attenzione! Ruolo non riconsciuto! Accesso Negato!") 
  
    case utente if utente["età"] >= 18:
        print("Accesso standard a tutti i servizi") 
    
    case utente if utente["età"] < 18:
        print("Accesso limitato! Alcune funzionalità sono bloccate")


