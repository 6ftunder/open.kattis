import sys

for _ in sys.stdin:
    # number of test cases ignored since it doesn't affect anything
    for i in sys.stdin:
        cities = set()  # empty set for cities to be added in, since it's a set it will remove duplicates
        i = int(i)  # number of cities we have to check
        for _ in range(i):
            # go thorugh the ammount of cases
            cities.add(input())
        print(len(cities))
