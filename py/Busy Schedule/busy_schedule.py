#cpu time 0.03s

all_times = []
while True:
    i = input()

    if i == '0':
        # let's end with the final output

        for hour, minute, ampm in all_times[:-1]:
            # for every time in all times, except the last
            hour = hour[0].replace('0', '12') if len(hour) == 1 else hour
            print('{}:{} {}'.format(hour, minute, ampm) if hour else '')

        hour, minute, ampm = all_times[-1]
        hour = hour[0].replace('0', '12') if len(hour) == 1 else hour
        print('{}:{} {}'.format(hour, minute, ampm), end="")
        break

    current_times = []
    if all_times:
        # empty line in our print
        all_times.append(['', '', ''])

    for _ in range(int(i)):
        # for our current input range add times to times list
        time = input()
        time = time[:2].replace('12', '0') + time[2:]  # try to replace the 12 with 0
        time = time.split()
        current_times += [time[0].split(':') + [time[1]]]  # append the current time to current_times
    current_times.sort(key=lambda x: (x[2], int(x[0]), int(x[1])))  # sort all_times by am/pm, hours, minutes
    all_times += current_times