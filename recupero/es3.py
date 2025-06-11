def numeri(dict:dict):
    new_dict = {}
    for key,value in dict.items():
        if value < 50:
            new_value = round(value +(value * 10/ 100), 2)
            new_dict[key] = [new_value]
    print(new_dict) 

numeri({"mela": 2.75, "merda": 500})

