cups = []  # list of cups with tuple (color, radius)

for i in range(int(input())):
    # go through i test cases and add the cups into the cups list
    # if we get data as diameter color we convert it to color radius
    # if we get data as color raius we just enter the data as is

    a, b = input().split()  # split the input data at ' '
    try:
        a = int(a)//2  # try to convert into int and divide by 2(diamater/2=radius)
        cups.append((b, a))
    except ValueError:
        # since first input was a string we can safely assume that b is a radius
        # that's if the input was even entered correctly
        cups.append((a, int(b)))

# print out the result
for cup in sorted(cups, key=lambda x: x[1]):
    # go through sorted cups and print out the order from smallest to largest cup
    print(cup[0])  # print out the current cup
