from enum import * 
class Genere(StrEnum):
    uomo = auto()
    donna = auto()

print("__name__ all'interno di mytypes.py: " + __name__)

if __name__ == "__main__":

    print("Test di mytypes.py\n=========\n")
    print(Genere.uomo)
    print(Genere.donna)
    print(Genere.donna[:2])

    try:
        Genere.donna = 5
    except AttributeError as e:
        print("Non è possibile riassegnare il valore 'donna' del tipo Genere")
        print("\t" + str(e))
    except TypeError as e:
        print(str(e))
    except Exception as e:
        print(str(e))