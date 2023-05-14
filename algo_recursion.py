from time import  perf_counter

#Sirul lui Fibonacci
#1, 1, 2, 3, 5, 8, 13...

def fibonaci_iterativ(n_th):
    # a = 1
    # b = 1
    #echivalent cu
    a, b = 1, 1 #delimitatorul de zecimale in python este ".". Am facut un assignment dublu

    #validare daca n_th este integer
    if not isinstance(n_th, int):
        return "Input invalid"

    #validare input
    if n_th <= 0:
        return "Input invalid"

    #primele doua elemente sunt mereu 1, 1
    if n_th in (1, 2):
        return 1
    else:
        for _ in range(3, n_th + 1):
            c = a + b
            a = b
            b = c
        return c

# print(fibonaci_iterativ(7))

def fibonaci_recursiv(n_th):
    # a = 1
    # b = 1
    #echivalent cu
    a, b = 1, 1 #delimitatorul de zecimale in python este ".". Am facut un assignment dublu

    #validare daca n_th este integer
    if not isinstance(n_th, int):
        return "Input invalid"

    #validare input
    if n_th <= 0:
        return "Input invalid"

    #primele doua elemente sunt mereu 1, 1
    if n_th in (1, 2):
        return 1
    else:
        return fibonaci_recursiv(n_th - 1) + fibonaci_recursiv(n_th - 2)

# print(fibonaci_recursiv(7))

n = 39
start_1 = perf_counter()
print(fibonaci_iterativ(n))
performanta_iterativ = perf_counter() - start_1 #timpul in secunde.milisecunde de executare a instructiunilor
print(f"factorial_iterativ cu n = {n} a rulat in {performanta_iterativ} secunde")

start_2 = perf_counter()
print(fibonaci_recursiv(n))
performanta_recursiv = perf_counter() - start_2
print(f"factorial_recursiv cu n = {n} a rulat in {performanta_recursiv} secunde")

print(f"Recursiv este de {round(performanta_recursiv/performanta_iterativ, 1)} ori mai incet pentru fibonacci cu n = {n}")
