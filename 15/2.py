inputFile = open("input.txt", "r")
initializationSequence = inputFile.readline().strip().split(",")

def hashAlgo(label):
    hashValue = 0
    for char in label:
        hashValue += ord(char)
        hashValue *= 17
        hashValue = hashValue % 256
    return hashValue

boxes = dict.fromkeys([i for i in range(256)])

answer = 0
for step in initializationSequence:
    hashValue = 0
    if step.find('=') != -1:
        step = step.split('=')
        boxNumber = hashAlgo(step[0])
        box = boxes[boxNumber]
        changed = False
        if box != None:
            for i in range(len(box)):
                if box[i][0] == step[0]:
                    boxes[boxNumber] = box[:i] + [[step[0], int(step[1])]] + box[i+1:]
                    changed = True
            if not changed:
                boxes[boxNumber] += [[step[0], int(step[1])]]
        else:
            boxes[boxNumber] = [[step[0], int(step[1])]]
    else:
        step = step.rstrip('-')
        boxNumber  = hashAlgo(step)
        box = boxes[boxNumber]
        if box != None:
            for i in range(len(box)):
                if box[i][0] == step:
                    boxes[boxNumber] = box[:i] + box[i+1:]

for i in range(len(boxes)):
    if boxes[i] != None:
        for j in range(len(boxes[i])):
            answer += (i+1) * (j+1) * boxes[i][j][1]

print(answer)
inputFile.close()
