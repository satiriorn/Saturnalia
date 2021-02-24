import random, Mafina, DB

def question(update, context):
    answer, lang = DB.DataBase.GetJsonLanguageBot(Mafina.Mafina.DB, update.message.chat.id)
    r = random.randint(0, 100)
    state_sys_answer = DB.DataBase.GetAnswerSystem(Mafina.Mafina.DB, update.message.chat.id)
    if state_sys_answer==True:
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