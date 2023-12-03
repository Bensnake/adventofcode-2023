inputFile = open("input.txt", "r")
lines = inputFile.readlines()

total = 0

for i in range(len(lines)):
    previousIsDigit = False
    for j in range(len(lines[i])):
        if lines[i][j].isdigit() and (not previousIsDigit):
            symbol = False
            numberLength = 1
            while lines[i][j + numberLength].isdigit():
                numberLength += 1

            aboveLine = i - 1
            belowLine = i + 1

            leftLimit = j - 1
            if leftLimit < 0:
                leftLimit = 0

            rightLimit = j + numberLength
            if rightLimit >= len(lines[i]) - 1:
                rightLimit = len(lines[i]) - 2

            if ((not lines[i][leftLimit].isdigit()) and lines[i][leftLimit] != ".") or ((not lines[i][rightLimit].isdigit()) and lines[i][rightLimit] != "."):
                symbol = True

            if aboveLine > -1 and (not symbol):
                for k in range(leftLimit, rightLimit + 1):
                    if (not lines[aboveLine][k].isdigit()) and lines[aboveLine][k] != ".":
                        symbol = True
                        break

            if belowLine < len(lines) and (not symbol):
                for k in range(leftLimit, rightLimit + 1):
                    if (not lines[belowLine][k].isdigit()) and lines[belowLine][k] != ".":
                        symbol = True
                        break

            if symbol:
                number = lines[i][j]
                for k in range(1, numberLength):
                    number += lines[i][j + k]

                total += int(number)

            previousIsDigit = True
        else:
            if (not lines[i][j].isdigit()):
                previousIsDigit = False

print(total)
inputFile.close()
