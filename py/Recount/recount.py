import sys

# cpu time 0.13 s
CANDIDATES = {}  # dict of all the candidates 'name': votes

for candidate in sys.stdin:
    # for every candidate that we put in, we add them to the CANDIDATES dict,
    # if already added add +1 to value(votes)
    # end the loop when we recieve ***

    if candidate == '***\n':
        # print out and break if at end '***'

        # find the winner of the election
        winner = max(CANDIDATES, key=CANDIDATES.get)

        # check if there is more than one winner. print winner's name, else print Runoff!
        print(winner.rstrip('\n') if list(CANDIDATES.values()).count(
            CANDIDATES[winner]) < 2 else 'Runoff!')
        break

    # add candidate if not in; add +1 to the value of candidate
    CANDIDATES[candidate] = CANDIDATES.get(candidate, 0) + 1
