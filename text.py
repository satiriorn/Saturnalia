import DogAndCat, weather, badge, CreateVoice, UkrainianGame, Meme, Youtube, Translate, Cut

def text(update,context):
    try:
        print(update)
        if str(update.message.chat_id) in badge.UseCommand.keys():
            res = badge.UseCommand[str(update.message.chat_id)]
            if res == "Audio": Youtube.Get_Audio(update, context)
            elif res == "Video":Youtube.Get_Video(update, context)
            elif res == "CutAudio":Cut.CutAudio(update, context)
            elif res == "CutVideo":Cut.CutVideo(update, context)
            elif res == "CreateVoice":CreateVoice.voice(update, context)
            elif res == "Translate":Translate.translate(update, context)
        elif "погода" == update.message.text.lower():
            weather.CurrentWeather(update, context)
        elif update.message.text.lower() == "котик":
            DogAndCat.Cat_photo(update, context)
        elif "мем" == update.message.text.lower():
            Meme.Get_meme(update, context)
        elif '?' in update.message.text.lower():
            UkrainianGame.question(update, context)
    except Exception:
        context.bot.send_message(update.message.chat.id, 'Я створив тисячи відповедей задля того, щоб тобі не відповідати.')
