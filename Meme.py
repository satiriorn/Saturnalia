import requests, Keyboard

def Get_meme(bot, update):
    try:
        c = requests.get('https://meme-api.herokuapp.com/gimme').json()
        update.message.reply_photo(c['url'])
    except Exception:
        bot.send_message(update.message.chat_id, "Ти точно людина? Меми, не хочуть бути с тобою.", reply_markup=Keyboard.InitKeyboard())