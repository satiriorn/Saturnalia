from ffmpy import FFmpeg
import Mafina, DB, os

def convert(update,context, answer, chat_id):
    if str(chat_id) in Mafina.Mafina.UseCommand.keys():
        if Mafina.Mafina.UseCommand[str(chat_id)] == "ConfirmSendVideo":
            file = context.bot.getFile(update.message.video.file_id)
            titlemp4 = ("{0}.mp4").format(chat_id)
            titlegif = ("{0}.gif").format(chat_id)
            file.download(titlemp4)
            ff = FFmpeg(inputs={titlemp4: None}, outputs={titlegif: '-vf scale=1280:720'})
            ff.run()
            context.bot.send_animation(chat_id, open(titlegif, 'rb'))
            Mafina.Mafina.UseCommand.pop(str(chat_id))
            DeletePath(titlemp4)
            DeletePath(titlegif)
    else:
        context.bot.send_message(chat_id, answer["36"])
        Mafina.Mafina.UseCommand[str(chat_id)] ="ConfirmSendVideo"

def DeletePath(file):
    os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)), file))