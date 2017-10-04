import sys

for i in sys.stdin:
    # input of i-inputs

    if i == '0\n':
        # reched the end break the loop
        break
    menu = dict()

    for _ in range(int(i)):
        # go through the inputs i times add them to menu dict
        order = input().rstrip().split()

        for thing in order[1:]:
            # for every thing in the order add to dict as key,
            # add person to value of food/drink ordered

            if not menu.get(thing, False):
                # if we don't have the item in the menu add it in
                menu[thing] = []

            # add the person who ordered it to the list of people that
            # ordered the item
            menu[thing] += [order[0]]

    for key, value in sorted(menu.items()):
        # for every sorted key
        # print out ordered keys with sorted values as string
        print(key, ' '.join(sorted(menu[key])) + ' ')

    print()  # print empty line
