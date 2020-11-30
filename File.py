import badge, Cut, DB, os

def file(update, context):
    print(update)
    if str(update.message.chat_id) == "1243553196":
        try:
            DB.DataBase.InsertFile(badge.DB, update.message.document.file_id)
        except Exception:
            DB.DataBase.InsertFile(badge.DB, update.message.video.file_id)
    if str(update.message.chat_id) in badge.UseCommand.keys():
        res = badge.UseCommand[str(update.message.chat_id)]
        if res == "CutAudio": Cut.CutAudio(update, context)
        elif res == "CutVideo": Cut.CutVideo(update, context)

def SendFile(update, context):
    fileID = DB.DataBase.GetFileId(badge.DB, update.message.chat_id)
    print(fileID)
    file = context.bot.getFile(fileID)
    title =("{0}.gif").format(update.message.chat_id)
    file.download(title)
    context.bot.send_video(update.message.chat_id, open(title, 'rb'))
    os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)), title))