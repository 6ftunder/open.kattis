import sys


def to_minutes(hour, minute):
    """
    converts hours to minutes and adds extra minutes in the time...
    returns the sum
    """
    return (hour * 60) + minute


for i in sys.stdin:
    month, day, year, time1, time2 = i.split()  # split the input at ' '

    hour1, minute1 = map(int, time1.split(':'))  # split the times at : and convert str to int
    hour2, minute2 = map(int, time2.split(':'))

    timeInSeconds = 60 * (to_minutes(hour2, minute2) - to_minutes(hour1, minute1))  # time in seconds

    print(month, day, year, '{} hours {} minutes'.format(timeInSeconds//3600, timeInSeconds//60 - (timeInSeconds//3600 * 60)))
