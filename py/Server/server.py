n, T = map(int, input().split())  # n is number of tasks, where T is allowed compute time

tasks = list(map(int, input().split()))  # input of tasks(their times of completion)

counter = 0  # number of added tasks
while T >= tasks[counter] and n > 0:
    # while we still have compute time add tasks
    # if there are no tasks we don't do anything
    T -= tasks[counter]
    counter += 1
    n -= 1
    if counter >= len(tasks):
        # we ran out of tasks
        break
print(counter)
