import random
import math

percentuale_mosse = random.randint(1, 10)
traguardo = 70
posizione_t:int = 1
posizione_l:int = 1



def posizione_gara(posizione_t:int = 1, posizione_l:int = 1):
    print("BANG !!!!! AND THEY'RE OFF !!!!!")
    while True:

        percorso = ["_"] * 70
        posizione_t = mossa_t(posizione_t)
        posizione_l = mossa_l(posizione_l)
        percorso[posizione_t - 1] = "T"
        percorso[posizione_l-1] = "H" 

        print(*percorso)
        if posizione_t == posizione_l:
            print("OUCH!!!")
        elif posizione_t >= traguardo and posizione_l >= traguardo:
            print("E' un pareggio")
            break
        elif posizione_t >= traguardo:
            print("TORTOISE WINS!||VAY!!!")
            break
        else:
            print("HAE WINS || YUCH!!!")
            break   
        
    

    


def mossa_t(posizione_t:int):
    n = random.randint(1, 5)
    if n == range(1, 5): 
        posizione_t += 3
    elif n == range(6,7):
        posizione_t -=6
        if posizione_t < 0:
            posizione_t = 0
    else:    
        posizione_t += 1
    return min(posizione_t, 70)
           
    

def mossa_l(posizione_l:int):
    n = random.randint(1,2)
    if n == range(1, 2):
        posizione_l = posizione_l
    elif n == range(3, 4):
        posizione_l += 9
    elif n == 5:
        posizione_l -= 12
        if posizione_l< 0:
            posizione_l = 0
    elif n == range(6, 7, 8):
        posizione_l += 1
    else:
        posizione_l -= 2
        if posizione_l < 0:
            posizione_l = 0
    return min(posizione_l, 70)




posizione_gara(1,1)









