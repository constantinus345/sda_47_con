"""
Schema aplicatiei:
oferim o locatie si vrem sa vedem cate grade sunt acolo acum, si eventual alte date
vrem sa trimitem aceste informatii o data pe ora la un cont de telegram
"""
# import the module
import python_weather
import asyncio
import telegram
from configs import token_telegram
from time import sleep
import os

"""i_1 = ia-mi datele de pe un site #astepte
i_2 = print(1+3)
i_3 = ia datele de pe site_2
#in mod clasic instructiunile se executa pe rand = sincroniza.
#Cu asyncio se pot executa intr-un mod ASyncronizat, aprox pararalel"""

async def getweather(cityx, idt):
    # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        # fetch a weather forecast from a city
        weather = await client.get(cityx)

        # returns the current day's forecast temperature (int)
        text = f"In {cityx} temperatura actuala este {weather.current.temperature} grade Celsius"
        await telegram_send_message(chat_idx = idt, text_x = text)

        # get the weather forecast for a few days
        # for forecast in weather.forecasts:
        #     print(forecast)
        #
        #     # hourly forecasts
        #     for hourly in forecast.hourly:
        #         print(f' --> {hourly!r}')

async def telegram_send_message(chat_idx, text_x):
    bot = telegram.Bot(token_telegram)
    async with bot:
        await bot.send_message(text = text_x, chat_id = chat_idx)

chat_id_con = 1307289323

#programul va rula, apoi va astepta 60*60 secunde, adica ruleaza la fiecare ora.

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(getweather(cityx = "Bucharest ", idt= chat_id_con))


