inputFile = open("input.txt", "r")

line = inputFile.readline()

total = 0

while line != "":
    histories = []
    histories.append(line.split())
    for i in range(len(histories[0])):
        histories[0][i] = int(histories[0][i])

    done = False
    while not done:
        done = True
        histories.append([])
        for i in range(len(histories[-2]) - 1):
            difference = histories[-2][i + 1] - histories[-2][i]
            histories[-1].append(difference)
            if difference != 0:
                done = False

    prediction = 0
    for i in range(len(histories) - 1, -1, -1):
        history = histories[i]
        prediction = history[0] - prediction
    total += prediction

    line = inputFile.readline()


print(total)

inputFile.close()
