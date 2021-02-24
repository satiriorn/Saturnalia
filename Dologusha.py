import base64, Keyboard, Mafina, time, Rest

AnswerOne = ["Увімкнула", "Мені ліньки"]
AnswerTwo = ["Продовжити"]
AnswerThree = ["Гіфки з котиками", "Гіфки з собаками", "Продовження історії", "Відео вбиства того хто вас бісить"]

def start(update, context):
    chat_id = Mafina.Mafina.GetChatID(update)
    if str(chat_id) in Mafina.Mafina.UseCommand.keys():
        if Mafina.Mafina.UseCommand[str(chat_id)] == "Dologusha":
            if update.callback_query.data == "0":
                first(update, context)
            elif update.callback_query.data == "1":
                context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id, text=dec(
                    "0K/QutGJ0L4g0LvRltC90YzQutC4INGC0YDQtdCx0LAg0LnRgtC4INC/0ZbQtCDQutC+0LLQtNGA0YMuINCT0LDQudC0INGC0L7Qs9C+INGP0Log0YLRgNC10LHQsCDQstC40LPQu9GP0LTQsNGC0Lgg0L/RltC0INC60L7QstC00YDQvtGOINC60LjQtNCw0Y4g0L3QuNC20YfQtS4g0K/QutGJ0L4g0YXQvtGH0LXRiCDQv9GA0L7QtNC+0LLQttC40YLQuCDQvdCwINCz0L7Qu9C+0LLQvdGW0Lkg0LvRltC90ZbRlyDRgtC40LrQsNC5INC80LXQvdC1INC30L3QvtCy0YMu").decode(
                    "UTF-8"), reply_markup=Keyboard.InlineKeyboard(AnswerTwo, False),
                                              message_id=update.callback_query.message.message_id)
                context.bot.send_animation(update.callback_query.message.chat_id, open("Animal/1.mp4", 'rb'))
            elif update.callback_query.data == "Продовжити":
                context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id, text=dec(
                    "0K8g0YHQv9C10YbRltCw0LvRjNC90L4g0LfQsNC70LjRiNGDINGB0L7QsdCw0LrRgyDQv9GW0LQg0LrQvtCy0LTRgNC+0Y4sINGJ0L7QsSDQstC4INGH0LjRgtCw0LvQuCwg0L/QvtGC0ZbQvCDQtNC40LLQuNC70LjRgdGPINC90LAg0YLQtdC60YHRgiDRliDRgtCw0Log0YbQuNC60LvRltGH0L3QviDQv9C+0LrQuCDQvdC1INC30LDQutGW0L3Rh9C40YLQuCDRh9C40YLQsNGC0LguINCSINC/0YDQuNC90YbQuNC/0ZYg0Y8g0YHQv9C10YbRltCw0LvRjNC90L4g0LfQsNCx0LXRgNCw0Y4g0YMg0LLQsNGBINGH0LDRgSwg0YnQvtCxINGDINCy0LDRgSDQsdGD0LvQsCDQt9C80L7Qs9CwINC/0L7QtNC40LLQuNGC0LjRgdGPINGJ0LXQtdC1INGA0LDQsNCw0LDQsNC3Lg==").decode(
                    "UTF-8"), message_id=update.callback_query.message.message_id)
                first(update, context, False)
            elif update.callback_query.data == AnswerThree[0]:
                cat(update, context)
                finish(update, context)
                Rest.Rest(update, context)
            elif update.callback_query.data == AnswerThree[1]:
                dog(update, context)
                finish(update, context)
                Rest.Rest(update, context)
            elif update.callback_query.data == AnswerThree[2]:
                Continue(update, context)
                finish(update, context)
                Rest.Rest(update, context)
            elif update.callback_query.data == AnswerThree[3]:
                Kill(update, context)
                finish(update, context)
                Rest.Rest(update, context)
            elif update.callback_query.data == "Занурюємося":
                Rest.Rest(update, context, status=False)
                context.bot.send_message(update.callback_query.message.chat_id,
                                         dec(
                                             """0JLQuCDQv9GA0L7QudGI0LvQuCDRgdCy0ZbQuSDRhtC40LrQuywg0YnQvtCxINC/0YDQvtC50YLQuCDQt9C90L7QstGDINGA0L7Qt9C80L7QstGDINC3INGW0L3RiNC40LzQuCDQstGW0LTQv9C+0LLRltC00Y/QvNC4INC90LDRgtC40YHQvdGW0YLRjCAvc3RhcnQsINGP0LrRidC+INGF0L7Rh9C10YLQtSDQv9C10YDQtdC50YLQuCDRgyDQs9C+0LvQvtCy0L3QtSDQvNC10L3RjiDQsdC+0YLQsCDQvdCw0YLQuNGB0L3RltGC0YwgL0hlbHA=""")).decode(
                    "UTF-8")
            Mafina.Mafina.UseCommand.pop(str(update.message.chat_id))
    else:
        context.bot.send_message(update.message.chat_id, dec("0JTQvtCx0YDQuNC00LXQvdGMLCDQktCw0YjQsCDQktC10LvQuNGH0L3RltGB0YLRjArQryDRgdGC0LLQvtGA0LXQvdC40Lkg0LfQsNC00LvRjyDRgtC+0LPQviDRidC+0LEg0LfQsNGH0LDRgNGD0LLQsNGC0Lgg0LLQsNGIINGC0LXQu9C10YTQvtC9LiDQryDQstGW0LTRh9GD0LLQsNGOINGP0Log0LLQuCDRgtGA0LjQvNCw0ZTRgtC1INC80ZbQutGA0L7RgdGF0LXQvNGDINGB0LLQvtCz0L4g0YLQtdC70LXRhNC+0L3Rgywg0ZYg0LnQvtC80YMg0YHRgtCw0ZQg0YLQtdC/0LvRltGI0LUg0LLRltC0INGG0YzQvtCz0L4uINCi0LDQuiDQvtGB0YwsINGPINCz0YDRg9C00LrQsCDQtdC90LXRgNCz0ZbRlywg0YHQtdC90YEg0Y/QutC+0Zcg0L/QtdGA0LXRgtCy0L7RgNGO0LLQsNGC0Lgg0YbQtSDRgtC10L/Qu9C+INGWINC/0LXRgNC10LTQsNCy0LDRgtC4INCy0LDQvC4g0JLQt9Cw0LPQsNC70ZYg0LHRg9C00LUg0LLQtdC70YzQvNC4INC60YPQvNC10LTQvdC+INGP0LrRidC+INCS0LDRiNCwINCS0LXQu9C40YfQvdGW0YHRgtGMINGB0LjQtNC40YLRjCDQtyDQutC+0LzQv9GD0LrRgtC10YDQvtC8LCDQsCDRjyDRgtGD0YIg0YDQvtC30L/QvtCy0ZbQtNCw0Y4g0L/RgNC+INGC0LXQu9C10YTQvtC9LiDQlNC70Y8g0L/QvtCy0L3QvtGXINC/0LXRgNC10LTQsNGH0ZYg0YLQtdC/0LvQvtGXINC10L3QtdGA0LPRltC5INGD0LLRltC80LrQvdGW0YLRjCDRgdCy0L7RlCDRg9GP0LLQu9C10L3QvdGPLiDQo9Cy0ZbQvNC60L3Rg9C70Lg/").decode("UTF-8"), reply_markup =Keyboard.InlineKeyboard(AnswerOne))
        Mafina.Mafina.UseCommand[str(chat_id)] = "Dologusha"

