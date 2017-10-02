# user inputs two numbers/coordinates (x,y) which tells us which quadrant the point is in
x = int(input())
y = int(input())

if x > 0 and y > 0:
    print(1)
elif x < 0 < y:
    print(2)
elif x < 0 > y:
    print(3)
else:
    print(4)