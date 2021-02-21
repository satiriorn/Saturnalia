import requests, badge, re, math, time, calendar, DB, os, shutil
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

def voice(update,context):
    answer, lang = DB.DataBase.GetJsonLanguageBot(badge.DB, update.message.chat_id)
    mp3_name = str(update.message.chat_id)+'.mp3'
    file = shutil.copy(r'voice.mp3', mp3_name)
    try:
        if str(update.message.chat_id) in badge.UseCommand.keys():
            if badge.UseCommand[str(update.message.chat_id)] == "CreateVoice":
                mes = update.message.text
                gTTS(text=mes, lang=detect(mes)).save(file)
                context.bot.send_voice(update.message.chat_id,open(file, 'rb'))
                os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)), file))
        else:
            badge.UseCommand[str(update.message.chat_id)] = "CreateVoice"
            context.bot.send_message(update.message.chat_id, answer["4"])
        badge.UseCommand.pop(str(update.message.chat_id))
    except Exception:
        context.bot.send_message(update.message.chat_id, answer["5"])
        badge.UseCommand.pop(str(update.message.chat_id))
        os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)), file))

def TranslateVoice(update, context, mes, lang):
    mp3_name = str(update.message.chat_id) + '.mp3'
    file = shutil.copy(r'voice.mp3', mp3_name)
    try:
        gTTS(text=mes.lower(), lang=lang).save(file)
        context.bot.send_voice(update.message.chat_id, open(file, 'rb'))
        context.bot.send_message(update.message.chat.id, mes)
        os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)), file))
        badge.UseCommand.pop(str(update.message.chat_id))
    except Exception:
        context.bot.send_message(update.message.chat_id, mes)
        badge.UseCommand.pop(str(update.message.chat_id))
        os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)), file))