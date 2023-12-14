inputFile = open("input.txt", "r")
lines = inputFile.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()


answers = []
for l in range(10000):
    for i in range(1, len(lines)):
        for j in range(len(lines[i])):
            k = 1

            flag = True
            while i - k >= 0 and flag:
                flag = False
                if lines[i - k + 1][j] == "O" and lines[i - k][j] == '.':
                    lines[i - k + 1] = lines[i - k + 1][:j] + '.' + lines[i - k + 1][j+1:]
                    lines[i - k] = lines[i - k][:j] + 'O' + lines[i - k][j+1:]
                    flag = True

                k += 1

    for i in range(len(lines)):
        for j in range(1, len(lines[i])):
            k = 1
            flag = True

            while j - k >= 0 and flag:
                flag = False
                if lines[i][j - k + 1] == "O" and lines[i][j - k] == '.':
                    lines[i] = lines[i][:j-k] + 'O.' + lines[i][j - k + 2:]
                    flag = True
                k += 1

    for i in range(len(lines) - 2, -1, -1):
        for j in range(len(lines[i])):
            k = 1
            flag = True

            while i + k < len(lines) and flag:
                flag = False
                if lines[i + k - 1][j] == "O" and lines[i + k][j] == '.':
                    lines[i + k - 1] = lines[i + k - 1][:j] + '.' + lines[i + k - 1][j+1:]
                    lines[i + k] = lines[i + k][:j] + 'O' + lines[i + k][j+1:]
                    flag = True
                k += 1

    for i in range(len(lines)):
        for j in range(len(lines[i]) - 2, -1, -1):
            k = 1
            flag = True

            while j + k < len(lines[i]) and flag:
                flag = False
                if lines[i][j + k - 1] == "O" and lines[i][j + k] == '.':
                    lines[i] = lines[i][:j+k-1] + '.O' + lines[i][j+k+1:]
                    flag = True
                k += 1

    answer = 0
    for i in range(len(lines)):
            answer += (len(lines) - i) * lines[i].count('O')

    print(l)
    print(answer)

inputFile.close()
