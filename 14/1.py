inputFile = open("input.txt", "r")
lines = inputFile.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()

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

answer = 0
for i in range(len(lines)):
    answer += (len(lines) - i) * lines[i].count('O')

print(answer)
inputFile.close()
