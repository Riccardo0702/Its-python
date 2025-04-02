#8-12

def lista_ingredienti(*args):
    for i in args:
        print(*i, sep = '\n')
print("Il panino 1 è composto da: ")
panino1 = ["prosciutto", "mozzarella", "pomodoro" ]
lista_ingredienti(panino1)

print("Il panino 2 è composto da: ")
panino2 = ["scamorza", "bresaola", "formaggio" ]
lista_ingredienti(panino2)

print("Il panino 3 è composto da: ")
panino3 = ["rucola", "salame", "insalata" ]
lista_ingredienti(panino3)