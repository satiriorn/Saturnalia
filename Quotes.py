import badge, random

def ShevchenkoStyle(bot, update, status=True):
    arr = len(badge.God)
    r = random.randint(0, arr)
    if status == True:
        bot.send_message(update.message.chat_id, badge.ShevchenkoStyle[r])
    else:
        return badge.ShevchenkoStyle[r]