import calendar
import time
import math
import re
import requests
from gtts import gTTS
from gtts_token.gtts_token import Token

def _patch_faulty_function(self):
    if self.token_key is not None:
        return self.token_key

    timestamp = calendar.timegm(time.gmtime())
    hours = int(math.floor(timestamp / 3600))

    results = requests.get("https://translate.google.com/")
    tkk_expr = re.search("(tkk:*?'\d{2,}.\d{3,}')", results.text).group(1)
    tkk = re.search("(\d{5,}.\d{6,})", tkk_expr).group(1)

    a, b = tkk.split('.')

    result = str(hours) + "." + str(int(a) + int(b))
    self.token_key = result
    return result

# Monkey patch faulty function.
Token._get_token_key = _patch_faulty_function

def voice(bot, update, status=True):
    try:
        mes = ""
        mp3_name = 'voice.mp3'
        if status == True:
            mes = update.message.text
        else:
            mes = update
        print(mes, 'voice')
        tts = gTTS('hello', lang='en').save(mp3_name)
        print("1")

        if status == True:
            print('2')
            return bot.send_voice(update.message.chat_id, open(mp3_name, 'rb'))
        else:
            return mp3_name
    except Exception:
        bot.send_message(update.message.chat_id, 'Голосовуха дала сбой, но я все равно с тобой')