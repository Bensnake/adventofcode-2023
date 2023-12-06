import math

inputFile = open("input.txt", "r")

races = inputFile.readlines()
for i in range(len(races)):
    races[i] = races[i].split(":")[1].strip().replace(" ", "")
    races[i] = int(races[i])

total = 0
for j in range(races[0]):
    if ((races[0] - j) * j) > races[1]:
        total += 1

print(total)

inputFile.close()
