
def add_2_v1(a,b):
    return a + b

add_2_v2 = lambda a, b: a+b
print(add_2_v1(3,4))
print(add_2_v2(3,4))

data = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}, {"name": "Bob2", "age": 22}]
#lambda se poate folosi in interiorul functiilor ca argument
#sorting values by a dictiory key
data.sort(key= lambda x: x["age"])
print(data)

par_sau_nu = lambda x: x % 2 == 0
print(par_sau_nu(7))
print(par_sau_nu(78))

unire_strings = lambda s1, s2: f"{s1} ---&--- {s2}"
print(unire_strings("Hello", "Ce mai faci?"))

listax = ['Ion', 'Vasile', 'Alexandru', 'Elena', 'Ana']
listax_sortata = sorted(listax, key = lambda x: len(x))
#am sortat lista dupa lungimea elementelor
print(listax_sortata)

divizibil_11 = [x for x in filter(lambda x: x%11==0, range(1, 112))]
#returneaza o lista cu elemente divizibile cu 11 dintr-un range stabilit
print(divizibil_11) #[11, 22, 33, 44, 55, 66, 77, 88, 99, 110]

listax = ['Ion', 'Vasile', 'Alexandru', 'Elena', 'Ana']
#creez o lista la care fiecare element este lower cu _abc
lista_noua = [x for x in map(lambda x : f"{x.lower()}_abc", listax)]
print(lista_noua)

listax = ['Ion', 'Vasile', 'Alexandru', 'Elena', 'Ana']
for el in listax:
    print(el)

listax_iter = iter(listax)
un_el = next(listax_iter)
print(un_el)

#creez 2 obiecte de la a la b, primul va fi lista (iterabil), al doilea va fi generator
def ab_v_lista(a,b):
    lisx = list()
    #lisx = []
    for x in range(a, b+1):
        lisx.append(x)
    return lisx

obiect_list = ab_v_lista(2,12)
print(obiect_list, type(obiect_list))

def ab_v_generator(a,b):
    for x in range(a, b+1):
        yield x

obiect_generator = ab_v_generator(2,12)
print(obiect_generator, type(obiect_generator))

for i in obiect_list:
    print(i, end="; ")
print("\n")
for j in obiect_generator:
    print(j, end="; ")

from sys import getsizeof
obiect_list_mare = ab_v_lista(2,10**6)
obiect_generator_mare = ab_v_generator(2,10**6)
print(f"Marimea obiect_list_mare = {getsizeof(obiect_list_mare)} bytes")
print(f"Marimea obiect_generator_mare = {getsizeof(obiect_generator_mare)} bytes")
print(f"Lista e de {getsizeof(obiect_list_mare)//getsizeof(obiect_generator_mare)} ori mai mare")
