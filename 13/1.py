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
        if pattern[i] == pattern[i + 1] and pattern[i + 1] != '\n':
            flag = True
            j = 2
            while (i+j) < len(pattern) and (i-j+1) > -1:
                if pattern[i+j] != pattern[i-j+1]:
                    flag = False

                j += 1

            if flag:
                answer += 100 * (i + 1)

    verticals = []
    for i in range(len(pattern[0])):
        line = []
        for j in range(len(pattern)):
            line.append(pattern[j][i])

        verticals.append(line)

    for i in range(len(verticals) - 1):
        if verticals[i] == verticals[i+1]:
            flag = True
            j = 2
            while (i+j) < len(verticals) and (i-j+1) > -1:
                if verticals[i+j] != verticals[i-j+1]:
                    flag = False
                j += 1

            if flag:
                answer += i+1

print(answer)
inputFile.close()
