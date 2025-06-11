def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    dict3 = dict1.copy()
    for key, value in dict2.items():
        if key in dict3:
            dict3[key] += value
        else:
            dict3[key] = value


    return dict3

print(merge_dictionaries({'x': 5}, {'x': -5}))
