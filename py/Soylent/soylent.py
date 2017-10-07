import sys, math

base_calories = 400  # number of calories each bottle provides
for _ in sys.stdin:
    for required_calories in sys.stdin:
        print(math.ceil(int(required_calories)/base_calories))

