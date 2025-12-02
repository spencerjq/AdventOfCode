with open("input.txt", newline='') as file:
    lines = file.readlines()
    total = 0
    gearTotal = 0
    x = 0
    y = 0
    yMax = len(lines)
    gears = {}

    while y < yMax:
        line = lines[y].replace("\r\n", "")       
        xMax = len(line)
        x = 0

        while x < xMax:
            if line[x].isdigit():
                number = str(line[x])
                checkIndexes = []

                if x > 0:
                    checkIndexes.append(x-1)

                checkIndexes.append(x)
                index = x + 1

                while index < xMax and line[index].isdigit():
                    number += str(line[index])
                    checkIndexes.append(index)
                    index += 1
                
                if index < xMax:
                    checkIndexes.append(index)

                loop = ((y > 0) * (y - 1)) + ((y == 0) * y)
                limit = loop + ((y < yMax - 1) * (3)) + ((y >= yMax - 1) * 2)
                valid = 0

                while loop < limit:
                    for checkIndex in checkIndexes:
                        valid = valid or (int(not lines[loop][checkIndex].isalnum() and lines[loop][checkIndex] != '.'))

                        if valid and lines[loop][checkIndex] == "*":
                            key = str(loop) + "," + str(checkIndex)

                            if key in gears:
                                gears[key].append(int(number))
                            else:
                                gears[key] = [int(number)]

                    loop += 1
                total += (valid * int(number))
                x = index -1
            x += 1
        y += 1

    for gear in gears.values():
        if len(gear) == 2:
            gearTotal += gear[0] * gear[1]
    
    print("total ", total)
    print("gearTotal", gearTotal)