import badge, Thread, DB, Keyboard
def SearchBook():
    pass
def UploadBook(update, context):
    

def MenuBook(update, context):
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, update.message.chat_id)
    context.bot.send_message(update.message.chat_id, answer["39"], reply_markup=Keyboard.InlineKeyboard(badge.MenuBookKeyboard, False))

def MonitorDoc(update, context):
    if str(update.message.chat_id) in badge.UseCommand.keys():
        res = badge.UseCommand[str(update.message.chat_id)]
        #if res == "Book": Thread.Thread(MenuBook)
    print("jopa"+str(update))