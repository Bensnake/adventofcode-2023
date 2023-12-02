inputFile = open("input.txt", "r")
lines = inputFile.readlines()

Total = 0

for line in lines:
    count = 0
    num = ""
    for char in line:
        if char >= "0" and char <= "9":
            if count == 0:
                num += char
            lastChar = char
            count += 1

    num += lastChar
    Total += int(num)

print(Total)

inputFile.close()
