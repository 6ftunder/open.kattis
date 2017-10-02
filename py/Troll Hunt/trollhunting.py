import sys
import math

for i in sys.stdin:
    b, k, g = map(int, i.split())  # b is the number of bridges, k is number of knights and g is number of groups for search needed
    print((b - 1) // (k // g) if (b - 1) % (k // g) == 0 else math.ceil(((b - 1) / (k // g))))  # b-1 because we can eliminate one of the bridges since the troll was on it
    # when you have an odd number you don't get even days that's why we round up to get the correct answer
    # if we have nothing left over we can just use those days as our answer
    break
