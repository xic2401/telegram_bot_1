from bs4 import BeautifulSoup
import telebot

import youtube_dl

import requests

token = '1702123934:AAG4xQh_ZnXnauuHnpjd0Jwojj9_fM4VwDw'
bot = telebot.TeleBot(token)
welcome_text = """
	Youtube downmloader!
"""
type_url = """
Введите ссылку на видео
"""


@bot.message_handler(content_types=['text'])
def send_welcome(message):
    chat_id = message.chat.id
    if message.text.lower() == 'привет':
        bot.reply_to(message=message,
                     text=welcome_text)
        download()
    else:
        pass
def download():

    url = 'https://www.youtube.com/watch?v=adLGHcj_fmA'

    headers = {
        'authorization': "Basic cnl4aWMyNDAxOkFreWxiZWtvdi4yNDAx",
        'x-rapidapi-key': "3ab6ddfed5msh28d51e4f519bea8p1f6acfjsn155908950743",
        'x-rapidapi-host': "youtube-mp3-downloader.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    bot.send_audio(response)


bot.polling()


