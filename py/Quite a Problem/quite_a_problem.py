import sys

def find_problem(string, find='problem'):
    '''Tries to find problem in a string'''

    return find in string.lower().rstrip()  # strip \n and put everything to lowercase

for string in sys.stdin:
    # goes through every input we put in and tries to find problem in the string
    print('yes' if find_problem(string) else 'no')