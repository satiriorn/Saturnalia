import os, badge, re, urllib.request, urllib.parse, DB
from mutagen.easyid3 import EasyID3

urlopen = urllib.request.urlopen
encode = urllib.parse.urlencode
retrieve = urllib.request.urlretrieve
cleanup = urllib.request.urlcleanup()

def list_download(song_list=None):
    if not song_list:
        song_list = ""
    fhand = open(song_list, 'r')
    for song in fhand:
        single_download(song)
    fhand.close()

def single_download(update,context):
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
            NameMusic = GetMp3()
            audio = EasyID3(NameMusic[0])
            audio['title'] = NameMusic[0].replace('.mp3',"")
            audio.save()
            context.bot.send_audio(update.message.chat_id, open(NameMusic[0], 'rb'))
            DeletePath(GetMp3())
    except Exception:
        DeletePath(GetMp3())
        context.bot.send_message(update.message.chat.id, answer["2"])

def GetMp3():
    NameMusic = [f for f in os.listdir(os.getcwd()) if f.endswith('.mp3')]
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