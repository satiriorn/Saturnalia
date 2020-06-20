import badge, random

def Evtuh(bot, update, status=True):
    r = random.randint(0, len(badge.God)-1)
    if status == True:
        bot.send_message(update.message.chat_id, badge.God[r])
    else:
        return badge.God[r]