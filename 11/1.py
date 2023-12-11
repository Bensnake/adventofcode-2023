inputFile = open("input.txt", "r")
cluster = inputFile.readlines()
tempCluster = []

for i in range(len(cluster)):
    cluster[i] = cluster[i].strip()
    galaxies = 0
    for j in range(len(cluster[i])):
        if cluster[i][j] == '#':
            galaxies += 1

    tempCluster.append(cluster[i])
    if galaxies == 0:
        tempCluster.append(cluster[i])

cluster = [] + tempCluster

i = 0
j = len(cluster[0])
while i < j:
    galaxies = 0
    for k in range(len(cluster)):
        if cluster[k][i] == '#':
            galaxies += 1

    if galaxies == 0:
        for k in range(len(cluster)):
            cluster[k] = cluster[k][:i + 1] + '.' + cluster[k][i + 1:]

        i += 1
        j += 1


    i += 1


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

        total += (y1 - y2) + (x1 - x2)

print(total)

inputFile.close()
