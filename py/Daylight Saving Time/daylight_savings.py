import sys

# cpu time 0.02s
for i in sys.stdin:
    for j in sys.stdin:
        # splitting the input at ' ' and converting input into int if it's a digit else str
        forwards_backwards, change, hour, minute = map(
            lambda x: int(x) if x.isdigit() else x, j.split())

        # time added together in minutes, added or removed change in minutes
        time_in_minutes = ((hour * 60) + minute) + \
            change if forwards_backwards == 'F' else \
                ((hour * 60) + minute) - change
        # we take hours and get the remainder with 24
        # hours % 24

        print('{} {}'.format(time_in_minutes // 60 % 24, time_in_minutes % 60))
