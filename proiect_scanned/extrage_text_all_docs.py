from access_docs import full_path_docs
#full_path_docs imi returneaza toate fisierele ce trebuie prelucrate
from extrage_text import save_extratected_text_to_txt
from configs import folder_docs
import asyncio

list_of_files = full_path_docs(folder_docs)
# print(list_of_files)

for file in list_of_files:
    try:
        save_extratected_text_to_txt(file)
    except Exception as e:
        print(f"Eroare = {e}")