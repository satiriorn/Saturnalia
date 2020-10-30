import badge,CuteAudio


def file(update, context):
    print(update)
    if badge.Cute == True:
        CuteAudio.Cut(update, context)