quanti=0
media=0
somma=0
risposta=""
while True:
    risposta=input("Vuoi inserire un voto? Digita 'SI' o 'NO'")
    if risposta == "SI":
        voto=int(input("Voto: "))
        if voto>0:
            somma += voto
            quanti += 1
    if risposta=="NO":
        break
media=somma/quanti
print(f"Hai inserito {quanti} voti e la media è {media:.2f}")