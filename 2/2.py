inputFile = open("input.txt", "r")
lines = inputFile.readlines()

Total = 0

for line in lines:
    possible = True
    game = line.split(":")[1].split(";")

    blueRequired = 0
    greenRequired = 0
    redRequired = 0

    for i in range(len(game)):
        colours = game[i].split(",")

        for i in range(len(colours)):
            colours[i] = colours[i].strip()
            if colours[i][1] >= "0" and colours[i][1] <= "9":
                num = int(colours[i][:2])
                if len(colours[i]) == 7:
                    if(num) > blueRequired:
                        blueRequired = num

                elif len(colours[i]) == 8:
                    if(num) > greenRequired:
                        greenRequired = num

                elif len(colours[i]) == 6:
                    if(num) > redRequired:
                        redRequired = num

            else:
                num = int(colours[i][0])
                if len(colours[i]) == 6:
                    if(num) > blueRequired:
                        blueRequired = num

                elif len(colours[i]) == 7:
                    if(num) > greenRequired:
                        greenRequired = num

                elif len(colours[i]) == 5:
                    if(num) > redRequired:
                        redRequired = num

    Total += (blueRequired * greenRequired * redRequired)

print(Total)

inputFile.close()
