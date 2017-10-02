import sys

case = 0  # counter for current case
for i in sys.stdin:
    case += 1
    X = list(map(int, i.split()))  # list of all numbers in current case

    #print out the current statistics
    print('Case {}: '.format(case), min(X[1:]), max(X[1:]), max(X[1:]) - min(X[1:]))
