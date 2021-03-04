from googletrans import Translator

class Translate():
    _mafina = None
    def __init__(self, M):
        Translate._mafina = M

    @classmethod
    def translate(self, update, context, answer, chat_id):
        try:
            if chat_id in self._mafina.UseCommand.keys():
                if self._mafina.UseCommand[chat_id] == "Translate":
                    result = ''
                    lang = self._mafina._DB.GetTranslateLanguage(chat_id)
                    translations = self._mafina._translator.translate([update.message.text], dest=lang)
                    for translation in translations:
                        result = translation.text
                    print(result)
                    self._mafina._voice.TranslateVoice(update, context, result, lang, chat_id)
            else:
                self._mafina.UseCommand[chat_id] = "Translate"
                context.bot.send_message(chat_id, answer["14"])

        except Exception:
            self._mafina.translator = Translator()
            context.bot.send_message(update.message.chat.id, answer["15"])
            self._mafina.UseCommand.pop(chat_id)