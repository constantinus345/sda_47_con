
links = ["http://www.anpm.ro/documents/16241/69085825/Ziua+Internationala+de+Actiune+pentru+Clima.pdf/379607d9-62fa-4642-8ed8-14c950a0172f",
         "http://www.anpm.ro/documents/16241/69085825/Ziua+Pasarilor+Migratoare.pdf/0bc4e3ea-f6ab-4ddc-9557-d9f573931642",
         "http://www.anpm.ro/documents/16241/2701245/comunicat.pdf/ff28465d-3036-44c7-a7a3-3e1ac7b9b5ab",
         "http://www.anpm.ro/documents/16241/69085825/Luna+Padurii+2023.pdf/7703ee4c-1415-4383-88d8-332a92d330d4",
         "http://www.anpm.ro/documents/16241/69085825/Ziua+mondiala+a+Zonelor+Umede.pdf/469cd5e5-7d8d-4287-912f-76b34cda4660"]

from urllib.request import urlretrieve
from configs import folder_docs
#scriu o functie care imi descarca aceste linkuri intr-un folder ca documente pdf

# link_test = links[1]
# path_pdf_test = f"{folder_docs}/doc_1.pdf"
# urlretrieve(link_test, path_pdf_test)

for index, link in enumerate(links):
    path_pdf = f"{folder_docs}/doc_{index+1}.pdf"
    print(f"Fisierul este in {path_pdf}, index = {index}")
    try:
        urlretrieve(link, path_pdf)
    except Exception as eroarea_mea:
        print(f"Avem o eroare = {eroarea_mea}")