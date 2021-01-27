import badge, Cut, DB, os, Convert, Thread

def file(update, context):
    print(update)
    if str(update.message.chat_id) == "1243553196":
        try:
            DB.DataBase.InsertFile(badge.DB, update.message.document.file_id)
        except Exception:
            DB.DataBase.InsertFile(badge.DB, update.message.video.file_id)
    if str(update.message.chat_id) in badge.UseCommand.keys():
        res = badge.UseCommand[str(update.message.chat_id)]
        if res == "CutAudio": Thread.Thread(Cut.CutAudio,(update, context))
        elif res == "CutVideo": Thread.Thread(Cut.CutVideo,(update, context))
        elif res == "ConfirmSendVideo": Thread.Thread(Convert.convert,(update,context))

def SendFile(update, context):
    fileID = DB.DataBase.GetFileId(badge.DB, str(155))
    print(fileID)
    file = context.bot.getFile(fileID)
    title =("{0}.gif").format(update.message.chat_id)
    file.download(title)
    context.bot.send_video(update.message.chat_id, open(title, 'rb'))
    os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)), title))