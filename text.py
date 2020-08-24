import DogAndCat, weather, badge, CreateVoice, UkrainianGame, Meme

def text(bot, update):
    try:
        if badge.Command == True:
            CreateVoice.voice(bot, update)
            badge.Command = False
        elif 'погода' in update.message.text.lower():
            weather.CurrentWeather(bot, update)
        elif update.message.text.lower() in 'котик' or update.message.text.lower() in 'мило':
            DogAndCat.Cat_photo(bot, update)
        elif 'мем' in update.message.text.lower()  :
            Meme.Get_meme(update)
        elif '?' in update.message.text.lower():
            UkrainianGame.question(bot, update)
    except Exception:
        bot.send_message(update.message.chat.id, 'Я створив тисячи відповедей задля того, щоб тобі не відповідати.')

def textMessage(bot, update):
    try:
        if '/translate' in update.message.text:
            #bot.send_message(update.message.chat_id,"""Введите язык текста""")
            badge.count = True
        elif badge.count == True:
            #translate(bot, update)
            badge.count = False
        else:
            text(bot, update)
    except Exception:
        bot.send_message(update.message.chat.id, 'Я створив тисячи відповедей задля того, щоб тобі не відповідати.')