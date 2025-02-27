moneta = 1
testa = 0
croce = 0

while moneta <= 8:
    print(f"Lancio numero {moneta}")
    x = str(input("Inserisci il risultato: "))
    if x == "t":
        print("E' uscito testa!")
        testa += 1
    else:
        print("E' uscito croce!")
        croce += 1
    moneta += 1
print(f"Testa è uscito {testa} volte!")
print(f"Croce è uscito {croce} volte!")

percentuale_testa = testa/8*100
percentuale_croce = croce/8*100
print(f"La percentuale delle volte che è uscito testa è: {percentuale_testa}%")
print(f"La percentuale delle volte che è uscito croce è: {percentuale_croce}%")