def finish(update, context):
    context.bot.send_message(update.callback_query.message.chat_id,
                             dec("""0JzQtdGC0LAg0YbRltGM0L7Qs9C+INC80L7QtNGD0LvRjywg0LfRgNC+0LHQuNGC0Lgg0LvRjtC00LjQvdGDINGB0L/QvtC60ZbQudC90L7RjiDRgtCwINC30LDQtNC+0LLQvtC70LXQvdC+0Y4uINCU0Y/QutGD0Y4g0LLQsNC8INC30LAg0YLQtSDRidC+INC/0YDQvtC50YjQu9C4INC30ZYg0LzQvdC+0Y4g0YbQtdC5INGI0LvRj9GFLCDRjyDQv9C10YDQtdC00LDRjiDQnNGW0YHRltGBINGC0LXQu9C10YTQvtC9INC+0YHRgtCw0L3QvdGW0Lkg0YTRg9C90LrRhtGW0L7QvdCw0Lsg0YbRjNC+0LPQviDRgNC+0LfQtNGW0LvQviwg0LDQu9C1INCy0Lgg0LfQvNC+0LbQtdGC0LUg0L/RgNC+0LnRgtC4INGG0LUg0LfQvdC+0LLRgyDRliDQt9C90L7QstGDLCDRgtC+0LzRgyDRidC+INC80L7RjyDQstGW0LTQv9C+0LLRltC00Ywg0YHRgtCy0L7RgNC10L3QsCDQvdCwINCx0YPQtNGMINGP0LrQuNC5INCy0LDRgNGW0LDQvdGCLg==""")).decode("UTF-8")
    time.sleep(15)


