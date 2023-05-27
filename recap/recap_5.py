# pass, continue, break
lisx = list(range(1, 13))
print("\npass :")
for x in lisx:
    if x % 3 == 0:
        pass
        # pass - nu are nici o influenta
    print(x, end = "; ")
print("\ncontinue :")
for x in lisx:
    if x % 3 == 0:
        continue #merge la urmatorul element din bucla, fara a executa codul de mai departe
    print(x, end = "; ")
print("\nbreak :")
for x in lisx:
    if x % 3 == 0:
        break #stopeaza imediat executarea buclei complet, si iese cu totul din bucla
    print(x, end = "; ")

