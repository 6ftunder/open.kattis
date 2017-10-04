from datetime import datetime as dt
import sys
## current cpu time 0.08
# needs to be improved

end = []  # print all the times
for i in sys.stdin:

    if i == '0\n':
        for j in range(1, len(end)):
            # for every item in the list end
            if j == len(end)-1:
                print(end[j].replace('AM', 'a.m.').replace('PM', 'p.m.'), end="")
                break
            print(end[j].replace('AM', 'a.m.').replace('PM', 'p.m.') + '\n' if end[j] != '\n' else '\n', end="")
        break

    times = []  # list of times
    end += '\n'

    for _ in range(int(i)):
        # convert the times into 24 hour time format

        time = input()
        # if it ends with a.m. change the part to AM; p.m. to PM
        if time[-4:] == 'a.m.':
            times.append(dt.strptime(time[:-4] + 'AM', '%I:%M %p'))
        else:
            times.append(dt.strptime(time[:-4] + 'PM', '%I:%M %p'))

    times.sort()
    end += [dt.strftime(current, '%I:%M %p').lstrip("0") for current in times]
