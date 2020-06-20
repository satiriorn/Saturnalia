import badge, random

def ShevchenkoStyle(bot, update, status=True):
    r = random.randint(0, len(badge.ShevchenkoStyle)-1)
    print(r)
    if status == True:
        bot.send_message(update.message.chat_id, badge.ShevchenkoStyle[r])
    else:
        return badge.ShevchenkoStyle[r]