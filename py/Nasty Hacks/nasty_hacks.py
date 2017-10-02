import sys

for i in sys.stdin:
    for j in i:
        # since the first input is always a number we will do the i-times
        print(j)  # we're going through each input
        k = sys.stdin
        loss, gain, cost = map(int, k.split())
        gain -= cost
        if gain > loss:
            print('advertise')
            break
        elif gain < loss:
            print('do not advertise')
            break
        else:
            print('does not matter')
            break
