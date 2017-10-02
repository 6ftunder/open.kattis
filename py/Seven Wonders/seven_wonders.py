cards = input()  # all the scientific cards we have

T = cards.count('T')  # count the amount of T(tablet) scientific cards
C = cards.count('C')  # count the amount of C(compass) scientific cards
G = cards.count('G')  # count the amount of G(gear) scientific cards

# print out the result with 7*min of the 3 scientific cards if player possesses all 3 cards
# else print out with the normal formula...
print(T**2 + C**2 + G**2 + 7*min((T, C, G)) if T and C and G else T**2 + C**2 + G**2)
