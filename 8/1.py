inputFile = open("input.txt", "r")

instructions = inputFile.readline().strip()
inputFile.readline()

root = 'AAA'
network = {}

line = inputFile.readline()
while line != "":
    line = line.split("=")
    key = line[0].strip()
    leftRight = line[1].strip()[1:-1].split(", ")
    network.update({key: leftRight})

    line = inputFile.readline()

steps = 0
i = 0

while root != 'ZZZ':

    steps += 1

    instruction = instructions[i]

    if i == len(instructions) - 1:
        i = 0
    else:
        i += 1

    match instruction:
        case 'L':
            instruction = 0
        case 'R':
            instruction = 1

    root = network[root][instruction]
        

print(steps)
inputFile.close()
