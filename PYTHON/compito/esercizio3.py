stringa:str = str(input("Inserisci una stringa: "))
reversed_str:str = ""

for i in stringa:
    reversed_str = i + reversed_str

print(reversed_str)