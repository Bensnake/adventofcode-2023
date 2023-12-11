import math

inputFile = open("input.txt", "r")

lines = inputFile.readlines()

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == 'S':
            x = j
            y = i 

starts = []

if lines[y][x-1] == '-' or lines[y][x-1] == 'F' or lines[y][x-1] == 'L':
    starts.append([y, x-1])
if lines[y][x+1] == '-' or lines[y][x+1] == 'J' or lines[y][x+1] == '7':
    starts.append([y, x+1])
if lines[y-1][x] == '|' or lines[y-1][x] == 'J' or lines[y-1][x] == 'L':
    starts.append([y-1, x])
if lines[y+1][x] == '|' or lines[y+1][x] == '7' or lines[y+1][x] == 'F':
    starts.append([y+1, x])

answer = 0
for start in starts:
    currentPipe = start
    currentPipeChar = lines[currentPipe[0]][currentPipe[1]]
    previousPipe = [y, x]
    steps = 0
    while currentPipeChar != 'S':
        steps += 1

        if currentPipeChar == '-':
            if previousPipe[1] == currentPipe[1] - 1:
                nextPipe = [currentPipe[0], currentPipe[1] + 1]
            else:
                nextPipe = [currentPipe[0], currentPipe[1] - 1]
        elif currentPipeChar == '|':
            if previousPipe[0] == currentPipe[0] - 1:
                nextPipe = [currentPipe[0] + 1, currentPipe[1]]
            else:
                nextPipe = [currentPipe[0] - 1, currentPipe[1]]
        elif currentPipeChar == 'L':
            if previousPipe[1] == currentPipe[1] + 1:
                nextPipe = [currentPipe[0] - 1, currentPipe[1]]
            else:
                nextPipe = [currentPipe[0], currentPipe[1] + 1]
        elif currentPipeChar == 'J':
            if previousPipe[0] == currentPipe[0] - 1:
                nextPipe = [currentPipe[0], currentPipe[1] - 1]
            else:
                nextPipe = [currentPipe[0] - 1, currentPipe[1]]
        elif currentPipeChar == '7':
            if previousPipe[0] == currentPipe[0] + 1:
                nextPipe = [currentPipe[0], currentPipe[1] - 1]
            else:
                nextPipe = [currentPipe[0] + 1, currentPipe[1]]
        elif currentPipeChar == 'F':
            if previousPipe[0] == currentPipe[0] + 1:
                nextPipe = [currentPipe[0], currentPipe[1] + 1]
            else:
                nextPipe = [currentPipe[0] + 1, currentPipe[1]]

        previousPipe = currentPipe
        currentPipe = nextPipe
        currentPipeChar = lines[currentPipe[0]][currentPipe[1]]

    if steps > answer:
        answer = steps

print(math.ceil(answer / 2))

inputFile.close()
