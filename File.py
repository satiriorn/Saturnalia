import badge,Cut


def file(update, context):
    print(update)
    if str(update.message.chat_id) in badge.UseCommand.keys():
        res = badge.UseCommand[str(update.message.chat_id)]
        if res == "CutAudio": Cut.CutAudio(update, context)