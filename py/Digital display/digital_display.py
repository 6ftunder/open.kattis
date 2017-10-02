import sys

# using a list of multiple dicts with all the parts needed to produce any part of any time
part = \
[{'1': '    +', '2': '+---+', '3': '+---+', '4': '+   +', '5': '+---+', '6': '+---+', '7': '+---+', '8': '+---+', '9': '+---+', '0': '+---+', ':': ' '},
 {'1': '    |', '2': '    |', '3': '    |', '4': '|   |', '5': '|    ', '6': '|    ', '7': '    |', '8': '|   |', '9': '|   |', '0': '|   |', ':': ' '},
 {'1': '    |', '2': '    |', '3': '    |', '4': '|   |', '5': '|    ', '6': '|    ', '7': '    |', '8': '|   |', '9': '|   |', '0': '|   |', ':': 'o'},
 {'1': '    +', '2': '+---+', '3': '+---+', '4': '+---+', '5': '+---+', '6': '+---+', '7': '    +', '8': '+---+', '9': '+---+', '0': '+   +', ':': ' '},
 {'1': '    |', '2': '|    ', '3': '    |', '4': '    |', '5': '    |', '6': '|   |', '7': '    |', '8': '|   |', '9': '    |', '0': '|   |', ':': 'o'},
 {'1': '    |', '2': '|    ', '3': '    |', '4': '    |', '5': '    |', '6': '|   |', '7': '    |', '8': '|   |', '9': '    |', '0': '|   |', ':': ' '},
 {'1': '    +', '2': '+---+', '3': '+---+', '4': '    +', '5': '+---+', '6': '+---+', '7': '    +', '8': '+---+', '9': '+---+', '0': '+---+', ':': ' '}]

output = ''  # our timed output
for time in sys.stdin:
    time = time.rstrip()
    if time == 'end':
        print(output+'end')  # print out end when at the end of the output
        break

    for i in range(7):
        # go through every part in the list
        string = ''
        for segment in time:
            # for every segment add to sting the current parts
            string += part[i][segment] + '  '
        output += string[:-2] + '\n'
    output += '\n\n'