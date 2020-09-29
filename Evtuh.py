import badge, random

def Evtuh(update, context, status=True):
    r = random.randint(0, len(badge.God)-1)
    return (lambda status:status if context.bot.send_message(update.message.chat_id, badge.God[r])else badge.God[r])(status)