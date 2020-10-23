import DB, badge, Url

def Cat_photo(update, context):
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, update.message.from_user.first_name)
    try:
        Url.Photo(Url.get_url('https://api.thecatapi.com/v1/images/search'), update, context)
    except Exception:
        context.bot.send_message(context.bot_data[update.poll_answer.poll_id], answer["6"])

def Dog_photo(update, context):
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, update.message.from_user.first_name)
    try:
        Url.Photo(Url.get_url('https://random.dog/woof.json'), update, context)
    except Exception:
        context.bot.send_message(context.bot_data[update.poll_answer.poll_id], answer["7"])