from time import  perf_counter

def factorial_iterativ(n):
    i = 1
    s = 1
    while i <= n:
        s = s * i
        i += 1
        #aceasta e functia factorial implementata in mod clasic / iterativ
    # factorial(5) = 1*2*3*4*5, adica factorial(n) = n! e produsul de la 1 la n
    return s

def factorial_recursiv(n):
    if n == 0 or n == 1:
        return 1
    else:
        #aici functia s-a apelat pe ea insasi, = modul recursiv
        return n * factorial_recursiv(n-1)

n = 800
start_1 = perf_counter()
print(factorial_iterativ(n))
performanta_iterativ = perf_counter() - start_1 #timpul in secunde.milisecunde de executare a instructiunilor
print(f"factorial_iterativ cu n = {n} a rulat in {performanta_iterativ} secunde")

start_2 = perf_counter()
print(factorial_recursiv(n))
performanta_recursiv = perf_counter() - start_2
print(f"factorial_recursiv cu n = {n} a rulat in {performanta_recursiv} secunde")

#factorial recursiv este totusi performant, vedeti diferenta gigantica in recurenta pentru fibonacci
