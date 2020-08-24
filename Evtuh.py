import badge, random, Keyboard

def Evtuh(bot, update, status=True):
    r = random.randint(0, len(badge.God)-1)
    if status == True:
        bot.send_message(update.message.chat_id, badge.God[r], reply_markup = Keyboard.InitKeyboard())
    else:
        return badge.God[r]