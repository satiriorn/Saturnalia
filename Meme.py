import requests

def Link():
    return requests.get('https://meme-api.herokuapp.com/gimme').json()['url']

def Get_meme(update, context):
    try:
        update.message.reply_photo(Link())
    except Exception:
        context.bot.send_message(update.message.chat_id, "Ти точно людина? Меми, не хочуть бути с тобою.")