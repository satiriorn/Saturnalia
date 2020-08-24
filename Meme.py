import requests, Keyboard

def Link():
    return requests.get('https://meme-api.herokuapp.com/gimme').json()['url']

def Get_meme(bot, update):
    try:
        update.message.reply_photo(Link())
    except Exception:
        bot.send_message(update.message.chat_id, "Ти точно людина? Меми, не хочуть бути с тобою.", reply_markup=Keyboard.InitKeyboard())