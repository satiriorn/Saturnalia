from ffmpy import FFmpeg
import badge

def convert(update,context):

    chat_id = badge.GetChatID(update)
    if str(chat_id) in badge.UseCommand.keys():
        if badge.UseCommand[str(chat_id)] == "ConfirmSendVideo":
            ff = FFmpeg(inputs={'video.mp4': None}, outputs={'video.gif': None})
            ff.run()
    else:
        context.bot.send_message(chat_id, answer["43"],
                                 reply_markup=Keyboard.InlineKeyboard(badge.ConfirmKeyboard, False))
