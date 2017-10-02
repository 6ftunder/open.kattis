# list of all the pieces; the number of said pieces
# below is the list of required pieces(the proper ammount)
# -----------
# One king
# One queen
# Two rooks
# Two bishops
# Two knights
# Eight pawns
setAmmount = [1, 1, 2, 2, 2, 8]  # the number of required pieces
pieces = map(int, input().split())  # map object of number of specific pieces, the list follows the order of above list

string = ''
for pieceNeeded, piece in zip(setAmmount, pieces):
    # for every piece we simply deduct the piece with required number of pieces
    string += str(pieceNeeded-piece) + ' '

print(string[:-1])