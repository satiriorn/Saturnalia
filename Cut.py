from pydub import AudioSegment
import badge, DB, Youtube, os, pytube, Keyboard
from mutagen.easyid3 import EasyID3
from datetime import timedelta, datetime

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
                Cut(update, context)
        else:
            context.bot.edit_message_text(chat_id=chat_id, text=answer["36"], message_id=update.callback_query.message.message_id)
            badge.UseCommand[str(chat_id)] = "CutVideo"
    except Exception:
        delete(update, chat_id)

def GetCutStart(update, context):
    chat_id = Youtube.GetChatID(update)
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, chat_id)
    file, name = "",""
    youtube = None
    try:
        if str(chat_id) in badge.UseCommand.keys():
            if badge.UseCommand[str(chat_id)] == "GetCutVideo":
                video_url = update.message.text
                try:
                    youtube = pytube.YouTube(video_url).streams.filter()
                except Exception:
                    youtube = pytube.YouTube(video_url).streams.filter().all()
                file = youtube[0].download()
                name = str(chat_id).replace('-','')
                print(name)
                os.rename(file, ('{}.mp4').format(name))
                badge.CutFile[str(chat_id)]= ('{}.mp4').format(name)
                context.bot.send_message(update.message.chat_id, answer["33"])
                badge.UseCommand.pop(str(chat_id))
                badge.UseCommand[str(chat_id)] = "CutEnd"
        else:
            context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id, text=answer["1"],
                                          message_id=update.callback_query.message.message_id)
            badge.UseCommand[str(chat_id)] = "GetCutVideo"
    except Exception:
        delete(update, chat_id)
        context.bot.send_message(chat_id, answer["2"])

def GetCutEnd(update, context):
    chat_id = Youtube.GetChatID(update)
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, chat_id)
    try:
        if str(chat_id) in badge.UseCommand.keys():
            if badge.UseCommand[str(chat_id)] == "CutEnd":
                Cut(update, context)
    except Exception:
        delete(update, chat_id)
        context.bot.send_message(chat_id, answer["2"])

def Cut(update, context):
    chat_id = Youtube.GetChatID(update)
    time = str(update.message.text).split('-')
    start = GetDataTime(time[0])
    finish = GetDataTime(time[1])
    duration = finish - start
    start = datetime.strftime(start, '%H:%M:%S')
    file = str(badge.CutFile[str(chat_id)])
    name = get_name(update)
    os.system(('ffmpeg -ss {} -i {} -to {} -c copy {}.mp4').format(str(start),
                                                                           os.path.join(file),
                                                                           str(duration),
                                                                           str(name)))
    context.bot.send_video(update.message.chat_id, open(('{}.mp4').format(str(name)), 'rb'))
    delete(update, chat_id)

def get_name(update):
    return (lambda x: x == 'private' if update.message.chat.username else DB.DataBase.GetIdUser(badge.DB, Youtube.GetChatID(update)))(
        update.message.chat.type)

def delete(update, chat_id):
    badge.UseCommand.pop(str(chat_id))
    file = badge.CutFile[str(chat_id)]
    badge.CutFile.pop(str(chat_id))
    remove(('{}.mp4').format(str(get_name(update))))
    remove(os.path.join(file))

def remove(name):
    os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)), name))

def GetDataTime(time):
    if str(time).count(':') > 1:
        return datetime.strptime(time, '%H:%M:%S')
    elif str(time).count(':') == 1:
        return datetime.strptime(time, '%M:%S')
    else:
        return datetime.strptime(time, '%S')