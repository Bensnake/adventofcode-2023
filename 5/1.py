inputFile = open("input.txt", "r")

line = inputFile.readline()
seeds = line.split(":")[1].strip().split()

for i in range(len(seeds)):
    seeds[i] = int(seeds[i])

locations = seeds

line = inputFile.readline()

while line != "":
    line = inputFile.readline()

    destinationLower = 0
    sourceLower = 0
    rangeLength = 0
    
    line = inputFile.readline()
    while line != "\n" and line != "":
        line = line.split()
        destinationLower = int(line[0])
        sourceLower = int(line[1])
        rangeLength = int(line[2])

        for i in range(len(locations)):
            if locations[i] >= sourceLower and locations[i] < (sourceLower + rangeLength):
                locations[i] = destinationLower + (locations[i] - sourceLower)

        line = inputFile.readline()


print(min(locations))

inputFile.close()
