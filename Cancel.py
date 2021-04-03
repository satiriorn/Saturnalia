class Cancel:
    _instance, _mafina = None, None
    def __new__(cls, M):
        if not hasattr(cls, '_inst'):
            Cancel._instance = super(Cancel, cls).__new__(cls)
            Cancel._mafina = M
            return Cancel._instance
    @classmethod
    def cancel(self, update, context, answer, chat_id):
        if chat_id in self._mafina.UseCommand.keys():
            self._mafina.UseCommand.pop(str(chat_id))
            context.bot.send_message(chat_id, answer["69"])
        else: context.bot.send_message(chat_id, answer["70"])