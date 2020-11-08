import requests

def get_url_cat():
    return requests.get('https://api.thecatapi.com/v1/images/search').json()[0]['url']

def get_url(str):
    try:
        return requests.get(str).json()['url']
    except Exception:
        return requests.get(str).json()[0]['url']

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

def Photo(url, update, context):
    if is_image(url):
        context.bot.send_photo(update.message.chat_id, url)
    elif is_animation(url):
        context.bot.send_animation(update.message.chat_id, url)