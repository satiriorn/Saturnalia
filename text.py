import DogAndCat, weather, badge, CreateVoice, UkrainianGame, Meme, AddMusic, Translate

def text(update,context):
   # try:
    if badge.CommandVoice == True:
        CreateVoice.voice(update, context)
        badge.Command = False
    elif badge.CommandMusic == True:
        AddMusic.single_download(update, context)
    elif badge.CommandTranslate == True:
        Translate.translate(update, context)
    elif 'погода' in update.message.text.lower():
        weather.CurrentWeather(update, context)
    elif update.message.text.lower() in 'котик' or update.message.text.lower() in 'мило':
        DogAndCat.Cat_photo(update, context)
    elif 'мем' in update.message.text.lower():
        Meme.Get_meme(update, context)
    elif '?' in update.message.text.lower():
        UkrainianGame.question(update, context)
   # except Exception:
        #context.bot.send_message(update.message.chat.id, 'Я створив тисячи відповедей задля того, щоб тобі не відповідати.')