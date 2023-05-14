import requests
import json

def str_from_list(listx):
    """
    daca listx este ['ab','cd','gh']
    returneaza un string 'ab, cd, gh'
    un fel de functie ajutatoare, utils
    """
    return ", ".join(listx)

def get_info_about_country(any_country_name):

    url = f"https://restcountries.com/v3.1/name/{any_country_name}"
    #am creat url cu variabila any_country_name, poate fi accesat si de pe browser
    raspuns = requests.get(url)
    date_primite = raspuns.json()[0]
    print(date_primite)
    #am primit ca rezultat un fisier json/ dictionar

    #nume_tara, timezones, suprafata, masina_side_rorl
    dictionar = dict()
    #am creat un dictionar gol prin dict(), echivalent cu dictionar = {}
    dictionar['nume_tara'] = date_primite['name']['official']
    #pentru cheia nume_tara am dat valoarea scoasa din json
    dictionar['timezones'] = str_from_list(date_primite['timezones'])
    dictionar['suprafata'] = int(date_primite["area"])
    dictionar['masina_side_rorl'] = date_primite['car']['side']
    #am returnat dictionarul construit prin metoda de mai sus
    return  dictionar

dictionar_rezultat = get_info_about_country("Romania")
#am apelat functia cu o variabila de nume de tara

strx_frum = f"""{dictionar_rezultat['nume_tara']} 
                are suprafata {dictionar_rezultat['suprafata']} km2,
                are timezones {dictionar_rezultat['timezones']},
                iar masinile conduc pe partea {dictionar_rezultat['masina_side_rorl']}""".replace("  ","")
#am creat un string cu valorile prezente in dictionarul dictionar_rezultat
#functia replace(prima_variabila, doua_variabila) inlocuieste prima_variabila cu doua_variabila
print(strx_frum)

#transformati acest script intr-o functie de gen get_info_about_country(any_country_name)
#returneaza un dictionar cu cheile> nume_tara, timezones, suprafata, masina_side_rorl

