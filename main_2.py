
import youtube_dl
import telebot
import requests
token = '1702123934:AAG4xQh_ZnXnauuHnpjd0Jwojj9_fM4VwDw'
bot = telebot.TeleBot(token)
def download(title, link):

    link = 'https://www.youtube.com/results?search_query=bruno+mars+leave+the+door+open'
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192', }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    return {
        'audio': open(title + '.mp3','rb'),
        'title': title,
    }
    print('download')
lola = 'sad'
if lola == 'sad':
    download()
else:
    pass