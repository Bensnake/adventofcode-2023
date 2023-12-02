inputFile = open("input.txt", "r")
lines = inputFile.readlines()

Total = 0
counter = 0

for line in lines:
    counter += 1
    count = 0
    num = ""
    for i in range(len(line)):
        char = line[i]
        if char >= "0" and char <= "9":
            if count == 0:
                num += char
            lastChar = char
            count += 1
        if i + 3 < len(line):

            if line[i:i+3] == "one":
                if count == 0:
                    num += "1"
                lastChar = "1"
                count += 1

            elif line[i:i+3] == "two":
                if count == 0:
                    num += "2"
                lastChar = "2"
                count += 1
            elif line[i:i+3] == "six":
                if count == 0:
                    num += "6"
                lastChar = "6"
                count += 1

        if i + 4 < len(line):
        
            if line[i:i+4] == "four":
                if count == 0:
                    num += "4"
                lastChar = "4"
                count += 1

            elif line[i:i+4] == "five":
                if count == 0:
                    num += "5"
                lastChar = "5"
                count += 1
            elif line[i:i+4] == "nine":
                if count == 0:
                    num += "9"
                lastChar = "9"
                count += 1

        if i + 5 < len(line):

            if line[i:i+5] == "seven":
                if count == 0:
                    num += "7"
                lastChar = "7"
                count += 1
            elif line[i:i+5] == "eight":
                if count == 0:
                    num += "8"
                lastChar = "8"
                count += 1
            
            elif line[i:i+5] == "three":
                if count == 0:
                    num += "3"
                lastChar = "3"
                count += 1

    num += lastChar
    print(counter, ", ", num)
    Total += int(num)

print(Total)

inputFile.close()
