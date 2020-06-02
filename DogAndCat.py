import  os, random, badge, datetime, requests
now = datetime.datetime.now()


def get_url():
    try:
        contents = requests.get('http://aws.random.cat/meow').json()
        url = contents['file']
        return url
    e


def is_image(url):
    allowed_extension = ['jpg', 'jpeg', 'png']
    flag = False
    for allowed_ext in allowed_extension:
        if url.lower().endswith(allowed_ext):
            flag = True
            return flag
    return flag

def is_animation(url):
    allowed_extension = ['mp4', 'gif']
    flag = False
    for allowed_ext in allowed_extension:
        if url.lower().endswith(allowed_ext):
            flag = True
            return flag
    return flag

def Cat_photo(bot, update):
    url = get_url()
    if is_image(url):
        update.message.reply_photo(url)
    elif is_animation(url):
        update.message.reply_animation(url)
