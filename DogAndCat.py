import  datetime, requests, DB, badge

now = datetime.datetime.now()

def get_url_cat():
    return requests.get('https://api.thecatapi.com/v1/images/search').json()[0]['url']

def get_url_dog():
    return requests.get('https://random.dog/woof.json').json()['url']

def CheckExtension(url, array):
    for allowed_ext in array:
        if url.lower().endswith(allowed_ext):
            return True
    return False

def is_image(url):
    allowed_extension = ['jpg', 'jpeg', 'png']
    return CheckExtension(url, allowed_extension)

def is_animation(url):
    allowed_extension = ['mp4', 'gif']
    return CheckExtension(url, allowed_extension)

def Photo(url, update):
    if is_image(url):
        update.message.reply_photo(url)
    elif is_animation(url):
        update.message.reply_animation(url)

def Cat_photo(update, context):
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, update.message.from_user.first_name)
    try:
        Photo(get_url_cat(), update)
    except Exception:
        context.bot.send_message(context.bot_data[update.poll_answer.poll_id], answer["6"])


def Dog_photo(update, context):
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, update.message.from_user.first_name)
    try:
        Photo(get_url_dog(), update)
    except Exception:
        context.bot.send_message(context.bot_data[update.poll_answer.poll_id], answer["7"])