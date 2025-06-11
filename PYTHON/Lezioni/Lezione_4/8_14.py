def make_car(nome, produttore, **args):
    auto={"Modello": nome, "Produttore": produttore, **args}
    return auto


nome=input("Nome modello: ")
produttore=input("Produttore: ")
dati={}
while True:
    altro=input("Vuoi aggiungere un altro dato? 'si' / 'no': ")
    if altro!="no":
        chiave=input("Nome della caratteristica che vuoi inserire: ")
        valore=input("Dato della caratteristica: ")
        dati[chiave]=valore
    else:
        break

auto=make_car(nome, produttore, **dati)
print("\n")
for chiave, valore in auto.items():
    print(chiave, valore, sep=': ')