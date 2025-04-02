n_tutor = 10
attesa = 0
studente = input("Inserisci lo studente: ")
while True:
    if n_tutor > 0:
        n_tutor += 1
        print("Tutor assegnato con successo")
    else:
        attesa += 1
        print("Studente in attesa")

    if n_tutor == 0 and attesa > 50:
        break

if n_tutor == 0 and attesa > 50:
    print("Il processo è terminato")