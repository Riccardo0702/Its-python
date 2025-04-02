def frequency_dict(elements: list) -> dict:
    frequenza = {}
    for item in elements:
        if item in frequenza:
            frequenza[item] += 1
        else:
            frequenza[item] = 1
    return frequenza

print(frequency_dict(['mela', 'banana', 'mela']))
    

