from datetime import datetime

def humanise(this_time):
    if this_time.hour >= 22:
        return "night"
    elif this_time.hour >= 18:
        return "evening"
    elif this_time.hour >= 14:
        return "afternoon"
    elif this_time.hour >= 10:
        return "day"
    elif this_time.hour >= 6:
        return "morning"
    else:
        return "night"
