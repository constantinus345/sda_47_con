import requests
import json

country = 'Japan'
url = f"https://restcountries.com/v3.1/name/{country}"
raspuns = requests.get(url)
date_primite = raspuns.json()[0]

date_primite_pretty = json.dumps(date_primite, indent=2)

print(date_primite_pretty)
# print(type(date_primite))

nume_tara = date_primite['name']['official']
capitala = date_primite['capital'][0]
population = date_primite['population']

print(nume_tara)
print(capitala)
print(population)

#transformati acest script intr-o functie de gen get_info_about_country(any_country_name)
#returneaza un dictionar cu cheile> nume_tara, timezones, suprafata, masina_side_rorl


