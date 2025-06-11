def liste(list):
    mydict: dict = {
        "positivi": [],
        "negativi": []
    }
    for i in list:
        if i > 0:
            mydict["positivi"].append(i)
        else:
            mydict["negativi"].append(i)
    return mydict

print(liste([-5, -1, 2, 3]))
