import requests, badge, DB

def Link():
    return requests.get('https://meme-api.herokuapp.com/gimme').json()['url']

def Get_meme(update, context):
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, update.message.from_user.first_name)
    try:
        update.message.reply_photo(Link())
        GroupChatMeme()
    except Exception:
        context.bot.send_message(update.message.chat_id, answer["3"])

def GroupChatMeme():
    while True:
        continue