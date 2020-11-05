<<<<<<< HEAD
import os, badge, DB, pytube, Keyboard, subprocess
from mutagen.easyid3 import EasyID3

=======
import os, badge, re, urllib.request, urllib.parse, DB, pytube, Keyboard
from mutagen.easyid3 import EasyID3

urlopen = urllib.request.urlopen
encode = urllib.parse.urlencode
retrieve = urllib.request.urlretrieve
cleanup = urllib.request.urlcleanup()

>>>>>>> facbc7dbfc3a4ebc81e5c6394c3214fb66074a92
def Start(update, context):
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, update.message.chat_id)
    context.bot.send_message(update.message.chat_id, answer["34"], reply_markup=Keyboard.InlineKeyboard(badge.YoutubeKeyboard, False))

def Get_Audio(update,context):
<<<<<<< HEAD
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
=======
    answer = GetAnswer(update)
    try:
        if badge.CommandMusic != True:
            context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id, text=answer["1"], message_id=update.callback_query.message.message_id)
            badge.CommandMusic = True
            badge.NameUserCommand = update.callback_query.message.chat.first_name
            return
        elif(badge.NameUserCommand == update.message.from_user.first_name):
            song=ReplaceLink(update)
            if "youtube.com/" not in song:
                query_string = encode({"search_query": song})
                html_content = urlopen("http://www.youtube.com/results?" + query_string)
                search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
                command = 'youtube-dl --embed-thumbnail --no-warnings --extract-audio --audio-format mp3 -o "%(title)s.%(ext)s" ' + \
                          search_results[0]
            else:
                command = 'youtube-dl --embed-thumbnail --no-warnings --extract-audio --audio-format mp3 -o "%(title)s.%(ext)s" ' + song[song.find("=") + 1:]
            os.system(command)
            NameMusic = GetFormat()
            audio = EasyID3(NameMusic[0])
            audio['title'] = NameMusic[0].replace('.mp3',"")
            audio.save()
            context.bot.send_audio(update.message.chat_id, open(NameMusic[0], 'rb'))
            DeletePath(GetFormat())
    except Exception:
        DeletePath(GetFormat())
        context.bot.send_message(update.message.chat.id, answer["2"])

def Get_Video(update, context):
    answer = GetAnswer(update)
>>>>>>> facbc7dbfc3a4ebc81e5c6394c3214fb66074a92
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

<<<<<<< HEAD
def GetChatID(update):
    try:
        return update.callback_query.message.chat_id
    except Exception:
        return update.message.chat_id
=======
def GetAnswer(update):
    try:
        return DB.DataBase.GetJsonLanguageBot(badge.DB, update.callback_query.message.chat_id)
    except Exception:
        return DB.DataBase.GetJsonLanguageBot(badge.DB, update.message.chat_id)
>>>>>>> facbc7dbfc3a4ebc81e5c6394c3214fb66074a92


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
<<<<<<< HEAD
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), NameMusic)
=======
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), NameMusic[0])
>>>>>>> facbc7dbfc3a4ebc81e5c6394c3214fb66074a92
    os.remove(path)