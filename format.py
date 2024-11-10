# split each sentence to a new line
def formatResponse(lines):
    for line in lines: line.replace('.', '.\n')
    return lines

file = open('./Torah/וירא.txt', 'r')

print(file.read())
