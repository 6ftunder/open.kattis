times = int(input())
# the whole alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(times):
    characters = {char.lower() for char in list(input().rstrip())}  # test with set instead of list
    #removed unecessary pring...
    missing = ''  # the missing characters will be added if they are missing

    for letter in alphabet:
        # for every letter in the alphabet we check if we have it in our string
        # if not, we add it to missing
        if letter not in characters:
            missing += letter

    print('pangram' if not missing else 'missing', missing)  # replaced panagram with pangram...