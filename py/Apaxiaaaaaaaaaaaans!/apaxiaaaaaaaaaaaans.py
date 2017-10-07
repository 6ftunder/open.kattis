# this solution is 0.03s
name = input()  # input of the name ma 200 chars
current = output = name[0]  # current char we compare it to; output

for counter, char in enumerate(name[1:], 1):
    # go through every character except the first char
    if char != current:
        output += char
        current = name[counter] if len(name[1:]) > counter else ''
print(output)