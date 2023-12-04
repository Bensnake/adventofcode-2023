inputFile = open("input.txt", "r")
lines = inputFile.readlines()

total = 0

cards = []

def readCard(cardNumber):
    global total

    total += 1
    wins = 0

    for number in cards[cardNumber - 1][0]:
        if number in cards[cardNumber - 1][1]:
            wins += 1

    if wins == 0:
        return
    else:
        for i in range(1, wins + 1):
            readCard(cardNumber + i)


for line in lines:
    line = line.strip()
    numbers = line.split(":")[1].split("|")
    
    winningNumbers = numbers[0].strip().split()
    cardNumbers = numbers[1].strip().split()

    cards.append([winningNumbers, cardNumbers])



for i in range(1, len(cards) + 1):
    readCard(i)

print(total)

inputFile.close()
