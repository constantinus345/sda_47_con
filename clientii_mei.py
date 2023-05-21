import pandas

client_1 = {"nume_prenume": "Ion Popescu",
            "canal_interes_id":"UCknLrEdhRCp1aegoMqRaCZg"}

client_2 = {"nume_prenume": "Alex K",
            "canal_interes_id":"UCvYRAY19-ld887bBZjCr_WQ"}

def create_excel_from_dicts(*dicts, path_to_excel):
    # *dicts inseamna ca va lua ca parametru un numar variabil de dictionare
    #lista_dict = [d for d in dicts]
    df = pandas.DataFrame(dicts)
    df.to_excel(path_to_excel, index=False)

#create_excel_from_dicts(client_1, client_2, path_to_excel = "clientii_mei.xlsx")

def read_excel(path_to_excel):
    df = pandas.read_excel(path_to_excel)
    #in variabila df am stocat un tabel citit din excel
    dict_clienti = {column: df[column].tolist() for column in df.columns}
    # dict_clienti = {"clienti_nume": df["nume_prenume"].tolist(),
    #                 "canal_interes_clienti": df["canal_interes_id"].tolist()}
    return dict_clienti

def add_column_to_excel(file_path, column_name, column_values):
    df = pandas.read_excel(file_path)
    df[column_name] = column_values
    df.to_excel(file_path, index=False)

if __name__ == "__main__":
    telegram_ids = [1727526004, 6099769056]
    #add_column_to_excel("clientii_mei.xlsx", "telegram_id", telegram_ids)
    datele_clientilor = read_excel("clientii_mei.xlsx")
    print(datele_clientilor)

