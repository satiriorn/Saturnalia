from googletrans import Translator
import badge, Keyboard, DB, CreateVoice
def translate(update, context):
    try:
        if badge.CommandTranslate != True:
            context.bot.send_message(update.message.chat_id, "Чекаю на текст:")
            badge.CommandTranslate = True
            return
        translator = Translator()
        result = ''
        lang = None
        if update.message.chat.type == "private":
            lang = DB.DataBase.GetTranlateLanguage(badge.DB, update.message.chat.first_name)
        else:
            lang = DB.DataBase.GetTranlateLanguage(badge.DB, update.message.chat.title)
        translations = translator.translate([update.message.text], dest=lang)
        for translation in translations:
            result = translation.text
        CreateVoice.TranslateVoice(update, context, result)
        badge.CommandTranslate = False
    except Exception:
        badge.CommandTranslate = False
        context.bot.send_message(update.message.chat.id, 'Щось пішло не так спробуй ще раз.')

def SettingTranslate(update,context):
    if badge.CommandSettingTranslate !=True:
        context.bot.send_message(update.message.chat_id, "Оберіть потрібну вам мову на яку бот буде перекладати:",
                                 reply_markup = Keyboard.InitKeyboard(badge.TranslateKeyboard))
        badge.CommandSettingTranslate = True
        return
    if update.message.chat.type == "private":
        DB.DataBase.VerificationLanguage(badge.DB, update.message.chat.first_name, badge.b[update.message.text])
    else:
        DB.DataBase.VerificationLanguage(badge.DB, update.message.chat.title, badge.b[update.message.text])

    context.bot.send_message(update.message.chat_id, "Ваша обрана мова встановлена.",
                             reply_markup=Keyboard.InitKeyboard(badge.MainKeyboard))
    badge.CommandSettingTranslate = False
