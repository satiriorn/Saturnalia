import DogAndCat, weather, badge, CreateVoice, UkrainianGame, Meme, AddMusic, Translate

def text(update,context):
    try:
        if badge.CommandVoice == True:
            CreateVoice.voice(update, context)
            badge.CommandVoice = False
        elif badge.CommandMusic == True:
            AddMusic.single_download(update, context)
        elif badge.CommandTranslate == True:
            Translate.translate(update, context)
        elif badge.CommandSettingTranslate ==True:
            Translate.SettingTranslate(update, context)
        elif 'погода' in update.message.text.lower():
            weather.CurrentWeather(update, context)
        elif update.message.text.lower() == 'котик':
            DogAndCat.Cat_photo(update, context)
        elif 'мем' == update.message.text.lower():
            Meme.Get_meme(update, context)
        elif '?' in update.message.text.lower():
            UkrainianGame.question(update, context)
    except Exception:
        badge.CommandVoice = False
        badge.CommandMusic = False
        badge.CommandTranslate = False
        badge.CommandSettingTranslate = False
        context.bot.send_message(update.message.chat.id, 'Я створив тисячи відповедей задля того, щоб тобі не відповідати.')