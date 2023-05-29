# In this kata, we will make a function to test whether a period is late.
#
# Our function will take three parameters:
#
# last - The Date object with the date of the last period
#
# today - The Date object with the date of the check
#
# cycleLength - Integer representing the length of the cycle in days
#
# Return true if the number of days passed from last to today is greater than cycleLength. Otherwise, return false.

# from datetime import date


# def period_is_late(last, today, cycle_length):
#     # The * takes out the value of the tuple passed (unpack the tuple).
#     l = date(*last)
#     t = date(*today)
#     delta = t - l
#     return delta.days > cycle_length

def period_is_late(last, today, cycle_length):
    return (today - last).days > cycle_length
