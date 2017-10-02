import sys

#cpu time 0.13 s
candidates = {}  # dict of all the candidates 'name': votes

for candidate in sys.stdin:
    # for every candidate that we put in we count it

    if candidate == '***\n':
        # print out and break if at end '***'
        winner = max(candidates, key=candidates.get)  # find the winner of the election
        print(winner.rstrip('\n') if list(candidates.values()).count(
            candidates[winner]) < 2 else 'Runoff!')  # check if there is more than one winner. print winner's name, else print Runoff!
        break
    candidates[candidate] = candidates.get(candidate, 0) + 1  # add candidate if not in; add +1 to the value of candidate