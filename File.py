import badge,CutAudio


def file(update, context):
    print(update)
    if badge.Cute == True:
        CutAudio.Cut(update, context)