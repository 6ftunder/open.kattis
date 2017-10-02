import sys
for i in sys.stdin:
    ab = i.split('-')
    st = ''
    for part in ab:
        st += part[0]
    print(st)