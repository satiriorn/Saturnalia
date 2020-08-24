import random

def question(bot, update):
    r = random.randint(0, 100)
    if(r<=10):
        bot.send_message(update.message.chat_id, " НІ! КАТЕГОРИЧНО НІ!")
    elif(r<=20):
        bot.send_message(update.message.chat_id, "ТИ ЩО ХВОРИЙ ЧИ ЩО? ЗВІСНО НІ.")
    elif (r <= 30):
        bot.send_message(update.message.chat_id, "АНІТРОХИ")
    elif (r <= 40):
        bot.send_message(update.message.chat_id, "Ні в якому разі")
    elif (r <= 50):
        bot.send_message(update.message.chat_id, "Вибачайся")
    elif (r <= 60):
        bot.send_message(update.message.chat_id, "Можливо")
    elif (r <= 70):
        bot.send_message(update.message.chat_id, "Нехай буде так")
    elif (r <= 80):
        bot.send_message(update.message.chat_id, "Залізобетонно")
    elif (r <= 90):
        bot.send_message(update.message.chat_id, "ЗВІСНО")
    elif (r <= 100):
        bot.send_message(update.message.chat_id, "Навіщо питати те, що всі і так знають?")


