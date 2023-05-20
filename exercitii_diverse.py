import tabula
import pandas

pdf_path = 'B:/Dropbox/SDA/Python_47/Algos/extable.pdf'
excel_path_folder = 'B:\Dropbox\SDA\Python_47\Algos'

tabele = tabula.read_pdf(pdf_path, pages='all')

with pandas.ExcelWriter(f"{excel_path_folder}/excel_tabele_sda.xlsx") as writer:
    for index, tabel in enumerate(tabele):
        # print(tabel)
        # print("\n\n\n")
        tabel.to_excel(writer, sheet_name=f"tabel_{index+1}", index=False)

print("Executat cu succes")

