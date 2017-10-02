abcPos = {}  # set positions for the collected numbers

numbers = list(map(int, input().split()))
positions = input()

values = {'A': min(numbers), 'C': max(numbers)}  # A is smallest number, C is largest number, B is what is left
C = max(numbers)
del numbers[numbers.index(values['A'])]  # remove both numbers
del numbers[numbers.index(values['C'])]
B = numbers[0]
values['B'] = B

n = 1
for letter in positions:
    abcPos[n] = letter
    n += 1

string = ''
for i in range(1, 4):
    string += str(values[abcPos[i]]) + ' '
print(string[:-1])
