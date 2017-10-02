import sys

for i in sys.stdin:
    numerator, denominator = map(int, i.split())
    if not numerator and not denominator:
        break
    wholeNumber = numerator//denominator
    print(wholeNumber, '{} / {}'.format(numerator-(denominator*wholeNumber), denominator))
