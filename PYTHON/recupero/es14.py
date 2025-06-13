def merge_intervals(intervalli: list[list[int]]):

    new_intervalli: list = []

    for intervallo in intervalli:
        intervallo_minore: int = 0
        intervallo_maggiore: int = 0
        if intervallo[0] > intervallo_minore:
           
           intervallo_minore = intervallo[0]

           new_intervalli.append(intervallo_minore)

        elif intervallo[-1] > intervallo_maggiore:

            intervallo_maggiore = intervallo[-1]

            new_intervalli.append(intervallo_maggiore)