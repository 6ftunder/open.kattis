import sys

for i in sys.stdin:
    r1, res = map(int, i.split())  # expected two numbers R1 and end result
    print(res*2 - r1)
