import os, badge, re
import urllib.request
import urllib.parse

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
    try:
        if badge.CommandMusic != True:
            context.bot.send_message(update.message.chat_id, "Мені потрібне посилання на відео:")
            badge.CommandMusic = True
            badge.NameUserCommand = update.message.from_user.first_name
            return
        elif(badge.NameUserCommand == update.message.from_user.first_name):
            song="https://www.youtube.com/watch?v="+(update.message.text).replace('https://youtu.be/','')

            if "youtube.com/" not in song:
                query_string = encode({"search_query": song})
                html_content = urlopen("http://www.youtube.com/results?" + query_string)
                search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
                command = 'youtube-dl --embed-thumbnail --no-warnings --extract-audio --audio-format mp3 -o "%(title)s.%(ext)s" ' + \
                          search_results[0]
            else:
                command = 'youtube-dl --embed-thumbnail --no-warnings --extract-audio --audio-format mp3 -o "%(title)s.%(ext)s" ' + song[song.find("=") + 1:]
            os.system(command)
            NameMusic = [f for f in os.listdir(os.getcwd()) if f.endswith('.mp3')]
            NameMusic.remove("voice.mp3")
            context.bot.send_audio(update.message.chat_id, open(NameMusic[0], 'rb'))
            badge.CommandMusic = False
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), NameMusic[0])
            os.remove(path)
    except Exception:
        badge.CommandMusic = False
        context.bot.send_message(update.message.chat.id, 'Щось пішло не так спробуй ще раз.')