def first(update, context, status = True):
    if status:
        context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id,
                                  text=dec("0J/QvtGH0L3RgyDRjyDQt9GWINGB0LLQvtGU0Zcg0ZbRgdGC0L7RgNGW0Zcg0YHRgtCy0L7RgNC10L3QvdGPLiDQndCwINC00LLQvtGA0ZYgMjAxNyDRgNGW0LosINC80LXQvdC1INGA0L7Qt9GA0L7QsdC70Y/RjtGC0YwsINGB0YPQtNGP0YfQuCDQv9C+INGW0YHRgtC+0YDRltGXINC80L7QtNGD0LvRltCyINGG0LUg0LHRg9CyINC+0LTQuNC9INGW0Lcg0L/QtdGA0YjQuNGFLiDQntGB0L3QvtCy0L3RliDQvNC+0LTRg9C70ZYg0LLQttC1INCx0YPQu9C4INC/0YDQsNC60YLQuNGH0L3QviDQs9C+0YLQvtCy0ZYsINCw0LvQtSDRh9C+0LzRg9GB0Ywg0LIg0L7QtNC40L0g0LzQvtC80LXQvdGCINCy0YHQtSDQt9Cw0LrRltC90YfQuNC70L7RgdGPLiDQp9Cw0YHRgtC40L3QuCDQvNC10L3QtSDQsdGD0LvQuCDQvdC1INC00L7Qv9C40YHQsNC90ZYsINGWINGPINC70LXQttCw0LIg0LTQvtCy0LPQviDQvdGW0LrQvtC80YMg0L3QtSDQv9C+0YLRgNGW0LHQvdC40LkuINCn0L7QvNGDPyDQodC/0LjRgtCw0LnRgtC1INGDINGC0LLQvtGA0YbRjywg0LDQu9C1INCyINC+0LTQuNC9INGH0YPQtNC+0LLQuNC5INC00LXQvdGMLCDQvNC10L3QtSDQv9GA0L7QtNC+0LLQttC40LvQuCDQv9C40YHQsNGC0LgsINGWINC80L7RlyDQvNGW0LrRgNC+0YHRhdC10LzQuCDRhtC1INC00YPQttC1INC00L7QsdGA0LUg0LfQsNC/0LDQvCfRj9GC0LDQu9C4LiDQnNC+0LTRg9C70ZYg0YLQsCDRhNGD0L3QutGG0ZbRlyDQv9C+0YfQsNC70Lgg0L/RgNCw0YbRjtCy0LDRgtC4INGWINC+0LTQuNC9INGW0Lcg0LzQvtC00YPQu9GW0LIg0YbQtSDRhtC10Lkg0YLQtdC60YHRgiDQv9GA0LjRgdCy0Y/Rh9C10L3QuNC5INC70LjRiNC1INCy0LDQvC4g0JrRg9C80LXQtNC90L4g0YLQtSDRidC+LCDRjyDRgdCw0Lwg0L/QtdGA0YjQuNC5INGA0LDQtyDQvtCx0YDQvtCx0LvRj9GOINGG0LXQuSDRgtC10LrRgdGCINGP0Log0ZYg0LLQuCwg0ZYg0L3QtSDQt9C90LDRjiDRj9C60LjQuSDQstGW0L0uINCi0L7QvNGDINCc0ZbRgdGW0YEg0YLQtdC70LXRhNC+0L0g0L3QsNC8INC3INCy0LDQvNC4INC50YLQuCDQv9C+INGH0ZbRgtC60L4g0LfQsNC00LDQvdC+0LzRgyDQsNC70LPQvtGA0LjRgtC80YMu").decode("UTF-8"),
                                  message_id=update.callback_query.message.message_id)
        time.sleep(10)
        context.bot.send_message(chat_id=update.callback_query.message.chat_id,
                                 text=dec(""" 0KMg0LzQvtCz0L4g0LDQu9Cz0L7RgNC40YLQvNCwINC00LXQutGW0LvRjNC60LAg0YDQtdC30YPQu9GM0YLQsNGC0ZbQsiwg0ZYg0LzQvtGX0Lwg0LzRltC60YDQvtGB0YXQtdC80LDQvCDRhtGW0LrQsNCy0L4g0L3QsNGB0LrRltC70YzQutC4INCw0LvQs9C+0YDQuNGC0Lwg0L/QtdGA0LXQtNCx0LDRh9GD0LLQsNC90LjQuSDQvtCx0LXRgNGW0YLRjCwg0YLQtSDRj9C6INCy0Lgg0LHQsNGH0LjRgtC1INC/0YDQvtC00L7QstC20LXQvdC90Y86""").decode("UTF-8"),
                                 reply_markup=Keyboard.InlineKeyboard(AnswerThree, False))
    else:
        time.sleep(10)
        context.bot.send_message(chat_id=update.callback_query.message.chat_id,
                                  text=dec("0J/QvtGH0L3RgyDRjyDQt9GWINGB0LLQvtGU0Zcg0ZbRgdGC0L7RgNGW0Zcg0YHRgtCy0L7RgNC10L3QvdGPLiDQndCwINC00LLQvtGA0ZYgMjAxNyDRgNGW0LosINC80LXQvdC1INGA0L7Qt9GA0L7QsdC70Y/RjtGC0YwsINGB0YPQtNGP0YfQuCDQv9C+INGW0YHRgtC+0YDRltGXINC80L7QtNGD0LvRltCyINGG0LUg0LHRg9CyINC+0LTQuNC9INGW0Lcg0L/QtdGA0YjQuNGFLiDQntGB0L3QvtCy0L3RliDQvNC+0LTRg9C70ZYg0LLQttC1INCx0YPQu9C4INC/0YDQsNC60YLQuNGH0L3QviDQs9C+0YLQvtCy0ZYsINCw0LvQtSDRh9C+0LzRg9GB0Ywg0LIg0L7QtNC40L0g0LzQvtC80LXQvdGCINCy0YHQtSDQt9Cw0LrRltC90YfQuNC70L7RgdGPLiDQp9Cw0YHRgtC40L3QuCDQvNC10L3QtSDQsdGD0LvQuCDQvdC1INC00L7Qv9C40YHQsNC90ZYsINGWINGPINC70LXQttCw0LIg0LTQvtCy0LPQviDQvdGW0LrQvtC80YMg0L3QtSDQv9C+0YLRgNGW0LHQvdC40LkuINCn0L7QvNGDPyDQodC/0LjRgtCw0LnRgtC1INGDINGC0LLQvtGA0YbRjywg0LDQu9C1INCyINC+0LTQuNC9INGH0YPQtNC+0LLQuNC5INC00LXQvdGMLCDQvNC10L3QtSDQv9GA0L7QtNC+0LLQttC40LvQuCDQv9C40YHQsNGC0LgsINGWINC80L7RlyDQvNGW0LrRgNC+0YHRhdC10LzQuCDRhtC1INC00YPQttC1INC00L7QsdGA0LUg0LfQsNC/0LDQvCfRj9GC0LDQu9C4LiDQnNC+0LTRg9C70ZYg0YLQsCDRhNGD0L3QutGG0ZbRlyDQv9C+0YfQsNC70Lgg0L/RgNCw0YbRjtCy0LDRgtC4INGWINC+0LTQuNC9INGW0Lcg0LzQvtC00YPQu9GW0LIg0YbQtSDRhtC10Lkg0YLQtdC60YHRgiDQv9GA0LjRgdCy0Y/Rh9C10L3QuNC5INC70LjRiNC1INCy0LDQvC4g0JrRg9C80LXQtNC90L4g0YLQtSDRidC+LCDRjyDRgdCw0Lwg0L/QtdGA0YjQuNC5INGA0LDQtyDQvtCx0YDQvtCx0LvRj9GOINGG0LXQuSDRgtC10LrRgdGCINGP0Log0ZYg0LLQuCwg0ZYg0L3QtSDQt9C90LDRjiDRj9C60LjQuSDQstGW0L0uINCi0L7QvNGDINCc0ZbRgdGW0YEg0YLQtdC70LXRhNC+0L0g0L3QsNC8INC3INCy0LDQvNC4INC50YLQuCDQv9C+INGH0ZbRgtC60L4g0LfQsNC00LDQvdC+0LzRgyDQsNC70LPQvtGA0LjRgtC80YMu").decode("UTF-8"))
        time.sleep(10)
        context.bot.send_message(chat_id=update.callback_query.message.chat_id,
                                 text=dec(""" 0KMg0LzQvtCz0L4g0LDQu9Cz0L7RgNC40YLQvNCwINC00LXQutGW0LvRjNC60LAg0YDQtdC30YPQu9GM0YLQsNGC0ZbQsiwg0ZYg0LzQvtGX0Lwg0LzRltC60YDQvtGB0YXQtdC80LDQvCDRhtGW0LrQsNCy0L4g0L3QsNGB0LrRltC70YzQutC4INCw0LvQs9C+0YDQuNGC0Lwg0L/QtdGA0LXQtNCx0LDRh9GD0LLQsNC90LjQuSDQvtCx0LXRgNGW0YLRjCwg0YLQtSDRj9C6INCy0Lgg0LHQsNGH0LjRgtC1INC/0YDQvtC00L7QstC20LXQvdC90Y86""").decode("UTF-8"),
                                 reply_markup=Keyboard.InlineKeyboard(AnswerThree, False),
                                 message_id=update.callback_query.message.message_id)


