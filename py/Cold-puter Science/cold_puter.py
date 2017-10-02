_ = input()  # number of test cases; we can ignore this since it has no significance
temps = map(int, input().split())  # all the temps stored to a list with type int

subercold = 0  # how many temps below 0 we got
for i in temps:
    # for every temp we recorded if it's less than 0 add +1 to subercold
    if i < 0:
        subercold += 1
print(subercold)
