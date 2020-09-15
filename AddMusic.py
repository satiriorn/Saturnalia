import re, os, sys, argparse, time, badge
import urllib.request
import urllib.parse

urlopen = urllib.request.urlopen
encode = urllib.parse.urlencode
retrieve = urllib.request.urlretrieve
cleanup = urllib.request.urlcleanup()

def video_title(url):
    try:
        webpage = urlopen(url).read()
        title = str(webpage).split('<title>')[1].split('</title>')[0]
    except:
        title = 'Youtube Song'
    return title

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
            return
        song=update.message.text
        if "youtube.com/" not in song:
            query_string = encode({"search_query": song})
            html_content = urlopen("http://www.youtube.com/results?" + query_string)
            search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
            command = 'youtube-dl --embed-thumbnail --no-warnings --extract-audio --audio-format mp3 -o "%(title)s.%(ext)s" ' + \
                      search_results[0]
        else:
            command = 'youtube-dl --embed-thumbnail --no-warnings --extract-audio --audio-format mp3 -o "%(title)s.%(ext)s" ' + song[song.find("=") + 1:]
        os.system(command)
        a=video_title(song)
        a=a.replace(' - YouTube', '')
        a+=".mp3"
        print(a)
        context.bot.send_audio(update.message.chat_id, open(a, 'rb'))
        badge.CommandMusic = False
    except Exception:
        context.bot.send_message(update.message.chat.id, 'Жіпа.')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-s", "--single", help="for single song download.")
    ap.add_argument("-l", "--list", help="for list of song download")
    #list_download()
    single_download()