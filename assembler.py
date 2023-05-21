import pandas as pd
import os
import json
import asyncio
from time import sleep

from clientii_mei import read_excel
from yt_api import get_info_of_channel_last_playlist
from telegram_func import send_telegram_message

def save_dict_to_excel(dict_to_save, path_to_save):
    dict_to_save = {key: [value] if not isinstance(value, list) else value for key, value in dict_to_save.items()}
    tabel = pd.DataFrame(dict_to_save)
    tabel.to_excel(path_to_save, index=True)

def save_dict_to_json(dict_to_save, path_to_save):
    with open(path_to_save, 'w') as fp:
        json.dump(dict_to_save, fp)



#notificarile catre clienti
#o sa creez un fisier cu userii notificati, 
#astfel ca n-o sa fie notificat din nou daca nu e un playlist nou

# path_cu_playlist_data = "B:/pyx/SDA/youtube_app_47"
# fisiere_json_playlist = [file for file in os.listdir(path_cu_playlist_data) if (file.endswith(".json") and not file.startswith("client_secret"))]
# #am facut un list comprehension care a selectat toate fisierele .json, in afara de cele care incep cu "client_secret"
# print(fisiere_json_playlist)

def read_data_from_json(pathx):
    with open(pathx, 'r') as json_file:
        data = json.load(json_file)
    return data

async def main():
    for client_index in range(len(clienti["nume_prenume"])):
        
        client_nume = clienti["nume_prenume"][client_index]
        canalul_sau_de_interes = clienti["canal_interes_id"][client_index]
        client_telegram_id = clienti["telegram_id"][client_index]
        
        json_file = f"{canalul_sau_de_interes}.json"
        data_playlist = read_data_from_json(json_file)
        #print(data_playlist)
        
        mesaj = f"""Salut {client_nume}, ultimul playlist de pe canalul tau de interes e:
        {data_playlist["playlist_name"]} cu {data_playlist["playlist_video_count"]} video-uri.
        Numarul total de playlistru este {data_playlist["total_playlists_of_channel"]}.""".replace("  ", "")
        
        await send_telegram_message(client_telegram_id, mesaj)
        # loop = asyncio.get_event_loop()
        # loop.run_until_complete(send_telegram_message(client_telegram_id, mesaj))
        # sleep(3)

if __name__ == "__main__":
    #clienti
    clienti = read_excel("clientii_mei.xlsx")
    #print(clienti)

    for un_canal in clienti["canal_interes_id"]:
        #playlisturi
        info_channel_plylists = get_info_of_channel_last_playlist(un_canal)
        save_dict_to_excel(info_channel_plylists, f"{un_canal}.xlsx")
        save_dict_to_json(info_channel_plylists, f"{un_canal}.json")

    asyncio.run(main())

        
    
    
