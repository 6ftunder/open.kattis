import sys

# we will skip the taste cases since it's irelevant to our output
# the second input will be split at simon says
# letters are only lowercase

for _ in sys.stdin:
    for simon in sys.stdin:

        # in simon try to find if simon says is located at the start
        # if it is print out the command else print empty line
        print(simon[11:] if simon.rstrip().find(
            'simon says ', 0, 11) is 0 else '')
