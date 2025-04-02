def build_profile(nome, cognome, età, capelli, peso):
    return print(f"{nome}, {cognome}, {età}, {capelli}, {peso}")

nome = input("Inserisci il tuo nome: ")
cognome = input("Inserisci il tuo cognome: ")
età = int(input("Inserisci la tua età: "))
capelli = input("Inserisci il colore dei tuoi capelli: ")
peso = int(input("Inserisci il tuo peso: "))

build_profile(nome, cognome, età, capelli, peso)
print(build_profile)