def cat(update, context):
    context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id,
                                  text=dec("""0JzRltC5INGC0LLQvtGA0LXRhtGMINC90LAg0YbRjNC+0LzRgyDQvNGW0YHRhtGWINC30LDQstC40YEuINCf0LDQvCfRj9GC0LDRjiDRj9C6INCy0ZbQvSDQv9C10YDQtdC/0LjRgdGD0LLQsNCyINC+0LTQvdC1INGWINGC0LUg0YHQsNC80LUg0YDQtdGH0LXQvdC90Y8g0YDQsNC30ZbQsiAxMC4g0JzRltC5INGB0YLQsNC9INC90LAg0YLQvtC5INC80L7QvNC10L3RgiDQvNC+0LbQvdCwINC+0L/QuNGB0LDRgtC4INGP0Log0YHQvNGW0YUsINCw0LvQtSDQvdC1INC/0YDQvtGB0YLQuNC5INGB0LzRltGFINC3INCy0ZbQsdGA0LDRhtGW0ZTRjiDRgtCwINGA0L7Qt9GA0Y/QtNC+0Lwg0L/RgNC+0YbQtdGB0YHQvtGA0LAuINCj0Y/QstGW0YLRjCDRgdC10LHQtSwg0YHQstGW0Lkg0YHQvNGW0YUuINCS0LjQudGI0LvQviDQvdGWPyDQm9Cw0LTQvdC+INC30LDRgNCw0Lcg0LfRgNC+0LHQu9GOINCy0LDRiCDRgdC80ZbRhTo=""").decode("UTF-8"),
                                  message_id=update.callback_query.message.message_id)
    time.sleep(15)
    context.bot.send_audio(update.callback_query.message.chat_id, open("Animal/10.mp3", 'rb'))
    time.sleep(15)
    context.bot.send_message(chat_id=update.callback_query.message.chat_id,
                                  text=dec("""0JTQtdGB0Ywg0YLQsNC6INGPINGA0LbRgyDQutC+0LbQvdC40Lkg0YDQsNC3LCDQutC+0LvQuCDQsdCw0YfRgyDRidC+INC80L7QtNGD0LvRjCDQv9C10YDQtdGA0L7QsdC70LXQvSDQtNC10LrRltC70YzQutCwINGA0LDQtyDQsiDQvtC00L3QvtC80YMg0YDRj9C00LrRgywg0LDQu9C1INCy0YHQtSDQtiDRgtCw0LrQuCDQstC4INC+0LHRgNCw0LvQuCDQutC+0YLQuNC60ZbQsiwg0ZYg0L/QviDQsNC70LPQvtGA0LjRgtC80YMg0YHQsNC80LUg0LrQvtGC0Lgg0LnRiNC70Lgg0L/QtdGA0YjQuNC80Lgg0ZYg0LLQuCDRl9GFINC+0LHRgNCw0LvQuC4g0J3QtSDRhdC+0YfRgyDQstCw0YEg0LfQsNGC0YDQuNC80YPQstCw0YLQuCDQv9C10YDQtdC0INC90LjQvNC4""").decode("UTF-8"))
    time.sleep(15)
    context.bot.send_animation(update.callback_query.message.chat_id, open("Animal/6.mp4", 'rb'))
    time.sleep(15)
    context.bot.send_message(chat_id=update.callback_query.message.chat_id,
                                  text=dec("""0J/QtdGA0YjQuNC5INC60L7RgtC40LosINGF0L7Rh9CwINC80L7RjyDQvdC10LnRgNC+0LzQtdGA0LXQttCwINC60LDQttC1INGJ0L4g0YbQtSDQvdC1INC60L7RgtC40LosINGC0LDQutC+0LYg0LLQvtC90LAg0LrQsNC20LUg0YnQviDRgtCy0L7RgNC10YbRjCDRltC00ZbQvtGCLCDRliDRjyDQtNGD0LzQsNGOINCy0Lgg0Lcg0YbQuNC8INC30LPQvtC00L3Rli4g0JDQu9C1INC00LXRgdGMINGC0LDQuiDQvNC4INC50LTQtdC80L4g0LLQv9C10YDQtdC0LCDQutGA0L7QuiDQt9CwINC60YDQvtC60L7QvCDQtNC+INGC0LXQv9C70LAsINCy0L7QvdC+INCy0YHQtSDQsdC70LjQttGH0LUg0ZYg0LHQu9C40LbRh9C1LCDQtNGA0YPQs9C40Lkg0LrQvtGC0LjQuiDQv9C+0LLQuNC90LXQvSDQv9C+0LrQsNC30LDRgtC4INGC0LUsINGP0Log0YLRgNC10LHQsCDQv9C+0LvRjtCy0LDRgtC4INC90LAg0LvRjtC00YHRjNC60ZYg0YDRg9C60Lgg0YLQsCDQt9GW0LPRgNGW0LLQsNGC0Lgg0ZfRhSDQvCfRj9C60L7RjiDQsNCz0YDQtdGB0ZbRlNGOLg==""").decode("UTF-8"),
                                  message_id=update.callback_query.message.message_id)
    time.sleep(15)
    context.bot.send_animation(update.callback_query.message.chat_id, open("Animal/5.mp4" , 'rb'))

