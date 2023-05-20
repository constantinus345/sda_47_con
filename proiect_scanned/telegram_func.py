#pip install python-telegram-bot
#unele librarii au pip install diferit de import!
import telegram
import asyncio

from configs import token_secret_telegram

async def send_telegram_message(chat_idx, message, parse_modex = "HTML"):
    """
    :param chat_id: id-ul telegram al utilizatorului
    :param message: mesajul trimis
    :return: None, face o actiune
    """
    token_secret = token_secret_telegram
    bot = telegram.Bot(token_secret)
    await bot.send_message(chat_id=chat_idx, text=message, parse_mode= parse_modex)

if __name__ == "__main__":
    #pentru a gasi id-ul tau de telegram> https://t.me/raw_info_bot
    id_constantin = 1307289323
    mesaj = 'Salut, ce zici?'
    # send_telegram_message(id_constantin, mesaj)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_telegram_message(id_constantin, mesaj))