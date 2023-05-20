import os

from configs import folder_docs

#functie care returneaza full path la fiecare fisier ce trebuie procesat
# for file in os.listdir(folder_docs):
#     print(file)

def full_path_docs(folder_cu_documente_pdf):
    #am scris list comprehension care returneaza full path a fisierelor care au extensia .pdf
    return [f"{folder_cu_documente_pdf}/{fisier}" for fisier in os.listdir(folder_cu_documente_pdf) if fisier.endswith(".pdf")]

# docs_pdfs = full_path_docs(folder_docs)
# for file in docs_pdfs:
#     print(file)