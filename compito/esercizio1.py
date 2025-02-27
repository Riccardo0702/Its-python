while True:
    parola:str = str(input("Inserisci una parola: "))
    if parola == "fine":
        print("fine esecuzione")
        break
    else:
        if parola[0] == parola[len(parola) - 1]:
            print("Primo e ultimo carattere uguali")

