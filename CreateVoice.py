import os, shutil
from gtts import gTTS
from langdetect import detect

class Voice:
    _instance, _mafina = None, None
    def __new__(cls, M):
        if not hasattr(cls, '_inst'):
            Voice._instance = super(Voice, cls).__new__(cls)
            Voice._mafina = M
            return Voice._instance

    @classmethod
    def gen_voice(self, update, context, answer, chat_id, text):
        self._mafina.UseCommand[chat_id] = "CreateVoice"
        self.voice(update, context, answer, chat_id, text)

    @classmethod
    def voice(self, update, context, answer, chat_id, text = ""):
        mp3_name = chat_id+'.mp3'
        file = shutil.copy(r'voice.mp3', mp3_name)
        try:
            if chat_id in self._mafina.UseCommand.keys():
                if self._mafina.UseCommand[chat_id] == "CreateVoice":
                    gTTS(text=text, lang=detect(text)).save(file)
                    context.bot.send_voice(chat_id, open(file, 'rb'))
                    os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)), file))
                    self._mafina.UseCommand.pop(chat_id)
            else:
                self._mafina.UseCommand[chat_id] = "CreateVoice"
                context.bot.send_message(chat_id, answer["4"])
        except Exception:
            context.bot.send_message(chat_id, answer["5"])
            self._mafina.UseCommand.pop(chat_id)
            os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)), file))

    @classmethod
    def TranslateVoice(self, update, context, mes, lang, chat_id):
        mp3_name = chat_id + '.mp3'
        file = shutil.copy(r'voice.mp3', mp3_name)
        try:
            gTTS(text=mes.lower(), lang=lang).save(file)
            context.bot.send_voice(chat_id, open(file, 'rb'))
            context.bot.send_message(chat_id, mes)
            os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)), file))
            self._mafina.UseCommand.pop(chat_id)
        except Exception:
            context.bot.send_message(chat_id, mes)
            self._mafina.UseCommand.pop(chat_id)
            os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)), file))
