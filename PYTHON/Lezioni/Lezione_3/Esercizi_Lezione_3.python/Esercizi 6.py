#6-1
#  persona = {"Nome":"Mario", "Cognome":"Rossi", "Età":19, "Città":"Roma"}
#  nomeMario = persona ["Nome"] 
# cognomeRossi = persona["Cognome"] 
# etàMatteo = persona["Età"] 
# cittàMario = persona["Città"]

# print (nomeMario) 
# print (cognomeRoss
# print (etàMario
# print (cittàMario)

# #6-2
#  numeri = {"Giulia:8,"Riccardo":2,"Lorenzo":12,"Antonio":34,"Alice":15} 
# numeroLucia = numeri["Giulia"] 
# numeroClaudio = numeri["Riccardo"] 
# numeroDomenico = numeri["Lorenzo"] 
# numeroLorenzo = numeri["Antonio"] 
# numeroAntonio = numeri["Alice"]

# print ("Giulia",numeroGiulia) 
# print ("Riccardo",numeroRiccardo) 
# print ("Lorenzo",numeroLorenzo) 
# print ("Antonio",numeroAntonio) 
# print ("Alice",numeroAlice)

# #6-3
# programma = {"tupla":"Tuples are a data type in Python used to store an ordered sequence of elements", "integer":"Numbers without decimals. Can be positive or negative", "float":"Numbers with decimals. Can be positive or negative", "string":"Textual data, but really, can be any symbols as long as it’s in quotation marks (“ ” or ‘ ’)", "boolean":"Value that’s returned by logical operations. Can only be True or False"} 
# meantupla = programma ["tupla"] 
# meaninteger = programma ["integer"] 
# meanfloat = programma ["float"] 
# meanstring = programma ["string"] 
# meanboolean = programma ["boolean"] 

# print ("tupla\n",meantupla) 
# print ("integer\n",meaninteger) 
# print ("float\n",meanfloat) 
# print ("string\n",meanstring) 
# print ("boolean\n",meanboolean)
 
#6-7 
# persona2 = {"Nome": "Giulia", "Cognome": "Rossi", "Età": 22, "Città": "Roma"} 
# persona3 = {"Nome": "Luca", "Cognome": "Verdi", "Età": 25, "Città": "Milano"} 
# people = [persona, persona2, persona3] 
# for person in people: print(f"Nome: {person['Nome']}") 
    # print(f"Cognome: {person['Cognome']}") 
    # print(f"Età: {person['Età']}") 
    # print(f"Città: {person['Città']}") 

# #6-8 
# cane = {"kind":"labrador","owner":"Luca"} 
# gatto = {"kind":"gatto_siamese","owner":"Alberto"} 
# coniglio = {"kind":"coniglio_albino","owner":"Giada"} 
# pets = [cane, gatto, coniglio] 
# for animal in pets: 
    # print(f"kind: {animal['kind']}") 
    # print(f"owner: {animal['owner']}")
  
# #6-9
#  favorite_places = { 'Alice': ['Paris', 'Tokyo', 'New York'], 'Bob': ['Mount Everest', 'Grand Canyon'], 'Charlie': ['Rome', 'Berlin', 'Sydney', 'Barcelona'] } 
# for name, places in favorite_places.items():
    #  print(f"{name}") 
    
# for place in places: 
    # print(f" {place}")
 
#6-10
# numeri = { "Lucia": [10, 15, 20], "Claudio": [8, 7, 9], "Domenico": [2, 3], "Lorenzo": [22, 25, 30], "Antonio": [14, 18, 12] } 
# for person, numbers in numeri.items(): 
    # print(f"{person}") 
# for number in numbers: 
    # print(f"{number}")
  
#6-11
#  cities = { "New York": { "country": "USA", "population": "8.4 million", "fact": "New York City is known for its iconic landmarks like the Statue of Liberty and Times Square." }, "Tokyo": { "country": "Japan", "population": "14 million", "fact": "Tokyo is the largest metropolitan area in the world by population." }, "Paris": { "country": "France", "population": "2.1 million", "fact": "Paris is home to the famous Eiffel Tower and is known as the 'City of Light'." } } 
# for city, info in cities.items(): 
    # print(f"City: {city}") 
    # print(f" Country: {info['country']}") print(f" Population: {info['population']}") 
    # print(f" Fact: {info['fact']}")