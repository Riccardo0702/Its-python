pi:float = 0
i:int = 1
x:int = 0

while True:
    if round(pi, 2) == 3.14:
        print(f"valore di 3.14 raggiunto. I termini necessari per raggiungerlo sono stati {x}")
        break
    else:
        pi = pi + (4/i)
        x += 1
        i += 2
        pi = pi - (4/i)
        x += 1
        i += 2

while True:
    if round(pi, 3) == 3.141:
        print(f"Valore di 3.141 raggiunto. I termini necessari per raggiungerlo sono stati {x}")
        break
    else:
        pi = pi + (4/i)
        x += 1
        i += 2
        pi = pi - (4/i)
        x += 1
        i += 2

while True:
    if round(pi, 4) == 3.1415:
        print(f"Valore di 3.1415 raggiunto. I termini necessari per raggiungerlo sono stati {x}")
        break
    else:
        pi = pi + (4/i)
        x += 1
        i += 2
        pi = pi - (4/i)
        x += 1
        i += 2

while True:
    if round(pi, 5) == 3.14159:
        print(f"Valore di 3.14159 raggiunto. I termini necessari per raggiungerlo sono stati {x}")
        break
    else:
        pi = pi + (4/i)
        x += 1
        i += 2
        pi = pi - (4/i)
        x += 1
        i += 2
