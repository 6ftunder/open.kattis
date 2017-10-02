import sys

for i in sys.stdin:
    # split the input at '-', add the initials of everything in the list to st, print out st
    ab = i.split('-')
    st = ''
    for part in ab:
        st += part[0]
    print(st)
