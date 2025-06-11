'''class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
alice = Person("Alice W.", 45)
bob = Person("Bob M.", 36)

if alice.age > bob.age:
    print(alice.age)
else:
    print(bob.age)

persona1 = Person("persona 1.", 22)
persona2 = Person("persona 3.", 44)
persona3 = Person("persona 3.", 66)

people = [alice, bob, persona1, persona2, persona3]

giovane = people[0]

for person in people:
    if person.age < giovane.age:
        giovane.age = person.age

print(giovane.age)

class student: 
    def __init__(self, name:str, studyProgram:str):
        self.name = name
        
        self.studyProgram = studyProgram
        

    def printInfo(self):
        print(f" Il nome è {self.name} e il corso di studi è {self.studyProgram}")

riccardo = student("Riccardo", "Cyber security")
nicolas = student("nicolas", "Cyber security")
valerio = student("valerio", "Cyber security")

riccardo.printInfo()
nicolas.printInfo()
valerio.printInfo()'''

'''#esercizio3

class animal:
    def __init__(self, nome:str, zampe:int):
        self.nome = nome
        self.zampe = zampe

    def printInfo(self):
        print(f"L'animale è {self.nome} e possiede {self.zampe} zampe")
    
    def setLegs(self):
        self.zampe = int(input("Inserisci la nuova quantità di zampe: "))
    def getLegs(self):
        print(f"Le zampe dell'animale {self.nome} sono state cambiate, adesso sono {self.zampe}")

cane = animal("Cane", 4)

cane.printInfo()

cane.setLegs()

cane.getLegs()

cane = animal("Cane", 4)
cane.printInfo()

cane.zampe = 5'''


#esercizio4

class food:
    def __init__(self, nome:str, price:int, description: str):
        self.nome = nome
        self.price = price
        self.description = description
    def printInfo():
        print(f"Il cibo è {self.nome}, il prezzo è: {self.price} ed è composto da {self.description}")

margherita = food("Margherita", 5.50, "Pomodoro, Mozzarella")
kebab = food("Kebab", 6.50, "piadina, kebab, insalata, pomodoro, patatine, picanto")
gelato = food("Gelato", 5.50, "Cioccolato")




        
