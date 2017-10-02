# input of all contestants
contestant1 = list(map(int, input().split()))
contestant2 = list(map(int, input().split()))
contestant3 = list(map(int, input().split()))
contestant4 = list(map(int, input().split()))
contestant5 = list(map(int, input().split()))

# we join all the contestants into one big list with the sum of their scores
# set in the list respectevly to their contestant number
group = []
group += [sum(contestant1), sum(contestant2), sum(contestant3), sum(contestant4), sum(contestant5)]

# output
maks = max(group)
print(group.index(maks)+1, maks)
