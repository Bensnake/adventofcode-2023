inputFile = open("input.txt", "r")
initializationSequence = inputFile.readline().strip().split(",")

answer = 0
for step in initializationSequence:
    hashValue = 0
    for char in step:
        hashValue += ord(char)
        hashValue *= 17
        hashValue = hashValue % 256
    answer += hashValue

print(answer)
inputFile.close()
