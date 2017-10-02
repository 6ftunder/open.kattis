x, y, n = map(int, input().split())
xStr = 'Fizz'
yStr = 'Buzz'
for i in range(1, n+1):
    string = ''
    if i % x == 0:
        string += xStr
    if i % y == 0:
        string += yStr
    print(string if string else i)
