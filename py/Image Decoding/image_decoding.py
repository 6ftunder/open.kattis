import sys
# work in progress,
# working version will be merged
# to master branch
#
#
#
decoded_output = []  # all the output we will print
for i in sys.stdin:
    try:
        for _ in range(int(i)):
            # for every input in the range provided decode the image
            pass
    except ValueError:
        # caught the ValueError, print out error decoding and pass the error
        print('Error decoding image')
        pass