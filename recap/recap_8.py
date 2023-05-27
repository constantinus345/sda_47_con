#Serialisation

#date tabelare
import pandas as pd
#pip install openpyxl

datele = {"Nume":["Ion", "Elena"],
          "Varsta": [22, 23]}

tabel = pd.DataFrame(datele)
print(tabel)

Folder = 'B:/Dropbox/SDA/Python_47'
file_excel = f"{Folder}/tabel_1.xlsx"
tabel.to_excel(file_excel, index=0)

tabel_citit = pd.read_excel(file_excel)
print(tabel_citit)

tabel_citit_2 = pd.read_excel(file_excel, sheet_name="foaie_3")
print(tabel_citit_2)
tabel_citit_2.to_excel(f"{Folder}/tabel_2.xlsx", index=False)

#json
#fisierele json sunt ~aceleasi ca dictionarele in python
import json
contact = {"Nume": "Ionescu",
          "Prenume": "Ion",
          "Telefoane": {
              "personal": "+40445545",
              "business": "+46544842"
          },
          "adresa": {"Strada":{"Denumire":"St cel Mare",
                               "Numar":"14"},
                     "Oras":"Botosani"}}

print(f"contact este de tip {type(contact)}")
Folder = 'B:/Dropbox/SDA/Python_47'

file_name_json_1 = f"{Folder}/json_1.json"
with open(file_name_json_1, "w") as fx:
    json.dump(contact, fx)
    print(f"Scrierea in {file_name_json_1} a fost cu succes")

#json.load - pentru a citi datele din fisier
with open(file_name_json_1, "r") as fr:
    contact_citit = json.load(fr)

print(contact_citit)

#json dumps transforma un obiect json/dictionar intr-un string frumos formatat
#indent inseamna spatiile intre etaje
#pentru ca dumps sa functioneze corect, cheile trebuie sa fie type-str
contact_citit_frumos = json.dumps(contact_citit, indent=2)
print(contact_citit_frumos)

nr_strada = contact_citit["adresa"]["Strada"]["Numar"]
print(nr_strada)

print(type(contact_citit_frumos)) #str
#pentru a transforma un string valid in json/dictionar
#folosim json.loads
contact_citit_dict = json.loads(contact_citit_frumos)
print(type(contact_citit_dict))
print(contact_citit_dict)

