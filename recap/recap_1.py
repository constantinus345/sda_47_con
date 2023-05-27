#python beginner
a = ["12"]
print(type(a))
if isinstance(a, int):
    print('is integer')
elif isinstance(a,float):
    print("is float")
elif isinstance(a, str):
    print("is string")
elif isinstance(a, list):
    print("is list")
else:
    print("None of the int, float or str")

listx = ["1", 1, 1.1, "sapte"]
#fiti atenti la denumirea variabilelor, modulelor, functiilor sa nu fie cuvinte cheie

#pentru a accesa fiecare element din lista prin iteratie>
for valoare in listx:
    #f-strings ne ofera posibilitatea de a ingloba variabile in strings
    print(f"{valoare} este de tip {type(valoare)}")

for index, valoare in enumerate(listx):
    #enumerate ne ofera posibilitatea sa iteram pe o lista, cu accesarea index si valorii
    print(f"{valoare} este de tip {type(valoare)}, e al {index+1} element")

#daca vrem sa editam in mai multe locuri in acelasi timp, click pe locatie avand apasat "alt"

print(list(enumerate(listx)))

c_1 = "ceva"
c_2 = 'ceva'
c_3 = """ceva
        aici
        hello
        """.replace(" "*4, "")
#replace(old_string, new_string) inlocuieste un string vechi cu unul nou
print(c_3)

#operatiuni cu strings
#daca un substring este prezent intr-un string
strx_1 = "Elevii de la SDA sunt elevi faini. Elevatia muntelui Everest este > 8000 m si e un munte fainle"
substring_1 = "le"
if substring_1 in strx_1:
    print(f"{substring_1} in strx_1")
else:
    print(f"{substring_1} NOT in strx_1")

count_substring = strx_1.count(substring_1)
print(f"{substring_1} de {count_substring} in strx_1")

print(strx_1.replace("Everest", "Kilimanjaro"))

strx_2 = "cE maI FACI?"
print(strx_2.lower()) #ce mai faci?
print(strx_2.upper()) #CE MAI FACI?
print(strx_2.capitalize()) #Ce mai faci?

for letter in strx_2:
    print(letter, end= "++")
    #end ne ofera posibilitatea sa schimbam ce se intampla dupa print, default= newline, \n

print("Ce mai \nfaci?")
#va printa cum e mai jos, pentru ca \n se duce pe linie noua
#Ce mai
# faci?

a = True #nu true, nu va functiona
print(a, type(a))
b = False #nu "false"
print(b, type(b))

c = 5 > 7
print(c, type(c)) #False <class 'bool'>
#putem da unei valori o propozitie logica, care va fi de tip boolean True or False

d = "le" in "Elevii mei sunt cei mai buni"
print(d, type(d)) #True <class 'bool'>

if c:
    print("se va executa (inclusiv) daca valoarea lui c este True")

ay = 0
by = None
cy = ""
dy = 4
ey = []
fy = [2]
if ay:
    print(ay) #valoarea 0 este considerata False
if by:
    print(by) #valoarea Null este considerata False
if cy:
    print(cy) #valoarea "" -empty string- este considerata False
if dy:
    print(dy) #valorile intregi <>0 sunt considerate True
if ey:
    print(ey) #valoarea [] este considerata False
if fy:
    print(fy) #valoarea unei liste cu 1+ elemente este considerata True
#acest bloc va printa doar 4 si [2] pentru celelalte valori sunt considerate False in Python.

a = True
b = False
print(a and b) #True and False = False
print(a or b) #True or False = True

n = '8'
print(int(n), type(int(n))) #8 <class 'int'>
m = 'opt'
print(int(m), type(int(m))) #ValueError: invalid literal for int() with base 10: 'opt'
print(isinstance(n, int)) #False, pentru ca '8' e string
print(n.isdigit()) #verifica daca un string este convertibil in integer

print(m.startswith("o")) #verifica daca string-ul m se incepe cu "o"
print(m.startswith("p"))
print(m.endswith("o"))
print(m.endswith("t")) #verifica daca string-ul m se termina cu "t"

strx_4 = 'Ce mai face Ion si Maria'
print(strx_4[3]) #al 4-lea element din string
print(strx_4[3:15]) #extrage substring-ul de la al 4-lea caracter pana la al 14-lea inclusiv

a = '7'
b = 7
print(a*3) # '777'
print(b*3) # 21

#python este un limbaj weakly typed, nu trebuie sa declaram tipurile de date

#Conventii in python
class CamelCaseExample:
    pass #conventie de denumire a claselor, sn CamelCase

def snake_case_example():
    pass #conventie de denumire a functiilor, sn snake_case

#is vs ==
a = [1,2,3,4]
b = list(range(1, 5))
print(f"a = {a}, b = {b}")
print(a == b) #True, au aceiasi valoare
print(a is b) #False, pentru ca nu sunt aceleasi obiecte, nu impart acelasi spatiu de memorie
#analogia cu doua oua foarte similare- ambele sunt aprox la fel, dar sunt totusi 2 oua diferite

"""
Aici e un comentariu multi-line
Scriu o functie care calculeaza suma elementelor unei liste, fiecare inmultit cu x
Adica [1,2,3] suma elementelor inmultit cu 2 va fi = 1*2 + 2*2 + 3*2 = 12
Voi face o functie in care folosesc type hints
"""

