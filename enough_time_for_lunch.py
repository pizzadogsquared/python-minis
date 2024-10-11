def enough_time_for_lunch(hour1, minute1, hour2, minute2):
    if hour1 > hour2:
        return(False)
    elif hour1 == hour2 and minute1 > minute2:
        return(False)
    elif hour1 == hour2 and minute1 < minute2:
        if minute2 - minute1 < 45:
            return(False)
        else:
            return(True)
    elif hour1 < hour2:
        hour_diff = hour2 - hour1
        rough_mins = hour_diff * 60
        if minute1 > minute2:
            mins_diff =  rough_mins - (minute1 - minute2)
            if mins_diff < 45:
                return(False)
            else:
                return(True)
        else:
            return(True)









