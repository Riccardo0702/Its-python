'''#8-3
def display_message(stringa: str):
    print(stringa)

string_1="Hello World"
display_message(string_1)


#8-2
def favorite_book(title: str):
    print(f"{title} è uno dei miei libri preferiti!")
    
libro=input("Qual è l'ultimo libro che hai letto?\n")
favorite_book(libro)

#8-3
def make_shirt(taglia: str, frase: str):
    print(taglia)
    print(frase)

taglia=input("Che taglia è la maglietta?")
frase=input("Quale frase vuoi stampata?")
print("------------")
print("Maglietta 1")
make_shirt(taglia, frase)
print("Maglietta 2")
make_shirt("S", "Forza Roma")

#8-4
def make_shirt(taglia: str, frase: str):
    print(taglia)
    print(frase)

taglia = input("Inserisci la taglia: ")
frase = input("Quale frase vuoi stampata?")
print("------------")
print("Maglietta 1")
make_shirt("Large", "I love python")
print("Maglietta 2")
make_shirt("Medium", "I love python")
print("Maglietta 3")
make_shirt(taglia, frase)

#8-5
def describe_city(city: str, country: str):
    print(city)

city1 = input("Inserisci la prima città: ")
country1 = "Italia"
city2 = input("Inserisci la seconda città: ")
country2 = input("Inserisci uno stato: ")
city3 = input("Inserisci la terza città: ")
country3 = input("Inserisci uno stato: ")

describe_city(city1, country1)
print(f"La città {city1} si trova in {country1}")
describe_city(city2, country2)
print(f"La città {city2} si trova in {country2}")
describe_city(city3, country3)
print(f"La città {city3} si trova in {country3}")

#8-6
def city_country(city: str, country: str):
    return f"{city}, {country}"


city1 = city_country("Santiago", "Chile")
city2 = city_country("Londra", "Inghilterra")
city3 = city_country("Roma", "Italia")

print(city1)
print(city2)
print(city3)


#8-7
def make_album(artist: str, album: str, num_song = None):
    album = {
        "artista": artist,
        "album": album}
    if num_song:
        album["num. songs"] = num_song
    return album
    

album1 = make_album("edoardo", "pizza", 20)
album2 = make_album("claudio", "prosciutto")
album3 = make_album("diego", "bresaola")
print(album1)
print(album2)
print(album3) 

#8-8
def make_album(artist: str, album: str, num_song = None):
    album = {"artista": artist,"album": album}
    if num_song:
        album["num_song"] = num_song
    return album

while True:
    artist = input("Inserisci l'artista: ")
    if artist == "q":
        break

    album = input("Inserisci il nome dell'album: ")
    if album == "q":
        break

    num_song = int(input("Inserisci il numero delle canzoni: "))
    if num_song == "q":
        break

    if num_song:
        album = make_album(artist, album, int(num_song))
    else:
        album = make_album(artist, album)
    print(album)

#8-9
list = ["Roma", "Lazio", "Inter", "Milan"]

def show_messages():
    i = 0
    for x in list:
        if i < len(list):
            print(list[0 + i])
            i += 1
        else:
            break

show_messages()

#8-10
list1 = ["Roma", "Lazio", "Inter", "Milan"]

def show_messages():
    for i in list1:
        print(i)
show_messages()

sent_messages = []
testo1 = list1[0]
testo2 = list1[1]
testo3 = list1[2]
testo4 = list1[3]

def send_messages(f"testo1": "{testo1}", testo2: "{testo2}", testo3: "{testo3}", testo4: {testo4}"):
    print(send_messages)
    for i in send_messages:
        sent_messages.append(i)
print(list1)
print(sent_messages)

#8-11
lista = ["Alessio", "Mario", "Valentino", "Mirko", "Alfio"]

sent_message=[]

def send_messages(*args):
    for i in args:
            print(i)
            sent_message.append(i)

send_messages("Alessio", "Mario", "Valentino", "Mirko", "Alfio")
print(lista)
print(sent_message)'''


        
