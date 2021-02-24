from googletrans import Translator
import Mafina, DB, CreateVoice

def translate(update, context, answer, chat_id):
    try:
        if str(update.message.chat_id) in Mafina.Mafina.UseCommand.keys():
            if Mafina.Mafina.UseCommand[str(update.message.chat_id)] == "Translate":
                result = ''
                lang = DB.DataBase.GetTranslateLanguage(Mafina.Mafina.DB, chat_id)
                translations = Mafina.Mafina.translator.translate([update.message.text], dest=lang)
                for translation in translations:
                    result = translation.text
                CreateVoice.TranslateVoice(update, context, result, lang)
        else:
            Mafina.Mafina.UseCommand[str(update.message.chat_id)] = "Translate"
            context.bot.send_message(update.message.chat_id, answer["14"])
    except Exception:
        Mafina.Mafina.translator = Translator()
        context.bot.send_message(update.message.chat.id, answer["15"])
        Mafina.Mafina.UseCommand.pop(str(update.message.chat_id))