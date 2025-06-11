oggetti = []
i = 1

while i <= 3:
    oggetto = str(input("Inserisci un oggetto: "))
    i += 1
    oggetti.append(oggetto)
print(oggetti)

for i in range(3):
    x = oggetti[i]
match x:
    case x if x in ["penna", "matita", "quaderno"]:
        print("Materiale scolastico")
    case x if x in ["pane", "latte", "uova"]:
        print("Prodotti alimentari")
    case x if x in ["sedia", "tavolo", "armadio"]:
        print("Mobili")
    case x if x in ["telefono", "computer", "tablet"]:
        print("Dispositivi elettronici")
    case _:
        print("Categoria sconosciuta")