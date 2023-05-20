#pip install pytesseract
import os

import pytesseract
from PIL import Image
#pip install PyMuPDF , se importa ca fitz (de ce? habar n-am)
import fitz
import  io
from configs import folder_docs, text_notificare, ids_telegram
from telegram_func import send_telegram_message
import asyncio

#scriu functie care imi ia ca argument un full file path of pdf
#returneaza textul extras
def extarct_text_from_pdf(full_pdf_path):
    """
    :param full_pdf_path: full path of a pdf document to extract text from
    :return: textul extras
    -- modul acesta e mai profesionist de a scrie documentatia unei functii, se numeste docstring
    """
    extracted_text_total = ""
    doc = fitz.open(full_pdf_path)
    for page in doc:
        imagine_pagina = page.get_pixmap(matrix=fitz.Matrix(2, 2), colorspace=fitz.csRGB, alpha=True)
        #pentru parametrii get_pixmap vedeti documentatia pe PyMuPDF
        img_data = imagine_pagina.tobytes()
        img = Image.open(io.BytesIO(img_data))
        text_pagina = pytesseract.image_to_string(img, lang='ron')
        #tesseract languages -> https://tesseract-ocr.github.io/tessdoc/Data-Files-in-different-versions.html
        extracted_text_total += text_pagina

    doc.close()
    return extracted_text_total

def save_extratected_text_to_txt(full_pdf_path):
    text_extracted = extarct_text_from_pdf(full_pdf_path)
    if text_notificare in text_extracted:
        mesaj = f"In documentul \n <b>{full_pdf_path}</b> a fost identificat string-ul \n<b>{text_notificare}</b>. \nMerci!"
        for id_t in ids_telegram:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(send_telegram_message(id_t, mesaj))


    text_full_path = full_pdf_path.replace(".pdf", ".txt")

    txt_files = [f"{folder_docs}/{file}" for file in os.listdir(folder_docs) if file.endswith(".txt")]
    if text_full_path in txt_files:
        print(f"fisierul {text_full_path} exista deja")
        return None
    # extrag textul dintr-un document pdf, si il salvez in txt in folder_docs
    with open(text_full_path, "w", encoding="utf-8") as file:
        file.write(text_extracted)
        print(f"Executat cu succes {file}")



# print("Outside main")

if __name__ == "__main__":
    pass
    # doc_test = 'C:/Users/const/PycharmProjects/sda_47/venv/proiect_scanned/docs/doc_1.pdf'
    # # text_doc = extarct_text_from_pdf(doc_test)
    # # print(text_doc)
    # save_extratected_text_to_txt(doc_test)
    # print("Inside main")