def multiplicare_multiplicator(x :int, lista: list[float]) -> float:
    """
    :param x: voi primi un integer
    :param lista: voi primi o lista cu numere rationale float
    :return: un  numar rational
    """
    rez = 0
    for el in lista:
        rez += el*x # echivalent cu rez = rez + el*x

    return rez

lix = [1,2,3,4]
x = 2.2
print(multiplicare_multiplicator(2, lix))

#type-hinting in python este ca o sugestie nu o constrangere
#exista programe care testeaza daca typing-ul (tipul elementelor - int, str, list etc) este respectat
#ex> pylint, pyflakes, mypy etc.
#type-hinting poate ajuta la debugging si inclisv evitarea bug-urilor
#valid din versiunea 3.5 al python

#operatori, assignment and equality check

#+ , - , *, /
#**, //, %
print(3**3) #27, adica 3 la puterea 3
print(19//7) #2, adica impartirea fara rest 19 la 7
print(19 % 7) #5, adica restul impartirii 19 la 7

print(3 == 4)
print(3 != 4) #!= not equal
print(3 < 4)
print(3 >= 4)
print(3 <= 4)

a = 3
a = a + 3
print(a)
a += 3 #echivalent cu a = a + 3
print(a)
a **= 2 #a va fi ridicat la patrat, echivalent cu a = a**2, sau a = a*a
print(a)

text_path = 'B:/Dropbox/SDA/Python_47/abc.txt' #path Unix
#Pentru copierea rapida a path-urilor in Windows, de tip Unix, folosesc https://pathcopycopy.github.io/
folder = r'B:\Dropbox\nSDA\Python_47' #path windows, necesar r"", adica raw string


folder_1 = r'B:\Dropbox\nSDA\Python_47' #r este raw string, nu interpreteaza caracterele speciale precum \n
folder_2 = 'B:\Dropbox\nSDA\Python_47' #\n va fi interpretat ca newline
print(folder_1)
print(folder_2)


text_path = 'B:/Dropbox/SDA/Python_47/abc.txt' #path Unix
#pentru a citi dintr-un fisier txt>
with open(text_path, 'r') as alias_fisier:
    print(alias_fisier.read())
#'r' inseamna read, operatiunea de citire din fisier

ceva_text = '\nce mai faci?'
with open(text_path, 'a') as f:
    #'a' este operatiune de append, adauga la fiserul existent
    f.write(ceva_text)

ceva_text_nou = 'Hello lady'
with open(text_path, 'w') as file:
    #'w' este operatiune de scriere, DAR scrie din nou, adica sterge tot ce era in fisier si apoi scrie
    file.write(ceva_text_nou)

a, b = 5, 7 #declarare de variabile pe aceiasi linie, adica a = 5, b= 7
str_f = f"Valorile sunt {a} si {b}"
print(str_f)
#alternativa la f-strings
str_format = "Valorile sunt {} si {}".format(a,b)
print(str_format)

lisx = ["1", 2, 3.4, [5, [8,9], 6], (11, 12, 23)]
print(f"Lista are {len(lisx)} elemente")
print(lisx[3][1][0]) #8, accesarea elementelor din nested lists, liste in liste

lisx.append(7)
print(lisx)
lisx.append([1,2,3]) #adauga lista ca singur element  ...7, [1, 2, 3]]
print(lisx)
lisx.extend([11,12,13]) #adauga fiecare element din lista ...7, [1, 2, 3], 11, 12, 13]
print(lisx)

lisx.insert(1, 'abc') #a inserat 'abc' la pozitia/indexul 1
print(lisx) #['1', 'abc', 2, 3.4,...

print(lisx[::-1]) #va printa lista in ordine inversa
lisx.pop(2) #scoate elementul de la indexul 2
print(lisx)

lisx.remove(3.4) #elimina un element dupa valoarea sa, nu dupa index ca pop
print(lisx)

#pericol- argument default lista la functie
def add_element_power_2(el, listx = []):
    listx.append(el**2)
    return listx

print(add_element_power_2(3)) #expected [9], got [9]
print(add_element_power_2(4)) #expected [16], got [9,16], unexpected behaviour

def add_element_power_2_v2(el, listx = None):
    if listx is None:
        listx = []
    listx.append(el**2)
    return listx

print(add_element_power_2_v2(3)) #expected [9], got as expected
print(add_element_power_2_v2(4)) #expected [16], got as expected

lisx = [1,2,3]
lisx[1] = 19
print(lisx)

tupx = (1,2,3)
tupx[1] = 19
print(tupx) #tuple este immutable, metaforic - tuple este un fel de lista in beton
#lista este mutable, putem sa schimbam valorile, pe cand la tuple -NU!

#initializare tuple
#incorect
tupx = (1)
print(tupx, type(tupx))

#corect, cu un singur element
tupx = (1,)
print(tupx, type(tupx))

#corect, fara nici un element
tupx = tuple() #tupx = () nu este valid
print(tupx, type(tupx))

def puterile(a,b,c):
    return a**2, b**3, c**4

ax = puterile(3,4,5)
print(ax, type(ax)) #functiile la return -> tuple

#set
#nu sunt ordonate, au elemente unice
some_set = {16, 1,2,3,2,3,3,3,3,4,5,6,13, 7,2,3}
print(some_set) #nu e garantat ca vor fi in o oarecare ordine, ex crescator

lisx = [16, 1,2,3,2,3,3,3,3,4,5,6,13, 7,2,3, 198]
print(lisx)
print(set(lisx))


