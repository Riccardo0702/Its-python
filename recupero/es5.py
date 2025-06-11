def moltiplicazione(list):
    threshold = 5
    numero = 1
    for n in list:
        if n < threshold:
            numero *= n
    return numero

print(moltiplicazione([1, 2, 3, 4, 6]))