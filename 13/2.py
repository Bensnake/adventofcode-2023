inputFile = open("input.txt", "r")
lines = inputFile.readlines()
patterns = []

pattern = []
for i in range(len(lines)):
    if lines[i] == '\n':
        patterns.append(pattern)
        pattern = []
    else:
        pattern.append(lines[i].strip())

patterns.append(pattern)

answer = 0
for pattern in patterns:
    for i in range(len(pattern) - 1):
        differences = 0

        for j in range(len(pattern[i])):
            if pattern[i][j] != pattern[i+1][j]:
                differences += 1

        if differences < 2:
            j = 2
            while (i+j) < len(pattern) and (i-j+1) > -1:
                for k in range(len(pattern[i+j])):
                    if pattern[i+j][k] != pattern[i-j+1][k]:
                        differences += 1


                j += 1

            if differences == 1:
                answer += 100 * (i + 1)

    verticals = []
    for i in range(len(pattern[0])):
        line = []
        for j in range(len(pattern)):
            line.append(pattern[j][i])

        verticals.append(line)

    for i in range(len(verticals) - 1):
        differences = 0

        for j in range(len(verticals[i])):
            if verticals[i][j] != verticals[i+1][j]:
                differences += 1

        if differences < 2:
            j = 2
            while (i+j) < len(verticals) and (i-j+1) > -1:
                for k in range(len(verticals[i+j])):
                    if verticals[i+j][k] != verticals[i-j+1][k]:
                        differences += 1
                j += 1

            if differences == 1:
                answer += i+1

print(answer)
inputFile.close()
