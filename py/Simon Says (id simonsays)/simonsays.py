import sys

for i in sys.stdin:
    for j in i:
        # since first input is always a number we will read the input i times
        for k in sys.stdin:
            k = k.split('Simon says')
            if not len(k) < 2:
                print(k[1])
