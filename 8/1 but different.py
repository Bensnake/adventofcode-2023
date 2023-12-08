inputFile = open("input.txt", "r")

instructions = inputFile.readline().strip()
inputFile.readline()

network = []
root = 'AAA'

line = inputFile.readline()
while line != "":
    line = line.split("=")
    key = line[0].strip()
    leftRight = line[1].strip()[1:-1].split(", ")
    network.append([leftRight[0], key, leftRight[1]])

    line = inputFile.readline()


i = 0
swap = True
while (i < (len(network) - 1) and swap):
    swap = False
    for j in range(len(network) - i - 1):

        for k in range(len(network[j][1])):
            if network[j][1][k] < network[j + 1][1][k]:
                break
            elif network[j][1][k] > network[j + 1][1][k]:
                temp = network[j]
                network[j] = network[j + 1]
                network[j + 1] = temp

                swap = True
                break
    i += 1

def binarySearch(item):
    global network

    low = 0
    high = len(network) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if network[mid][1] < item:
            low = mid + 1
        elif network[mid][1] > item:
            high = mid - 1
        else:
            return network[mid]

    return []

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
            instruction = 2

    currentNode = binarySearch(root)
    root = currentNode[instruction]

print(steps)
inputFile.close()
