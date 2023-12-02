redTotal = 12
greenTotal = 13
blueTotal = 14

inputFile = open("input.txt", "r")
lines = inputFile.readlines()
currentGame = 1

Total = 0

for line in lines:
    possible = True
    game = line.split(":")[1].split(";")

    for i in range(len(game)):
        colours = game[i].split(",")

        for i in range(len(colours)):
            colours[i] = colours[i].strip()
            if colours[i][1] >= "0" and colours[i][1] <= "9":
                if len(colours[i]) == 7:
                    if(int(colours[i][:2])) > blueTotal:
                        possible = False
                        break
                elif len(colours[i]) == 8:
                    if(int(colours[i][:2])) > greenTotal:
                        possible = False
                        break
                elif len(colours[i]) == 6:
                    if(int(colours[i][:2])) > redTotal:
                        possible = False
                        break
            else:
                if len(colours[i]) == 6:
                    if(int(colours[i][0])) > blueTotal:
                        possible = False
                        break
                elif len(colours[i]) == 7:
                    if(int(colours[i][0])) > greenTotal:
                        possible = False
                        break
                elif len(colours[i]) == 5:
                    if(int(colours[i][0])) > redTotal:
                        possible = False
                        break 
        
    if possible:
        Total += currentGame

    currentGame += 1

print(Total)

inputFile.close()
