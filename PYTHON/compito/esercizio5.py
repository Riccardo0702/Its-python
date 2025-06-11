denaro:int = int(input("Inserire euro "))
tot_barrette:int = 0
buono_sconto:int = 0

while denaro > 0:
    tot_barrette += 1
    buono_sconto += 1

    if buono_sconto == 6:
        buono_sconto = 0
        tot_barrette += 1
    
    denaro -= 1

print(f"Hai preso {tot_barrette} barrette e sono rimasti {buono_sconto} buoni sconto")