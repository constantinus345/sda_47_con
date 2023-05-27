#seturile sunt mult mai eficiente in operatiunile de apartenenta, x in set

set_1 = {1,2,3}
list_1 = [1,2,3]
# 1 in set_1 va fi mai rapid decat 1 in list_1, mai ales cand avem multe elemente.

from time import perf_counter #pentru a calcula performanta in timp a unor operatiuni
from random import randint, choices
import string #pentru a crea cuvinte cu caractere aleatorii
from sys import getsizeof #pentru a vedea cata memorie ocupa un obiect, in bytes
def list_random_size(size):
    random_strings = []
    for i in range(size):
        string_length = randint(3,9)
        rand_string = ''.join(choices(string.ascii_letters, k=string_length))
        random_strings.append(rand_string)
    return random_strings

lisx_1 = list_random_size(10**6)
element_random = lisx_1[10**6 - randint(100, 10**5)]
#randint(100, 10**5) returneaza un numar aleatoriu intre 100 si 100.000
print(element_random)
setx_1 = set(lisx_1)

time_start_1 = perf_counter()
#? perf_counter returneaza numarul de secunde de la deschiderea calculatorului (nu-s sigur, ceva de genu)
if element_random in lisx_1:
    print(f"{element_random} in lisx_1")
time_lisx = perf_counter() - time_start_1
print(f"For x in list took = {time_lisx} secunde")

time_start_2 = perf_counter()
if element_random in setx_1:
    print(f"{element_random} in set_1")
time_setx = perf_counter() - time_start_2
print(f"For x in set took = {time_setx} secunde")
print(f"{time_lisx//time_setx} faster is x in set than x in list")

memorie_lista = getsizeof(lisx_1)
memorie_set = getsizeof(setx_1)
print(f"lista are {memorie_lista} bytes, set are {memorie_set} bytes, lista are cu {memorie_lista- memorie_set} mai mult")