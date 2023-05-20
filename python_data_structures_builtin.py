#int, float
a = 7
print(a, type(a))
b = 4.2
print(b, type(b))

#string
c = 'abc'
print(c, type(c))

#lista
#listele sunt mutable, adica putem sa schimbam valorile elementelor
#tipul de date in lista poate fi diferit, o combinatie de tipuri de date e posibila
l = [1,2,3]
print(l, type(l))
l[0] = 'abc'
print(l)

#dict
#dictionarele nu au cheile ordonate, adica nu putem accesa cheile dupa un index
dx = {"a":[1,2,3], "b": 2.3, "d": {"c":7}}
#cheile si valorile pot fi un mix de date, cheile pot fi string sau int
print(dx, type(dx))

#tuple, similar cu listele dar nu sunt mutable
tup = ('1',2, 3.4)
print(tup, type(tup))
#tup[0] = 'abc' #eroare, schimbarea elementelor functioneaza doar la liste
# print(tup[1])

#sets
#structura de date neordonata (nu putem accesa dupa index) cu date unice
setx = {1,2,3,4,2} #echivalent cu {1, 2, 3, 4}
print(setx, type(setx))
lisx = [1,2,1,2,3,54,2,1]
print(set(lisx))