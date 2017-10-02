_ = input()
temps = map(int, input().split())

subercold = 0  # how many temps below 0 we got
for i in temps:
    # for every temp we recorded if it's less than 0 add to the subercold temps
    if i < 0:
        subercold += 1
print(subercold)