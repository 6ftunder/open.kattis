import sys
# work in progress,
# working version will be merged
# to master branch
#
#
#
def output(list):
    # prints out decoded images in the list
    for line in list[1:-1]:
        print(line if line else '')
    print(list[-1], end="")

def first_line(line):
    # get the first input and set the needed length of lines
    current_pixel, number_of_outputs = line[0], line[1:]
    line_output = ''  # the current line
    for times in number_of_outputs:
        line_output += current_pixel * times  # add the current pixels in the line
        current_pixel = d[current_pixel]  # change into second pixel

    return len(line_output), line_output

d = {'.': '#', '#': '.'}  # next pixel we have to take
decoded_output = []  # all the output we will print
for i in sys.stdin:
    if i == '0\n':
        # if at end print out
        output(decoded_output)
        break

    decoding_error = False  # if we detect an error in our output (more pixels than needed
    decoded_output.append('')
    first_line_return = first_line(list(map(lambda x: int(x) if x.isdigit() else x, input().split())))
    length_of_lines = first_line_return[0]
    decoded_output.append(first_line_return[1])
    for _ in range(int(i) - 1):
        # for every input in the range provided decode the image
        current_input = list(map(lambda x: int(x) if x.isdigit() else x, input().split()))
        current_pixel, number_of_outputs = current_input[0], current_input[1:]
        line_output = ''  # the current line
        for times in number_of_outputs:
            line_output += current_pixel * times  # add the current pixels in the line
            current_pixel = d[current_pixel]  # change into second pixel
        decoded_output.append(line_output)
        if not decoding_error:
            if length_of_lines < len(line_output):
                decoded_output.append('Error decoding image')
                decoding_error = not decoding_error
