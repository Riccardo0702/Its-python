def conversione(list_tuple:list[tuple]) -> dict:
    dict =  {}
    for key, value in list_tuple:
        if key in dict:
            dict[key] += value
        else:
            dict[key] = value 
    return dict

lista = [("a", 1), ("b", 2), ("c", 3), ("a", 3)]
print(conversione(lista))
