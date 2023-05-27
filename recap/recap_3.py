dictx = {"key_1": 1,
         "key_2": [1,2,3],
         3: {"key_nested_1": 3.4,
             "key_nested_2": "salut"}
         }

#accesarea valorilor din dictionar dupa chei
print(dictx[3]["key_nested_2"])

# iterarea pe dictionar
# dupa chei si valori
for key, value in dictx.items():
    print(f"Cheia {key} are valoarea {value}")

#doar iterare pe chei
for keyx in dictx.keys():
    print(f"Avem cheia {keyx}")

#doar iterare pe valori
for valx in dictx.values():
    print(f"Avem valoarea {valx}")

#pentru a initializa un dictionar gol
dict_1 = {}
print(dict_1, type(dict_1))
#modul recomandat de initializare este:
dict_2 = dict()
print(dict_2, type(dict_2))

#modul recomandat de initializare a unui set gol
set_1 = set()
print(set_1, type(set_1))

#pentru a scrie structura unui cod, putem folosi "pass" la functii si clase
#ca apoi sa le populam cu cod

def ceva_func(arg_1: int, arg_2: float, arg_3: str) -> str:
    pass

class CevaFunc:
    pass

class CevaFunc:
    def ceva_func_2(self):
        pass

