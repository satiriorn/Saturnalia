import requests

def Get_meme(update):
    c = requests.get('https://meme-api.herokuapp.com/gimme').json()
    update.message.reply_photo(c['url'])