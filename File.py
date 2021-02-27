import os, Thread
class File:
    _instance, _mafina = None, None
    def __new__(cls, M):
        if not hasattr(cls, '_inst'):
            File._instance = super(File, cls).__new__(cls)
            File._mafina = M
            return File._instance
    @classmethod
    def file(self, update, context, answer, lang, chat_id):
        print(update)
        print(chat_id)
        if chat_id == "1243553196":
            try:
                self._mafina._DB.InsertFile(update.message.document.file_id)
            except Exception:
                self._mafina._DB.InsertFile(update.message.video.file_id)
        if chat_id in self._mafina.UseCommand.keys():
            res = self._mafina.UseCommand[chat_id]
            if res == "CutAudio": Thread.Thread(self._mafina._cut.CutAudio, (update, context, answer, chat_id))
            elif res == "CutVideo": Thread.Thread(self._mafina._cut.CutVideo, (update, context, answer, chat_id))
            elif res == "ConfirmSendVideo": Thread.Thread(self._mafina._std.convert, (update, context, answer, chat_id))
            elif res == "Check" or res == "UploadFile" or res == "Confirm" or res == "BookLang" or res == "FormatBook":
                Thread.Thread(self._mafina._book.UploadBook, (update, context, answer, lang, chat_id))

    @classmethod
    def SendFile(self, update, context):
        fileID = self._mafina._DB.GetFileId(str(155))
        print(fileID)
        file = context.bot.getFile(fileID)
        title =("{0}.gif").format(update.message.chat_id)
        file.download(title)
        context.bot.send_video(update.message.chat_id, open(title, 'rb'))
        os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)), title))
