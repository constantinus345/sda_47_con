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
folder = r'B:\Dropbox\SDA\Python_47' #path windows, necesar r"", adica raw string
