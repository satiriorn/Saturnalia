import  datetime, requests

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

def Cat_photo(bot, update):
    try:
        Photo(get_url_cat(), update)
    except Exception:
        bot.send_message(update.message.chat_id, "Ти точно людина? Коти, не хочуть бути с тобою.")


def Dog_photo(bot, update):
    try:
        Photo(get_url_dog(), update)
    except Exception:
        bot.send_message(update.message.chat_id, "Рада собак заборонила в'їзд гіфок та картинок собак в полі зору ваших очей та чатику.")