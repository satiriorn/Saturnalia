import DogAndCat, weather, badge, CreateVoice, UkrainianGame, Meme

def text(update,context):
    try:
        if badge.Command == True:
            CreateVoice.voice(update, context)
            badge.Command = False
        elif 'погода' in update.message.text.lower():
            weather.CurrentWeather(update, context)
        elif update.message.text.lower() in 'котик' or update.message.text.lower() in 'мило':
            DogAndCat.Cat_photo(update, context)
        elif 'мем' in update.message.text.lower():
            Meme.Get_meme(update, context)
        elif '?' in update.message.text.lower():
            UkrainianGame.question(update, context)
    except Exception:
        context.bot.send_message(update.message.chat.id, 'Я створив тисячи відповедей задля того, щоб тобі не відповідати.')

def textMessage(update, context):
    try:
        if '/translate' in update.message.text:
            #context.bot.send_message(update.message.chat_id,"""Введите язык текста""")
            badge.count = True
        elif badge.count == True:
            #translate(context.bot, update)
            badge.count = False
        else:
            text(context.bot, update)
    except Exception:
        context.bot.send_message(update.message.chat.id, 'Я створив тисячи відповедей задля того, щоб тобі не відповідати.')