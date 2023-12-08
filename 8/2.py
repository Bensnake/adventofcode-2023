import math

inputFile = open("input.txt", "r")

instructions = inputFile.readline().strip()
inputFile.readline()

roots = []
network = {}

line = inputFile.readline()
while line != "":
    line = line.split("=")
    key = line[0].strip()
    leftRight = line[1].strip()[1:-1].split(", ")
    network.update({key: leftRight})

    line = inputFile.readline()

for key in network.keys():
    if key[-1] == 'A':
        roots.append(key)

steps = 0
Z = []
i = 0

while roots != []:

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

    toRemove = []
    for j in range(len(roots)):
        roots[j] = network[roots[j]][instruction]
        if roots[j][-1] == 'Z':
            toRemove.append(roots[j])

    for item in toRemove:
        roots.remove(item)
        Z.append(steps)
        
answer = 1
for number in Z:
    answer = (math.lcm(answer, number))

print(answer)

inputFile.close()
