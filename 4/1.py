inputFile = open("input.txt", "r")
lines = inputFile.readlines()

total = 0

for line in lines:
    line = line.strip()
    numbers = line.split(":")[1].split("|")
    
    winningNumbers = numbers[0].strip().split()
    cardNumbers = numbers[1].strip().split()

    points = 0

    for number in cardNumbers:
        if number in winningNumbers:
            if points > 0:
                points = points * 2
            else:
                points += 1

    total += points

print(total)

inputFile.close()
