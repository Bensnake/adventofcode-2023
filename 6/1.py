import math

inputFile = open("input.txt", "r")

races = inputFile.readlines()
for i in range(len(races)):
    races[i] = races[i].split(":")[1].split()
    for j in range(len(races[i])):
        races[i][j] = int(races[i][j])

product = 1
for i in range(len(races[0])):
    total = 0
    for j in range(races[0][i]):
        if ((races[0][i] - j) * j) > races[1][i]:
            total += 1

    product *= total

print(product)

inputFile.close()
