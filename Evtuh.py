import badge, random, Keyboard

def Evtuh(update, context, status=True):
    try:
        r = random.randint(0, len(badge.God)-1)
        if status == True:
            context.bot.send_message(update.message.chat_id, badge.God[r])
        else:
            return badge.God[r]
    except Exception:
        context.bot.send_message(update.message.chat_id, "Ти не потрібен українському богу віршів.")