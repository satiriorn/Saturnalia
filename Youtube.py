import os, badge, re, urllib.request, urllib.parse, DB, pytube
from mutagen.easyid3 import EasyID3

urlopen = urllib.request.urlopen
encode = urllib.parse.urlencode
retrieve = urllib.request.urlretrieve
cleanup = urllib.request.urlcleanup()

def Get_Audio(update,context):
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, update.message.chat_id)
    try:
        if badge.CommandMusic != True:
            context.bot.send_message(update.message.chat_id, answer["1"])
            badge.CommandMusic = True
            badge.NameUserCommand = update.message.from_user.first_name
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
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, update.message.chat_id)
    if badge.CommandVideo != True:
        context.bot.send_message(update.message.chat_id, answer["1"])
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
    NameMusic.remove("voice.mp3")
    return NameMusic

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
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), NameMusic[0])
    os.remove(path)