inputFile = open("input.txt", "r")

line = inputFile.readline()
seeds = line.split(":")[1].strip().split()
temp = []

for i in range(0, len(seeds), 2):
    temp.append([int(seeds[i]), int(seeds[i + 1])])

seeds = temp

line = inputFile.readline()

def getNextMap(file):
    nextMap = []

    line = file.readline()
    line = file.readline()

    while line != "\n" and line != "":
        line = line.split()
        for i in range(len(line)):
            line[i] = int(line[i])

        nextMap.append(line)

        line = file.readline()

    return nextMap


def findDestinations(source):
    global thisMap

    destinations = []

    Ls = source[0]
    Us = source[0] + source[1]

    flag = False

    for element in thisMap:
        Lm = element[1]
        Um = element[1] + element[2]
        destVal = element[0]

        if Ls >= Lm and Ls < Um and Us > Lm and Us <= Um:
            nextLower = Ls - Lm + destVal
            destinations.append([nextLower, source[1]])

            flag = True
            break
        elif Ls < Lm and Us > Lm and Us <= Um:
            nextLower = destVal
            destinations.append([nextLower, (Us - Lm)])
            destinations += (findDestinations([Ls, (Lm - Ls)]))

            flag = True
            break
        elif Ls >= Lm and Ls < Um and Us > Um:
            nextLower = Ls - Lm + destVal
            destinations.append([(Ls - Lm + destVal), (Um - Ls)])
            destinations += (findDestinations([Um, (Us - Um)]))

            flag = True
            break
        elif Ls < Lm and Us > Um:
            destinations.append([destVal, (Um - Lm)])
            destinations += (findDestinations([Ls, (Lm - Ls)]))
            destinations += (findDestinations([Um, (Us - Um)]))
            
            flag = True
            break

    if not flag:
        destinations.append(source)

    return destinations 



old = seeds
new = []

thisMap = getNextMap(inputFile)
while thisMap != []:
    new = []
    for i in old:
        new += findDestinations(i)

    old = new
    thisMap = getNextMap(inputFile)


new.sort()
print(min(new)[0])

inputFile.close()