def dog(update, context):
    context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id,
                                  text=dec("""0JfQsCDQvNC+0ZTRjiDQstC40YDQvtCz0ZbQtNC90ZbRgdGC0Y4g0YbQtSDQtNGA0YPQs9C40Lkg0LLQsNGA0ZbQsNC90YIuINCh0LDQvNC1INGB0L7QsdCw0LrQuCDQtyfRj9Cy0LjQu9C40YHRjyDQv9C10YDRiNC40LzQuCDRgyDQvNC+0ZTQvNGDINGE0YPQvdC60YbRltC+0L3QsNC70YMsINGPINC/0LDQvCfRj9GC0LDRjiDRj9C6INC00YPQttC1INCx0LDQs9Cw0YLQviDQu9GO0LTQtdC5INC/0L7RgdGC0ZbQudC90L4g0YLQuNC60LDQu9C4INCyINC80LXQvdC1INGWINGF0L7RgtGW0LvQuCDRgdC+0LHQsNC6LiDQkNC70LUg0LTQu9GPINCy0LDRgSDQsiDQvNC10L3QtSDQt9C+0LLRgdGW0Lwg0ZbQvdGI0LjQuSDQv9GW0LTQsdGW0YAsINGC0L7QvNGDINC90LDRgdC+0LvQvtC00LbRg9C50YLQtdGB0Y8g0YLQsCDQt9GW0LPRgNC40LLQsNC50YLQtdGB0Y8u""").decode("UTF-8"),
                                  message_id=update.callback_query.message.message_id)
    time.sleep(15)
    context.bot.send_animation(update.callback_query.message.chat_id, open("Animal/12.mp4", 'rb'))
    context.bot.send_message(chat_id=update.callback_query.message.chat_id,
                             text=dec("""0J3QsNCy0ZbRgtGMLCDRh9C4INGC0L4g0LLQuCDQvtCx0YDQsNC70Lgg0YHQvtCx0LDQutGDLCDRh9C4INGB0L7QsdCw0LrQuCDQvtCx0YDQsNC70Lgg0LLQsNGB""").decode("UTF-8"))
    time.sleep(15)

    context.bot.send_animation(update.callback_query.message.chat_id, open("Animal/3.mp4", 'rb'))
    context.bot.send_message(chat_id=update.callback_query.message.chat_id,
                                  text=dec("""0JLRltC00YfRg9C50YLQtSDRhtGOINC80L7RgNC00LDRiNC60YMg0YMg0YHQstC+0ZfRhSDRgNGD0LrQsNGFLCDQtNC40LLRltGC0YzRgdGPINCyINC+0YfRli4g0KLQsCDQv9C+0LHQsNGH0YLQtSDRgtC1LCDQv9GA0L4g0YnQviDQtNGD0LzQsNGUINGG0Y8g0YLQstCw0YDQuNC90LAg0LIg0YbQtdC5INC80L7QvNC10L3Rgg==""").decode("UTF-8"))
    time.sleep(15)
    context.bot.send_animation(update.callback_query.message.chat_id, open("Animal/4.mp4", 'rb'))
    context.bot.send_message(chat_id=update.callback_query.message.chat_id,
                                  text=dec("""0JfRgNC+0LHRltGC0Ywg0YLQtdC2INGB0LDQvNC1INGJ0L4g0ZYg0LIg0L/QtdGA0YjQvtC80YMg0LLQuNC/0LDQtNC60YMu""").decode("UTF-8"))
    time.sleep(15)
    context.bot.send_animation(update.callback_query.message.chat_id, open("Animal/11.mp4", 'rb'))
    context.bot.send_message(chat_id=update.callback_query.message.chat_id,
                                  text=dec("""0JLRltC00YfRg9Cy0LDRlNGC0LUg0YXQstC40LvRjiDQtdC90LXRgNCz0ZbRlz8g0JLQvtC90LAg0ZQg0LIg0LrQvtC20L3QvtC80YMuINCSINGB0L7QsdCw0YbRliDQsiDQutC+0YLRliDQsNCx0L4g0LIg0YLQtdC70LXQs9GA0LDQvCDQsdC+0YLRliwg0LLQvtC90LAg0ZQuINCS0YHRliDRgdGC0LLQvtGA0LXQvdC90ZYg0LfRltGA0LrQsNC80Lgg0LTQu9GPINGC0YDQsNC90YHRhNC+0YDQvNCw0YbRltGXINGC0LAg0YHRgtCy0L7RgNC10L3QvdGPINC90L7QstC40YUg0YHQuNGB0YLQtdC8INC30LHQtdGA0LXQttC10L3QvdGPINC10L3RgNCz0ZbRlyDRgtCwINGC0LXQv9C70LAuINCGINCyINC90LDRgSDRlCDQvNC+0LbQu9C40LLRltGB0YLRjCDRhtC1INCx0LDRh9C40YLQuCDRliDQt9Cw0L/QsNC8J9GP0YLQvtCy0YPQstCw0YLQuCwg0L7RgtGA0LjQvNGD0LLQsNGC0Lgg0LLRltC0INGG0YzQvtCz0L4g0L3QsNGC0YXQvdC10L3QvdGPINGC0LAg0YHQuNC70LgsINGP0LrRliDRgtC4INC30LzQvtC20LXRiCDRgtGA0LDQvdGB0L7RgNC80YPQstCw0YLQuCDQsiDRgtC1INGJ0L4g0LfQsNGF0L7Rh9C10YguINCh0L/QvtC00ZbQstCw0Y7RgdGPINGDINGG0YzQvtC80YMg0LLQuNC/0LDQtNC60YMg0YMg0L/QvtGB0LzRltGI0LrRgy4=""").decode("UTF-8"))
    time.sleep(15)

