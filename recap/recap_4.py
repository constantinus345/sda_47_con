from recap.configs import numar_de_ghicit
print(numar_de_ghicit)

numar_ghicit_user = input("Ghiceste un numar de la 1 la 1000 = ")

#o singura incercare
if numar_ghicit_user.strip().isdigit():
    #strp ne elimina spatiile goale din extremitatile string-ului
    if str(numar_ghicit_user) == str(numar_de_ghicit):
        print("Ai ghicit corect")
    else:
        print("Nu ai ghicit, ghinion")
else:
    print("Numarul nu e int sau transformabil in int")

# a = "hello ce   faci"
# b = "   hello ce faci  "
# print(a.strip()) #hello ce   faci
# print(b.strip()) #hello ce faci

# for i in range(3):
#     if numar_ghicit_user.strip().isdigit():
#         # strp ne elimina spatiile goale din extremitatile string-ului
#         if str(numar_ghicit_user) == str(numar_de_ghicit):
#             print("Ai ghicit corect")
#         else:
#             print("Nu ai ghicit, ghinion")
#     else:
#         print("Numarul nu e int sau transformabil in int")
#Principiul DRY = do not repeat yourself
#cand suntem nevoiti sa dam des copy-paste la cod, mai bine scriem o functie

def ghicit_sau_aproape(numar_ghicit_de_user, numar_de_ghicit_f):

    if numar_ghicit_de_user.strip().isdigit():
        # strp ne elimina spatiile goale din extremitatile string-ului
        if str(numar_ghicit_de_user) == str(numar_de_ghicit_f):
            print("Ai ghicit corect")
        else:
            if abs(int(numar_ghicit_de_user) - int(numar_de_ghicit_f)) > 50:
                print("Esti foarte departe")
            elif abs(int(numar_ghicit_de_user) - int(numar_de_ghicit_f)) > 10:
                print("Esti aproape")
            elif abs(int(numar_ghicit_de_user) - int(numar_de_ghicit_f)) >= 1:
                print("Esti foarte foarte aproape")
    else:
        print("Numarul nu e int sau transformabil in int")

numar_ghicit_user = input("Ghiceste un numar de la 1 la 1000 = ")
ghicit_sau_aproape(numar_ghicit_user, numar_de_ghicit)

#refactoring (schimbam) functia ghicit_sau_aproape ca sa fie mai pythonic, corect dpv al stilului

def guess_or_code_v2(user_guess, target_nr):
    user_guess = str(user_guess.strip())
    try:
        user_guess = int(user_guess)
        target_nr = int(target_nr)
        diferenta = abs(user_guess - target_nr)
        #abs insamna valoare absoluta, adica abs(-4) = abs(4) = 4
    except Exception as e:
        print(f"Valorile nu sunt valide, eroare = {e}")
        return None
        # tot ce e mai departe va fi ignorat daca valoarea introdusa nu e valida,
        # gen "44", "  77" etc

    # daca a ajuns codul pana aici, inseamna ca user_guess.isdigit() = True
    if user_guess == target_nr:
        print(f"Ai ghicit, bravo, numarul este = {target_nr}")
        return True
    elif diferenta > 50:
        print("Esti foarte departe")
    elif diferenta > 10:
        print("Esti aproape")
    else:
        print("Esti foarte foarte aproape")

numar_ghicit_user = input("Ghiceste un numar de la 1 la 1000 = ")
print("Acum v_1:")
ghicit_sau_aproape(numar_ghicit_user, numar_de_ghicit)
print("Acum v_2")
guess_or_code_v2(numar_ghicit_user, numar_de_ghicit)

#dam utilizatorului un  numar limitat de incercari
for i in range(4):
    numar_ghicit_user = input("Ghiceste un numar de la 1 la 1000 = ")
    if guess_or_code_v2(numar_ghicit_user, numar_de_ghicit):
        break

#numar nelimitat de incercari, pana ghiceste
while True:
    #while True se executa la infinit, daca nu o stopam la un break
    numar_ghicit_user = input("Ghiceste un numar de la 1 la 1000 = ")
    if guess_or_code_v2(numar_ghicit_user, numar_de_ghicit):
        print("bravo")
        break

