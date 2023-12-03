inputFile = open("input.txt", "r")
lines = inputFile.readlines()

total = 0

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "*":
            adjacentNumbers = []

            aboveLine = i - 1
            belowLine = i + 1

            leftLimit = j - 1
            if (not leftLimit < 0):
                if lines[i][leftLimit].isdigit():
                    k = 0
                    numReversed = ""
                    while lines[i][leftLimit - k].isdigit():
                        numReversed += lines[i][leftLimit - k]
                        k += 1

                    num = ""
                    for k in range(1, len(numReversed) + 1):
                        num += numReversed[-k]

                    adjacentNumbers.append(int(num))
            else:
                leftLimit = j


            rightLimit = j + 1
            if (rightLimit < len(lines[i]) - 1):
                if lines[i][rightLimit].isdigit():
                    k = 0
                    num = ""
                    while lines[i][rightLimit + k].isdigit():
                        num += lines[i][rightLimit + k]
                        k += 1

                    adjacentNumbers.append(int(num))
            else:
                rightLimit = j

            if aboveLine > -1:
                previousIsDigit = False
                for k in range(leftLimit, rightLimit + 1):
                    if lines[aboveLine][k].isdigit() and (not previousIsDigit):
                        numReversed = ""
                        l = 0
                        while lines[aboveLine][k - l].isdigit():
                            numReversed += lines[aboveLine][k - l]
                            l += 1
                        num = ""
                        for l in range(1, len(numReversed) + 1):
                            num += numReversed[-l]

                        l = 1
                        while lines[aboveLine][k + l].isdigit():
                            num += lines[aboveLine][k + l]
                            l += 1

                        adjacentNumbers.append(int(num))

                        previousIsDigit = True
                    else:
                        if (not lines[aboveLine][k].isdigit()):
                            previousIsDigit = False

            if belowLine > -1:
                previousIsDigit = False
                for k in range(leftLimit, rightLimit + 1):
                    if lines[belowLine][k].isdigit() and (not previousIsDigit):
                        numReversed = ""
                        l = 0
                        while lines[belowLine][k - l].isdigit():
                            numReversed += lines[belowLine][k - l]
                            l += 1
                        num = ""
                        for l in range(1, len(numReversed) + 1):
                            num += numReversed[-l]

                        l = 1
                        while lines[belowLine][k + l].isdigit():
                            num += lines[belowLine][k + l]
                            l += 1

                        adjacentNumbers.append(int(num))

                        previousIsDigit = True
                    else:
                        if (not lines[belowLine][k].isdigit()):
                            previousIsDigit = False
                    
            if len(adjacentNumbers) == 2:
                total += (adjacentNumbers[0] * adjacentNumbers[1])

print(total)
inputFile.close()
