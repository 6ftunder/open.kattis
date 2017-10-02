import sys

# new alphabet stored in dict
newAlphabet = {'a': '@', 'b': '8', 'c': '(', 'd': '|)', 'e': '3', 'f': '#', 'g': '6', 'h': '[-]', 'i': '|', 'j': '_|',
               'k': '|<', 'l': '1', 'm': '[]\/[]', 'n': '[]\[]', 'o': '0', 'p': '|D', 'q': '(,)', 'r': '|Z', 's': '$',
               't': "']['", 'u': '|_|', 'v': '\/', 'w': '\/\/', 'x': '}{', 'y': "`/", 'z': '2'}
for i in sys.stdin:
    str = ''

    for j in i.lower().rstrip():
        # go through every letter in our message and change it for the newAlphabet letter
        # if letter is not in the newAlphabet keep the same letter
        str += newAlphabet.get(j, j)

    print(str)  # output the end result