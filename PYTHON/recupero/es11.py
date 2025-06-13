from string import ascii_lowercase

def occorrenze(stringa: str) -> dict[str, int]:
    occorrenze_dict = {}
    parolefrase = stringa.lower().split()

    for parola in parolefrase:
        c_parola = ""
        for i in parola:
            if i in ascii_lowercase:
                c_parola += i

        if c_parola:
            if c_parola not in occorrenze_dict:
                occorrenze_dict[c_parola] = 1
            else:
                occorrenze_dict[c_parola] += 1

    print(occorrenze_dict)


occorrenze('Ciao Python, come va Python?')

    

