
#importam module din codul nostru
import configs
print(configs.numar_de_ghicit)

#sau
import recap.configs as confx #pot sa pun alias la ceea ce import
print(confx.numar_de_ghicit)

from configs import *
#* inseamna ca importa toate elementele din configs
print(numar_de_ghicit)

#import module built-in
import math
nr = 1
print(math.sin(nr)) #sinus al valorii 1

from math import sin, cos, pi
nr = 1
print(sin(1))
print(cos(1))
print(pi)

from math import sin as sinus
print(sinus(1))

#!!!!! evitati importarea tuturor modulelelor cu *
from math import * #code smell
#se vor importa toate modulele de math, e indicat sa importam doar ce avem nevoie
print(sqrt(25))

#restul modulelor care nu sunt built-in sau nu-s parte din proiect,
# le instalam cu pip install
#de exemplu pip install pandas
import pandas


