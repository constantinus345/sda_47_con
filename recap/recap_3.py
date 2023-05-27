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

#adaug o cheie si o valoare la dictionar
#se recomanda cheile sa fie de tip string
dict_2["cheia_mea_1"] = "ceva valoare"
print(dict_2)

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

dictx = {"key_1": 1,"key_2": [1,2,3], 3: {"key_nested_1": 3.4,"key_nested_2": "salut"}}
#pretty print dict
import json
#json.dumps transforma dictionarul intr-un string cu o reprezentare "frumoasa" a dictionarului
#mai usor de citit pentru ochiul uman
pretty_dict_string = json.dumps(dictx, indent=2)
print(dictx)
print(pretty_dict_string)

nume_prenume_varsta = (("Ion", "Ionescu", 27),
                       ("Vasile", "Vasilescu", 28),
                       ("Elena", "Ailenei", 29))

#dict comprehension pentru a crea un dictionar din nume_prenume_varsta
nume_prenume_varsta_dict = {prenume: varsta for prenume, nume, varsta in nume_prenume_varsta}
print(nume_prenume_varsta_dict)

old_dict = {"a":4, "b": 5, "c":7}
#creez un dictionar cu aceleasi chei dar valorile ridicate la patrat
new_dict = {key: value**2 for key, value in old_dict.items()}
print(new_dict)

#user_input
numele_tau = input("Cum te numesti? = ")
print(f"Incantat de cunostina {numele_tau}!")

numarul_tau = input("Zi un numar care il voi ridica ^2 = ")
print(numarul_tau, type(numarul_tau))
#calculez patratul acestui numar
# try:
#     numar_tau_patrat = int(numarul_tau) ** 2
#     print(f"Numarul tau ^2 = {numar_tau_patrat}")
# except Exception as e:
#     print(f"Avem eroare = {e}")

#varianta 2
if numarul_tau.isdigit():
    numar_tau_patrat = int(numarul_tau) ** 2
    print(f"Numarul tau ^2 = {numar_tau_patrat}")
else:
    print("Numarul dat nu e integer")

#functii cu numar nespecificat de argumente
def sumax(a, b):
    return a +b
print(sumax(3,7))

def sumax_multiple(*args):
    rez = 0
    for arg in args:
        if str(arg).isdigit():
            rez += int(arg)
    return rez
print(sumax_multiple(2,"trei",4,5))

#varianta mai eleganta
def sumax_multiple_v2(*args):
    #suma unei liste create prin metoda list comprehension
    return sum([arg for arg in args if str(arg).isdigit()])

print(sumax_multiple_v2(2,"trei",4,5))

lisx = [1,2,3]
print(sum(lisx))

#calculez suma elementelor integer din lista, eliminand elementele netransformabile in integer
lisy = [1,"doi","3",4]
sumay = sum([int(element) for element in lisy if str(element).isdigit()])
print(sumay) #=8

#valori nedeterminate sub forma cheie:valoare ca argumentele unei functii
def ceva_functie(**kwargs):
    for key, value in kwargs.items():
        print(key, ": ", value)

ceva_functie(unu = "cifra 1",
             doi = "cifra 2",
             hello = 'salut',
             buna = "buna ziua")
#ghilemelele "" si '' pot functiona impreuna, dar e bine estetic sa fim consistenti

#Estetica in scrierea de python
#https://peps.python.org/pep-0008/ - ghidul oficial de stil in python
#google's adice> https://google.github.io/styleguide/pyguide.html
#youtube> https://www.youtube.com/watch?v=woIkysZytSs&ab_channel=ArjanCodes
#""" e acceptabil estetic
str_multiline_1 = """
ceva 
scris aici
hello
"""
#nu se recomanda ' pentru multi-line string
str_multiline_2 = '''
ceva 
scris aici
hello
'''



# print(str(1) == str("1")) -> True
