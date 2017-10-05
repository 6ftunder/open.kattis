all_times = []

#cpu time 0.3s
while True:
    i = input()

    if i == '0':
        # let's end with the final output

        for j in range(len(all_times) + 1):
            # for every current time in the current range

            if j == len(all_times)-1:
                hours, minutes, ampm = all_times[j]
                print(hours[0].replace('0', '12') + ":" + minutes if len(hours) == 1 else hours + ":" + minutes, ampm, end="")
                break
            if not all_times:
                # breal of empty
                break
            if all_times[j] == '\n':
                print()
            else:
                hours, minutes, ampm = all_times[j]
                print(hours[0].replace('0', '12') + ":" + minutes if len(hours) == 1 else hours + ":" + minutes, ampm,)
        break

    current_times = []
    if all_times:
        all_times.append('\n')

    for _ in range(int(i)):
        # for our current input range add times to times list
        time = input()
        time = time[:2].replace('12', '0') + time[2:]  # try to replace the 12 with 0
        time = time.split()
        current_times += [time[0].split(':') + [time[1]]]  # append the current time to current_times
    current_times.sort(key=lambda x: (x[2], int(x[0]), int(x[1])))  # sort all_times by am/pm, hours, minutes
    all_times += current_times
