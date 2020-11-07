import DogAndCat, weather, badge, CreateVoice, UkrainianGame, Meme, Youtube, Translate, Cut, Thread

def text(update,context):
    #try:
    print(update)
    if str(update.message.chat_id) in badge.UseCommand.keys():
        res = badge.UseCommand[str(update.message.chat_id)]
        if res == "Audio": Thread.Thread(Youtube.Get_Audio,(update, context))
        elif res == "Video":Thread.Thread(Youtube.Get_Video,(update, context))
        elif res == "CutAudio":Thread.Thread(Cut.CutAudio,(update, context))
        elif res == "CutVideo":Thread.Thread(Cut.CutVideo,(update, context))
        elif res == "CreateVoice":Thread.Thread(CreateVoice.voice,(update, context))
        elif res == "Translate":Thread.Thread(Translate.translate,(update, context))
        elif res == "GetCutVideo":Thread.Thread(Cut.GetCutStart,(update,context))
        elif res == "CutEnd":Thread.Thread(Cut.Cut,(update, context))
    elif "погода" == update.message.text.lower():
        Thread.Thread(weather.CurrentWeather,(update, context))
    elif update.message.text.lower() == "котик":
        Thread.Thread(DogAndCat.Cat_photo,(update, context))
    elif "мем" == update.message.text.lower():
        Thread.Thread(Meme.Get_meme,(update, context))
    elif '?' in update.message.text.lower():
        Thread.Thread(UkrainianGame.question,(update, context))
    #except Exception:
    #    context.bot.send_message(update.message.chat.id, 'Я створив тисячи відповедей задля того, щоб тобі не відповідати.')
