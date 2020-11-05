import random, badge, DB

def question(update, context):
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, update.message.chat.id)
    r = random.randint(0, 100)
    if(r<=10):
        context.bot.send_message(update.message.chat_id, answer["16"])
    elif(r<=20):
        context.bot.send_message(update.message.chat_id, answer["17"])
    elif (r <= 30):
        context.bot.send_message(update.message.chat_id, answer["18"])
    elif (r <= 40):
        context.bot.send_message(update.message.chat_id, answer["19"])
    elif (r <= 50):
        context.bot.send_message(update.message.chat_id, answer["20"])
    elif (r <= 60):
        context.bot.send_message(update.message.chat_id, answer["21"])
    elif (r <= 70):
        context.bot.send_message(update.message.chat_id, answer["22"])
    elif (r <= 80):
        context.bot.send_message(update.message.chat_id, answer["23"])
    elif (r <= 90):
        context.bot.send_message(update.message.chat_id, answer["24"])
    elif (r <= 100):
        context.bot.send_message(update.message.chat_id, answer["25"])