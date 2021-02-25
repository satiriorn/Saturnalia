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
    def voice(self, update, context, answer, chat_id):
        mp3_name = chat_id+'.mp3'
        file = shutil.copy(r'voice.mp3', mp3_name)
        try:
            if chat_id in self._mafina.UseCommand.keys():
                if self._mafina.UseCommand[chat_id] == "CreateVoice":
                    mes = update.message.text
                    gTTS(text=mes, lang=detect(mes)).save(file)
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
    """
    def TranslateVoice(update, context, mes, lang):
        mp3_name = str(update.message.chat_id) + '.mp3'
        file = shutil.copy(r'voice.mp3', mp3_name)
        try:
            gTTS(text=mes.lower(), lang=lang).save(file)
            context.bot.send_voice(update.message.chat_id, open(file, 'rb'))
            context.bot.send_message(update.message.chat.id, mes)
            os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)), file))
            Mafina.Mafina.UseCommand.pop(str(update.message.chat_id))
        except Exception:
            context.bot.send_message(update.message.chat_id, mes)
            Mafina.Mafina.UseCommand.pop(str(update.message.chat_id))
            os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)), file))
    """