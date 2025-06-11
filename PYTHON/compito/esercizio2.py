stringa:str = str(input("Inserisci una stringa: "))
S:int = 0

for i in stringa:
    if i == " ":
        S += 1

print(f"Nella stringa {stringa} ci sono {S} spazi")