import math

inputFile = open("input.txt", "r")

lines = inputFile.readlines()
replacedLines = [] + lines

for i in range(len(lines)):
    lines[i] = lines[i].strip()
    for j in range(len(lines[i])):
        if lines[i][j] == 'S':
            x = j
            y = i 

starts = []
instructions = ""

#if lines[y][x-1] == '-' or lines[y][x-1] == 'F' or lines[y][x-1] == 'L':
    #    starts.append([y, x-1])
if lines[y][x+1] == '-' or lines[y][x+1] == 'J' or lines[y][x+1] == '7':
    starts.append([y, x+1])
    instructions += "RR"
#if lines[y-1][x] == '|' or lines[y-1][x] == 'J' or lines[y-1][x] == 'L':
    #    starts.append([y-1, x])
#if lines[y+1][x] == '|' or lines[y+1][x] == '7' or lines[y+1][x] == 'F':
#    starts.append([y+1, x])
#    instructions += "DD"


start = starts[0]
currentPipe = start
currentPipeChar = lines[currentPipe[0]][currentPipe[1]]
previousPipe = [y, x]
while currentPipeChar != 'S':

    lines[currentPipe[0]] = lines[currentPipe[0]][:currentPipe[1]] + '#' + lines[currentPipe[0]][currentPipe[1] + 1:]

    if currentPipeChar == '-':
        if previousPipe[1] == currentPipe[1] - 1:
            nextPipe = [currentPipe[0], currentPipe[1] + 1]
            instructions += "RR"
        else:
            nextPipe = [currentPipe[0], currentPipe[1] - 1]
            instructions += "LL"
    elif currentPipeChar == '|':
        if previousPipe[0] == currentPipe[0] - 1:
            nextPipe = [currentPipe[0] + 1, currentPipe[1]]
            instructions += "DD"
        else:
            nextPipe = [currentPipe[0] - 1, currentPipe[1]]
            instructions += "UU"
    elif currentPipeChar == 'L':
        if previousPipe[1] == currentPipe[1] + 1:
            nextPipe = [currentPipe[0] - 1, currentPipe[1]]
            instructions += "UU"
        else:
            nextPipe = [currentPipe[0], currentPipe[1] + 1]
            instructions += "RR"
    elif currentPipeChar == 'J':
        if previousPipe[0] == currentPipe[0] - 1:
            nextPipe = [currentPipe[0], currentPipe[1] - 1]
            instructions += "LL"
        else:
            nextPipe = [currentPipe[0] - 1, currentPipe[1]]
            instructions += "UU"
    elif currentPipeChar == '7':
        if previousPipe[0] == currentPipe[0] + 1:
            nextPipe = [currentPipe[0], currentPipe[1] - 1]
            instructions += "LL"
        else:
            nextPipe = [currentPipe[0] + 1, currentPipe[1]]
            instructions += "DD"
    elif currentPipeChar == 'F':
        if previousPipe[0] == currentPipe[0] + 1:
            nextPipe = [currentPipe[0], currentPipe[1] + 1]
            instructions += "RR"
        else:
            nextPipe = [currentPipe[0] + 1, currentPipe[1]]
            instructions += "DD"

    previousPipe = currentPipe
    currentPipe = nextPipe
    currentPipeChar = lines[currentPipe[0]][currentPipe[1]]


lines[currentPipe[0]] = lines[currentPipe[0]][:currentPipe[1]] + '#' + lines[currentPipe[0]][currentPipe[1] + 1:]

grid = []
for i in range(len(lines) * 2):
    grid.append('.' * len(lines[0]) * 2)

start = [currentPipe[0]*2, currentPipe[1]*2]

nextUp = start
for instruction in instructions:
    match instruction:
        case 'R':
            nextUp = [nextUp[0], nextUp[1]+1]
        case 'L':
            nextUp = [nextUp[0], nextUp[1]-1]
        case 'U':
            nextUp = [nextUp[0] - 1, nextUp[1]]
        case 'D':
            nextUp = [nextUp[0] + 1, nextUp[1]]

    grid[nextUp[0]] = grid[nextUp[0]][:nextUp[1]] + '#' + grid[nextUp[0]][(nextUp[1]+1):]


def clearHorizontally(y, start):
    global grid

    upper = len(grid[y]) - 1
    x = start
    while x <= upper:
        if grid[y][x] == '.':
            grid[y] = grid[y][:x] + '*' + grid[y][x+1:]
            x += 1
        elif grid[y][x] == '*':
            x += 1
        else:
            break



    x = start
    if x == 0:
        x = upper-x

    while x > -1:
        if grid[y][x] == '.':
            grid[y] = grid[y][:x] + '*' + grid[y][x+1:]
            x -= 1
        elif grid[y][x] == '*':
            x -= 1
        else:
            break
        

def clearVertically(x, start):
    global grid

    lower = len(grid) - 1

    y = start
    while y <= lower:
        if grid[y][x] == '.':
            grid[y] = grid[y][:x] + '*' + grid[y][x+1:]
            y += 1
        elif grid[y][x] == '*':
            y += 1
        else:
            break

    y = start
    if y == 0:
        y = lower - y

    while y > -1:
        if grid[y][x] == '.':
            grid[y] = grid[y][:x] + '*' + grid[y][x+1:]
            y -= 1
        elif grid[y][x] == '*':
            y -= 1
        else:
            break

for i in range(len(grid[0])):
    clearVertically(i, 0)


for i in range(len(grid)):
    clearHorizontally(i, 0)

for k in range(30):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '*':
                clearHorizontally(i, j)
                clearVertically(j, i)

answer = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '.':
            if lines[i // 2][j // 2] not in ['#']:
                answer += 1

for line in grid:
    print(line)

for line in lines:
    print(line)

print(answer/4)

inputFile.close()
