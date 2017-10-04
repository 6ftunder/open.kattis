import sys

# for every line in the input split the names in the input
# and add them to the list of names
# list of people consists of tuples (name, surname)

people = []  # list of all the people
names = set()  # set of all names
repeated_names = set()  # set of all repeated names

for line in sys.stdin.readlines():
    # for the whole input take out names and surnames
    # add the name to set names and add name to repeated_names
    # if the name alerady in name
    # add tuple (name, surname) to list of people

    line = line.split()

    if line[0] in names:
        repeated_names.add(line[0])
    names.add(line[0])

    people.append(tuple(line))

# sort people by surname then by name
people = sorted(people, key=lambda x: (x[1], x[0]))

for name, surname in people:
    # print out people with surname if repeated, withouth if not repeated
    print(name, surname if name in repeated_names else '')