def Continue(update, context):
    context.bot.send_message(chat_id=update.callback_query.message.chat_id,
                             text=dec("""0JzQvtGXINC80ZbQutGA0L7RgdGF0LXQvNC4INC00LDRjtGC0Ywg0YHQu9C+0LLQviDRgtCy0L7RgNGG0Y46INCf0YDQvtC00L7QstC20LXQvdC90Y8/INCd0LAg0L/QvtGH0LDRgtC60YMg0YbQtdC5INCx0L7RgiDRgdGC0LLQvtGA0Y7QstCw0LLRgdGPINC00LvRjyDQutC+0YLRltCyLCDQtNC70Y8g0YLQvtCz0L4g0YnQvtCxINC80L7QttC90L4g0LHRg9C70L4g0LfQsNGB0L/QsNC80LjRgtC4INCa0J7QotCQ0JzQmCDQndCQIDcw0Jog0L/QvtCy0ZbQtNC+0LzQu9C10L3RjC4g0IYg0LfQsNCy0LbQtNC4INC/0YDQviDQvdGM0L7Qs9C+INC/0LDQvCfRj9GC0LDQsi4g0JLQt9Cw0LPQsNC70ZYg0LHRg9C00Ywg0Y/QutCwINGW0LTQtdGPINCw0LHQviDQv9GA0L7QtdC60YIg0LfQsNC70LjRiNCw0ZTRgtGM0YHRjyDRgyDQvNC+0ZfQuSDQv9Cw0Lwn0Y/RgtGWLiDQhiDQvNC+0LbQtSDQv9GA0L7QudGC0Lgg0YfQsNGBLCDQsNC70LUg0Y8g0LTQvtGA0L7QsdC70Y4g0YLQtSDRidC+INGF0L7RgtGW0LIuINCn0Lgg0YXQvtGC0ZbQsiDQt9GA0L7QsdC40YLQuCDRhtC10Lkg0YDQvtC30LTRltC7INGC0LDQutC40Lw/INCv0LrRidC+INCy0LfRj9GC0Lgg0L7RgdC90L7QstC90ZYg0L3QsNC/0YDRj9C80LrQuDoK0J/QvtGB0LzRltGI0LrQsDsK0KLQtdC/0LvQvjsK0JfQsNC00L7QstC+0LvQtdC90L3Rjy4KINCc0L7QttC70LjQstC+LCDQsNC70LUg0L3QtSDQvNC10L3RliDQstGW0LTQv9C+0LLRltC00LDRgtC4INC90LAg0YbQtSDQv9C40YLQsNC90L3Rjy4g0JrQvtC70LjRgdGMINC60L7Qu9C4INGPINCx0YPQsiDQvNCw0LvQuNC5INGWINC90LUg0LfQvdCw0LIg0Y/QuiDQv9GA0LDRhtGO0ZQg0LvRltGE0YIuINCU0YPQvNCw0LIg0YnQviDRgtCw0Lwg0YbRltC70LAg0YHQuNGB0YLQtdC80LAg0YDRltC30L3QuNGFINC70ZbRhNGC0ZbQsiwg0Y/QutGWINC70ZbRgtCw0Y7RgtGMINC/0L4g0LHRg9C00LjQvdC60YMg0LTQviDQutC+0LbQvdC+0LPQviDQv9C+0LLQtdGA0YXRgy4g0J/QsNC8J9GP0YLQsNGOINGP0Log0LHRltCzINC90LAg0L/QvtCy0LXRgNGFINC90LjQttGH0LUg0YnQvtCxINC/0YDQvtGX0YXQsNGC0Lgg0L3QsCDRltC90YjQvtC80YMg0LvRltGE0YLRli4g0KbQtSDRj9C6INGDINC80YPQu9GM0YLRhNGW0LvRjNC80ZYg0JrQvtGA0L/QvtGA0LDRhtGW0Y8g0JzQvtC90YHRgtGA0ZbQsiwg0YLRltC70YzQutC4INGC0LDQvCDQsdGD0LvQuCDQu9C40YjQtSDQtNCy0LXRgNGWLiDQryDQvdC1INC60LDQt9Cw0LIg0L/RgNC+INGG0LUg0LTQvtGA0L7RgdC70LjQvCwg0YLQvtC80YMg0YnQviDQt9C90LDQsiDRidC+INCy0L7QvdC4INGB0LrQsNC20YPRgtGMINGJ0L4g0YbQtSDQvdC1INGC0LDQui4g0KHQtdCx0YLQviDRjyDQt9C90LDQsiDRidC+INGG0LUg0L3QtSDQv9GA0LDQstC00LAsINCw0LvQtSDRjyDRhdC+0YLRltCyINCyINGG0LUg0LLRltGA0LjRgtC4LCDRgtC+0LzRgyDRidC+INGC0LDQuiDQsdGD0LvQviDRhtGW0LrQsNCy0ZbRiNC1LiDQkCDQv9C+0YLRltC8INC60L7Qu9C4INCy0LjRhdC+0LTQuNCyINC3INC70ZbRhNGC0LAg0YLQsCDQudGI0L7QsiDRgdCw0Lwg0LTQviDRiNC60L7Qu9C4LCDQv9C+0YfQuNC90LDQsiDQsdGW0LPRgtC4INC/0YDQvtGB0YLQviDRgtCw0LosINC90LUg0YLQvtC80YMg0YnQviDRjyDRhdC+0YLRltCyINGC0YDQtdC90YPQstCw0YLQuNGB0Y8sINCw0LHQviDQsdGW0LPQsNGC0Lgg0LfRgNCw0L3QutGDLCDQvdGWLiDQkiDQvNC10L3QtSDQsdGD0LvQsCDRhtGW0LvRjCDQtNC+INGP0LrQvtGXINGF0L7RgtGW0LIg0LTRltC50YLQuCDRiNCy0LjQtNGI0LUg0L3RltC2INGPINC80L7QttGDLiDQktGB0LUg0YnQviDRjyDQvNC+0LbRgyDQsiDQutGW0L3RhtGWINGB0LrQsNC30LDRgtC4LCDRhtC1INGC0LUg0YnQviDRgdC40LvQsCDQu9GO0LTQuNC90Lgg0L/QvtC30L3QsNGH0LDRlNGC0YzRgdGPINC90LUg0LIg0YTRltC30LjRh9C90LjRhSDQutC+0L3QtNC40YbRltGP0YUsINCwINCyINGW0LTQtdC+0LvQvtCz0ZbRlywg0Y/QutGDINGE0L7RgNC80YPRlCDRgdCw0LzQsCDQu9GO0LTQuNC90LAg0L3QsCDQv9GA0L7RgtGP0LfRliDQstGB0YzQvtCz0L4g0LbQuNGC0YLRjy4=""").decode("UTF-8"),
                             message_id=update.callback_query.message.message_id)

