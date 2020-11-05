from pydub import AudioSegment
import badge, DB, Youtube, os, pytube, Keyboard
from mutagen.easyid3 import EasyID3

def CutStart(update, context):
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, update.message.chat_id)
    context.bot.send_message(update.message.chat_id, answer["35"], reply_markup=Keyboard.InlineKeyboard(badge.CutKeyboard, False))

def CutAudio(update, context):
    chat_id = Youtube.GetChatID(update)
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, chat_id)
    print(update)
    if str(chat_id) in badge.UseCommand.keys() and update.message.text == None:
        print(update.message.text)
        if badge.UseCommand[str(chat_id)] == "CutAudio":
            file = context.bot.getFile(update.message.audio.file_id)
            title = update.message.audio.title
            if title!=None:
                badge.CutAudio[str(chat_id)]=file.download(title)
            else:
                badge.CutAudio[str(chat_id)] = "ExtractTrack.mp3"
                file.download(title)
        context.bot.send_message(update.message.chat_id, answer["33"])
    elif str(chat_id) in badge.UseCommand.keys()and update.message.text != None:
        print(update.message.text)
        if badge.UseCommand[str(chat_id)] == "CutAudio":
            time = str(update.message.text).split('-')
            start = (time[0]).split(':')
            finish = (time[1]).split(':')
            startMin = int(start[0])
            startSec = int(start[1])
            endMin = int(finish[0])
            endSec = int(finish[1])
            startTime = startMin * 60 * 1000 + startSec * 1000
            endTime = endMin * 60 * 1000 + endSec * 1000
            NameMusic = badge.CutAudio[str(chat_id)]
            song = AudioSegment.from_mp3(NameMusic)
            extract = song[startTime:endTime]
            ExtractName = NameMusic.replace('.mp3',"")+'-extract'
            extract.export(ExtractName, format="mp3")
            audio = EasyID3(ExtractName)
            audio['title'] = ExtractName
            audio.update()
            context.bot.send_audio(update.message.chat_id, open(ExtractName, 'rb'))
            badge.UseCommand.pop(str(chat_id))
            badge.CutAudio.pop(str(chat_id))
            remove(NameMusic)
            remove(ExtractName)
    else:
        context.bot.edit_message_text(chat_id=chat_id, text=answer["32"], message_id=update.callback_query.message.message_id)
        badge.UseCommand[str(chat_id)] = "CutAudio"

def remove(name):
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), name)
    os.remove(path)