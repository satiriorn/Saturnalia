import badge, random

def Evtuh(bot, update, status=True):
    arr = len(badge.God)
    r = random.randint(0, arr)
    if status == True:
        bot.send_message(update.message.chat_id, badge.God[r])
    else:
        return badge.God[r]