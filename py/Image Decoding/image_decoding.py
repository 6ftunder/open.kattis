import sys

def first_line(line):
    # get the first input and set the needed length of lines
    pixel, number_of_outputs = line[0], line[1:]
    line_output = ''  # the current line
    for times in number_of_outputs:
        line_output += pixel * times  # add the current pixels in the line
        pixel = d[pixel]  # change into second pixel
    sys.stdout.write(line_output + '\n')

    return len(line_output)

d = {'.': '#', '#': '.'}  # next pixel we have to take
first = True  # we have not printed anything yet, so skip the first \n

while True:
    i = int(input())
    if i == 0:
        # if at end break
        break

    if first:
        first = not first
    else:
        sys.stdout.write('\n')

    decoding_error = False  # if we detect an error in our output (more pixels than needed)
    first_line_return = first_line(list(map(lambda x: int(x) if x.isdigit() else x, input().split())))
    length_of_lines = first_line_return
    for _ in range(int(i) - 1):
        # for every input in the range provided decode the image
        current_input = list(map(lambda x: int(x) if x.isdigit() else x, input().split()))
        current_pixel, number_of_outputs = current_input[0], current_input[1:]
        line_output = ''  # the current line
        for times in number_of_outputs:
            line_output += current_pixel * times  # add the current pixels in the line
            current_pixel = d[current_pixel]  # change into second pixel
        sys.stdout.write(line_output + '\n')
        if not decoding_error:
            if length_of_lines != sum(number_of_outputs):
                decoding_error = not decoding_error

    if decoding_error:
        sys.stdout.write('Error decoding image' + '\n')
