with open("input.txt", newline='') as file:
    lines = file.readlines()

    gameSums = 0
    powerSums = 0

    # Part 1
    redLimit = 12
    greenLimit = 13
    blueLimit = 14

    for line in lines:
        line = line.replace("\r\n", "")

        # Part 2
        redPower = 0
        greenPower = 0
        bluePower = 0

        game = int(line.split(":")[0].replace("Game", ""))
        valid = 1

        for round in line.split(":")[1].split(";"):
            for color in round.split(","):
                if color.find("red") > -1:
                    num = int(color.replace("red", ""))
                    valid = valid * (num <= redLimit)
                    redPower = ((num > redPower) * num) + ((num <= redPower) * redPower)
                elif color.find("green") > -1:
                    num = int(color.replace("green", ""))
                    valid = valid * (num <= greenLimit)
                    greenPower = ((num > greenPower) * num) + ((num <= greenPower) * greenPower)
                elif color.find("blue") > -1:
                    num = int(color.replace("blue", ""))
                    valid = valid * (num <= blueLimit)
                    bluePower = ((num > bluePower) * num) + ((num <= bluePower) * bluePower)
        gameSums += (valid * game)
        powerSums += (redPower * greenPower * bluePower)
    print("GameSums: ", gameSums)
    print("PowerSums: ", powerSums)

                

