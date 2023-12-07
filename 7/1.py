inputFile = open("input.txt", "r")
hands = inputFile.readlines()


handsByType = [[], [], [], [], [], [], []]

def sortHand(hand, value):
    cards = []

    for i in range(len(hand)):
        alreadyRecorded = False

        for j in range(len(cards)):
            if cards[j][0] == hand[i]:
                alreadyRecorded = True

        if not alreadyRecorded:
            copies = 1
            for j in range(i + 1, len(hand)):
                if hand[j] == hand[i]:
                    copies += 1
            
            cards.append([hand[i], copies])

    pairs = 0
    triples = 0
    fours = 0
    fives = 0

    for card in cards:
        match card[1]:
            case 2:
                pairs += 1
            case 3:
                triples += 1
            case 4:
                fours += 1
            case 5:
                fives += 1

    if fives == 1:
        handsByType[6].append([hand, value])
    elif fours == 1:
        handsByType[5].append([hand, value])
    elif triples == 1 :
        if pairs == 1:
            handsByType[4].append([hand, value])
        else:
            handsByType[3].append([hand, value])
    elif pairs == 2:
        handsByType[2].append([hand, value])
    elif pairs == 1:
        handsByType[1].append([hand, value])
    else:
        handsByType[0].append([hand, value])


for i in range(len(hands)):
    hands[i] = hands[i].split()
    hands[i][1] = int(hands[i][1])
    
    handType = sortHand(hands[i][0], hands[i][1])

for i in range(len(handsByType)):

    j = 0
    swap = True

    while (j < (len(handsByType[i]) - 1) and swap):
        swap = False
        for k in range(len(handsByType[i]) - j - 1):

            for l in range(len(handsByType[i][k][0])):
                card = handsByType[i][k][0][l]
                nextHandCard = handsByType[i][k + 1][0][l]

                match card:
                    case 'T':
                        card = '10'
                    case 'J':
                        card = '11'
                    case 'Q':
                        card = '12'
                    case 'K':
                        card = '13'
                    case 'A':
                        card = '14'

                match nextHandCard:
                    case 'T':
                        nextHandCard = '10'
                    case 'J':
                        nextHandCard = '11'
                    case 'Q':
                        nextHandCard = '12'
                    case 'K':
                        nextHandCard = '13'
                    case 'A':
                        nextHandCard = '14'

                card = int(card)
                nextHandCard = int(nextHandCard)

                if card < nextHandCard:
                    break
                elif card > nextHandCard:
                    temp = handsByType[i][k]
                    handsByType[i][k] = handsByType[i][k + 1]
                    handsByType[i][k + 1] = temp

                    swap = True
                    break
        j += 1


rank = 1
total = 0
for handType in handsByType:
    for hand in handType:
        total += (rank * hand[1])
        rank += 1



print(total)

inputFile.close()
