inputFile = open("input.txt", "r")
cluster = inputFile.readlines()

for i in range(len(cluster)):
    cluster[i] = cluster[i].strip()
    galaxies = 0
    for j in range(len(cluster[i])):
        if cluster[i][j] == '#':
            galaxies += 1

    if galaxies == 0:
        cluster[i] = '!'*len(cluster[i])

for i in range(len(cluster[0])):
    galaxies = 0
    for j in range(len(cluster)):
        if cluster[j][i] == '#':
            galaxies += 1

    if galaxies == 0:
        for j in range(len(cluster)):
            cluster[j] = cluster[j][:i] + '!' + cluster[j][i + 1:]


galaxies = []
for i in range (len(cluster)):
    for j in range(len(cluster[i])):
        if cluster[i][j] == '#':
            galaxies.append([i, j])

total = 0
for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        y1 = max([galaxies[i][0], galaxies[j][0]])
        y2 = min([galaxies[i][0], galaxies[j][0]])
        x1 = max([galaxies[i][1], galaxies[j][1]])
        x2 = min([galaxies[i][1], galaxies[j][1]])

        for k in range(y2, y1):
            total += 1
            if cluster[k][x1] == '!':
                total += 999999

        for k in range(x2, x1):
            total += 1
            if cluster[y1][k] == '!':
                total += 999999


print(total)

inputFile.close()