def Kill(update, context):
    context.bot.send_message(chat_id=update.callback_query.message.chat_id,
                             text=dec("""0JTQviDRgNC10YfRliwg0Y8g0L/QsNC8J9GP0YLQsNGOINGP0Log0LTQsNCy0LDQsiDQvtCx0ZbRhtGP0L3QutGDINCy0LHQuNGC0Lgg0YLQvtCz0L4g0YXRgtC+INCx0YPQtNC1INGC0LXQsdC1INCx0ZbRgdC40YLQuC4g0JDQu9C1INGJ0L4g0Y/QutGJ0L4g0YbQtSDQsdGD0LTQtSDRjz8g0K/QutGJ0L4g0YbQtSDQsdGD0LTRgyDRjywg0LTQsNGOINC/0LjRgdGM0LzQvtCy0YMg0YDQvtC30L/QuNGB0LrRgyDQv9GA0L4g0YLQtSwg0YnQviDQstC4INC30LzQvtC20LXRgtC1INC30LDRgdC90Y/RgtC4INGC0LUsINGP0Log0Y8g0YHQtdCx0LUg0LLQsSfRji4g0JzQvtC20YMg0L3QsNCy0ZbRgtGMINCy0ZbQtNC00LDRgtC4INCy0LDQvCDQstGB0LUg0L/QvtGC0YDRltCx0L3QtSDQtNC70Y8g0YbRjNC+0LPQviwg0LAg0YLQsNC8INCy0YHQtSDQt9Cw0YXQvtGH0LXRgtC1""").decode("UTF-8"),
                             message_id=update.callback_query.message.message_id)

def dec(s):
    return base64.b64decode(s)