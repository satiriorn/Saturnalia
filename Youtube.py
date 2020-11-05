import os, badge, DB, pytube, Keyboard, subprocess
from mutagen.easyid3 import EasyID3

def Start(update, context):
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, update.message.chat_id)
    context.bot.send_message(update.message.chat_id, answer["34"], reply_markup=Keyboard.InlineKeyboard(badge.YoutubeKeyboard, False))

def Get_Audio(update,context):
    chat_id = GetChatID(update)
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, chat_id)
    file, NameMusic = "", ""
    try:
        if str(chat_id) in badge.UseCommand.keys():
            if badge.UseCommand[str(chat_id)] == "Audio":
                url=ReplaceLink(update)
                youtube = pytube.YouTube(url).streams.filter(only_audio=True)#.all()
                file = youtube[0].download()
                title = pytube.YouTube(url).player_response['videoDetails']['title']
                NameMusic = file.replace('.mp4','.mp3')
                subprocess.call([
                    'ffmpeg',
                    '-i', os.path.join(file),
                    os.path.join(NameMusic)
                ])
                audio = EasyID3(NameMusic)
                audio['title'] = title
                audio.save()
                context.bot.send_audio(chat_id, open(NameMusic, 'rb'))
                badge.UseCommand.pop(str(chat_id))
                DeletePath(NameMusic)
                DeletePath(file)
        else:
            context.bot.edit_message_text(chat_id=chat_id, text=answer["1"], message_id=update.callback_query.message.message_id)
            badge.UseCommand[str(chat_id)] = "Audio"
    except Exception:
        DeletePath(NameMusic)
        DeletePath(file)
        context.bot.send_message(chat_id, answer["2"])

def Get_Video(update, context):
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, GetChatID(update))
    if badge.CommandVideo != True:
        context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id, text=answer["1"],
                                      message_id=update.callback_query.message.message_id)
        badge.CommandVideo = True
        return
    else:
        video_url = ReplaceLink(update)
        youtube = pytube.YouTube(video_url)
        video = youtube.streams.first()
        a = video.download()
        context.bot.send_video(update.message.chat_id, open(a, 'rb'))
        DeletePath(GetFormat('.mp4'))
        #command = 'ffmpeg -ss 00:00:33 -i jopa.mp4 -to 00:00:48 -c copy out.mp4'
        #os.system(command)

def GetFormat(format = '.mp3'):
    NameMusic = [f for f in os.listdir(os.getcwd()) if f.endswith(format)]
    if format == '.mp3':NameMusic.remove("voice.mp3")
    return NameMusic

def GetChatID(update):
    try:
        return update.callback_query.message.chat_id
    except Exception:
        return update.message.chat_id


def ReplaceLink(update):
    Link=["https://www.youtube.com/","https://youtu.be/","https://music.youtube.com/"]
    link = None
    for i in range(len(Link)):
        if Link[0] in update.message.text:
            return update.message.text
        elif Link[i] in update.message.text:
            link = Link[0]+update.message.text.replace(Link[i], '')
    return link

def DeletePath(NameMusic):
    badge.CommandMusic = False
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), NameMusic)
    os.remove(path)