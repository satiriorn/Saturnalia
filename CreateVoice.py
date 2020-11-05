import requests, badge, re, math, time, calendar, DB
from gtts import gTTS
from gtts_token.gtts_token import Token
from langdetect import detect

def _patch_faulty_function(self):
    try:
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
    except Exception:
        print("0")

Token._get_token_key = _patch_faulty_function

def voice(update,context, Status=True):
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, update.message.chat_id)
    try:
        mes =""
        if Status == True:
            mes = update.message.text
        else:
            mes = update
        mp3_name = 'voice.mp3'
        if badge.CommandVoice != True:
            context.bot.send_message(update.message.chat_id, answer["4"])
            badge.CommandVoice = True
            return
        gTTS(text = mes, lang=detect(mes)).save(mp3_name)
        return (lambda status: status if context.bot.send_voice(update.message.chat_id, open(mp3_name, 'rb')) else mp3_name) (Status)
    except Exception:
        context.bot.send_message(update.message.chat_id, answer["5"])

def TranslateVoice(update, context, mes, lang):
    try:
        mp3_name = 'voice.mp3'
        gTTS(text=mes.lower(), lang=lang).save(mp3_name)
        context.bot.send_voice(update.message.chat_id, open(mp3_name, 'rb'))
        context.bot.send_message(update.message.chat.id, mes)
    except Exception:
        context.bot.send_message(update.message.chat_id, mes)
