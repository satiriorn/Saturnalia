import badge, random

def ShevchenkoStyle(update, context,  status=True):
    r = random.randint(0, len(badge.ShevchenkoStyle)-1)
    if status == True:
        context.bot.send_message(update.message.chat_id, badge.ShevchenkoStyle[r])
    else:
        return badge.ShevchenkoStyle[r]