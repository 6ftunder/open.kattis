import sys

times = int(input())
for _ in range(times):
    # since first input is always a number we will read the input i times
    k = input().split('Simon says')
    if not len(k) < 2:
        # if we got 'Simon says', the length will be greater or equal to 2
        print(k[1])
