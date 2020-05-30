import  os, random, badge

def Cat_photo(bot, update, status=True):
    try:
        if status == True:
            file = os.listdir('telegramCat')
            r = random.randint(0, 207)
            t = 'telegramCat/'
            return bot.send_photo(update.message.chat_id, open(t + file[r], 'rb'))
        else:
            file = badge.httpCat
            r = random.randint(0, len(file))
            print(file[r])
            return file[r]
    except Exception:
        bot.send_message(update.message.chat_id, "Пока без котиков, только не плачь, умоляю")