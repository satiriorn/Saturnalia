import os, badge, DB, pytube, Keyboard, subprocess
from mutagen.easyid3 import EasyID3

def Start(update, context):
    answer, lang = DB.DataBase.GetJsonLanguageBot(badge.DB, update.message.chat_id)
    context.bot.send_message(update.message.chat_id, answer["34"], reply_markup=Keyboard.InlineKeyboard(badge.YoutubeKeyboard[lang], False))

def Get_Audio(update,context):
    chat_id = badge.GetChatID(update)
    answer, lang = DB.DataBase.GetJsonLanguageBot(badge.DB, chat_id)
    file, NameMusic = "", ""
    try:
        if str(chat_id) in badge.UseCommand.keys():
            if badge.UseCommand[str(chat_id)] == "Audio":
                url=update.message.text
                print(url)
                try:
                    youtube = pytube.YouTube(url).streams.filter(only_audio=True).first()
                    file = youtube.download()
                except Exception:
                     youtube = pytube.YouTube(url).streams.filter(only_audio=True).all()
                     file = youtube[0].download()
                details = pytube.YouTube(url).player_response['videoDetails']
                print(details)
                NameMusic = file.replace('.mp4','.mp3')
                subprocess.call([
                    'ffmpeg',
                    '-i', os.path.join(file),
                    os.path.join(NameMusic)
                ])
                audio = EasyID3(NameMusic)
                audio['title'] = details['title'].replace(details['author'], "").replace('- ','')
                audio['artist'] = details['author']
                audio.save()
                context.bot.send_audio(chat_id, open(NameMusic, 'rb'))
                badge.UseCommand.pop(str(chat_id))
                DeletePath(NameMusic)
                DeletePath(file)
        else:
            context.bot.edit_message_text(chat_id=chat_id, text=answer["1"], message_id=update.callback_query.message.message_id)
            badge.UseCommand[str(chat_id)] = "Audio"
    except Exception:
        badge.UseCommand.pop(str(chat_id))
        context.bot.send_message(chat_id, answer["2"])
        DeletePath(NameMusic)
        DeletePath(file)

def Get_Video(update, context):
    chat_id = badge.GetChatID(update)
    answer, lang = DB.DataBase.GetJsonLanguageBot(badge.DB, chat_id)
    file = ""
    try:
        if str(chat_id) in badge.UseCommand.keys():
            if badge.UseCommand[str(chat_id)] == "Video":
                video_url = update.message.text
                youtube = pytube.YouTube(video_url).streams.first()
                file = youtube.download()
                context.bot.send_video(update.message.chat_id,open(file, 'rb'))
                badge.UseCommand.pop(str(chat_id))
                DeletePath(file)
        else:
            context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id, text=answer["1"],
                                          message_id=update.callback_query.message.message_id)
            badge.UseCommand[str(chat_id)] = "Video"
    except Exception:
        badge.UseCommand.pop(str(chat_id))
        context.bot.send_message(chat_id, answer["2"])
        DeletePath(file)

def GetFormat(format = '.mp3'):
    NameMusic = [f for f in os.listdir(os.getcwd()) if f.endswith(format)]
    if format == '.mp3':NameMusic.remove("voice.mp3")
    return NameMusic

def DeletePath(NameMusic):
    os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)), NameMusic))