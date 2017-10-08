import sys

for i in sys.stdin:
    n, carrots = i.split()  # n is number of contestants, carrots is carrots given out
    print(carrots)
    for j in n:
        for k in sys.stdin:
            pass