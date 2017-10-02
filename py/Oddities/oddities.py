# since we have a small sample size -10 <= x <= 10 we can write out every solution
# saving time and compute power hue...
solutions = {int(10): 'even', int(9): 'odd', int(8): 'even', int(7): 'odd', int(6): 'even', int(5): 'odd', int(4): 'even', \
             int(3): 'odd', int(2): 'even', int(1): 'odd', int(0): 'even', int(-1): 'odd', int(-2): 'even', int(-3):'odd', \
             int(-4): 'even', int(-5): 'odd', int(-6): 'even', int(-7): 'odd', int(-8): 'even', int(-9): 'odd', int(-10): 'even'}

for i in range(int(input())):
    # go through the i times, given by the input
    storage = int(input())  # store the current number
    print('{} is {}'.format(storage, solutions[storage]))
