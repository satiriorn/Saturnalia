from pydub import AudioSegment
import badge, DB, Youtube, os, pytube, Keyboard
from mutagen.easyid3 import EasyID3

def CutStart(update, context):
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, update.message.chat_id)
    context.bot.send_message(update.message.chat_id, answer["35"], reply_markup=Keyboard.InlineKeyboard(badge.CutKeyboard, False))

def CutAudio(update, context):
    chat_id = Youtube.GetChatID(update)
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, chat_id)
    NameMusic, ExtractName = "", ""
    try:
        if str(chat_id) in badge.UseCommand.keys() and update.message.text == None:
            if badge.UseCommand[str(chat_id)] == "CutAudio":
                file = context.bot.getFile(update.message.audio.file_id)
                title = update.message.audio.title
                if title!=None:
                    badge.CutFile[str(chat_id)]=file.download(title)
                else:
                    badge.CutFile[str(chat_id)] = "ExtractTrack.mp3"
                    file.download(title)
            context.bot.send_message(update.message.chat_id, answer["33"])
        elif str(chat_id) in badge.UseCommand.keys()and update.message.text != None:
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
                NameMusic = badge.CutFile[str(chat_id)]
                song = AudioSegment.from_mp3(NameMusic)
                extract = song[startTime:endTime]
                ExtractName = NameMusic.replace('.mp3',"")+'-extract'
                extract.export(ExtractName, format="mp3")
                audio = EasyID3(ExtractName)
                audio['title'] = ExtractName
                audio.update()
                context.bot.send_audio(update.message.chat_id, open(ExtractName, 'rb'))
                badge.UseCommand.pop(str(chat_id))
                badge.CutFile.pop(str(chat_id))
                remove(NameMusic)
                remove(ExtractName)
        else:
            context.bot.edit_message_text(chat_id=chat_id, text=answer["32"], message_id=update.callback_query.message.message_id)
            badge.UseCommand[str(chat_id)] = "CutAudio"
    except Exception:
        badge.UseCommand.pop(str(chat_id))
        badge.CutFile.pop(str(chat_id))
        remove(NameMusic)
        remove(ExtractName)
        context.bot.send_message(chat_id, answer["2"])

def CutVideo(update, context):
    chat_id = Youtube.GetChatID(update)
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, chat_id)
    try:
        if str(chat_id) in badge.UseCommand.keys() and update.message.text == None:
            if badge.UseCommand[str(chat_id)] == "CutVideo":
                file = context.bot.getFile(update.message.video.file_id)
                badge.CutFile[str(chat_id)] = file.download()
                context.bot.send_message(update.message.chat_id, answer["33"])
        elif str(chat_id) in badge.UseCommand.keys()and update.message.text != None:
            if badge.UseCommand[str(chat_id)] == "CutVideo":
                Cut(update,chat_id)
        else:
            context.bot.edit_message_text(chat_id=chat_id, text=answer["36"], message_id=update.callback_query.message.message_id)
            badge.UseCommand[str(chat_id)] = "CutVideo"
    except Exception:
        delete(chat_id)

def GetCutStart(update, context):
    chat_id = Youtube.GetChatID(update)
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, chat_id)
    file = ""
    try:
        if str(chat_id) in badge.UseCommand.keys():
            if badge.UseCommand[str(chat_id)] == "GetCutVideo":
                video_url = Youtube.ReplaceLink(update)
                youtube = pytube.YouTube(video_url).streams.first()
                file = youtube.download()
                os.rename(file, ('{}.mp4').format(update.message.chat.username))
                file = ('{}.mp4').format(update.message.chat.username)
                badge.CutFile[str(chat_id)]= file
                context.bot.send_message(update.message.chat_id, answer["33"])
                badge.UseCommand.pop(str(chat_id))
                badge.UseCommand[str(chat_id)] = "CutEnd"
        else:
            context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id, text=answer["1"],
                                          message_id=update.callback_query.message.message_id)
            badge.UseCommand[str(chat_id)] = "GetCutVideo"
    except Exception:
        delete(chat_id)
        context.bot.send_message(chat_id, answer["2"])

def GetCutEnd(update, context):
    chat_id = Youtube.GetChatID(update)
    if str(chat_id) in badge.UseCommand.keys():
        if badge.UseCommand[str(chat_id)] == "CutEnd":
            Cut(update, context)

def Cut(update, context):
    chat_id = Youtube.GetChatID(update)
    try:
        time = str(update.message.text).split('-')
        start = (time[0]).split(':')
        finish = (time[1]).split(':')
        startMin = int(start[0])
        startSec = int(start[1])
        endMin = int(finish[0])
        endSec = int(finish[1])
        durationMin = endMin - startMin - 1
        durationSec = (60 - startSec) + endSec
        if durationSec >= 60:
            while (durationSec >= 60):
                durationSec -= 60
                durationMin += 1
        file = str(badge.CutFile[str(chat_id)])
        durationMin = valid_duration(durationMin)
        durationSec = valid_duration(durationSec)
        os.system(('ffmpeg -ss 00:{}:{} -i {} -to 00:{}:{} -c copy {}.mp4').format(str(startMin), str(startSec),
                                                                                   file,
                                                                                   str(durationMin), str(durationSec),
                                                                                   str(chat_id)))
        context.bot.send_video(update.message.chat_id, open(('{}.mp4').format(str(chat_id)), 'rb'))
        delete(chat_id)
    except Exception:
        delete(chat_id)

def valid_duration(duration):
    if duration < 10:
        duration = '0' + str(duration)
    return duration

def delete(chat_id):
    remove(('{}.mp4').format(str(chat_id)))
    remove(badge.CutFile[str(chat_id)])
    badge.UseCommand.pop(str(chat_id))
    badge.CutFile.pop(str(chat_id))

def remove(name):
    os.remove( os.path.join(os.path.abspath(os.path.dirname(__file__)), name))