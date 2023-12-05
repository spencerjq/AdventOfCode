with open("input.txt", newline='') as file:
    lines = file.readlines()
    total = 0
    copies = {}
    index = 1

    for line in lines:
        line = line.replace("\r\n", "")
        winners = list(filter(("").__ne__,line.split("|")[0].split(":")[1].split(" ")))
        winners = [eval(i) for i in winners]
        winners.sort()

        matchers = list(filter(("").__ne__,line.split("|")[1].split(" ")))
        matchers = [eval(i) for i in matchers]
        matchers.sort()

        score = 0
        copy = 0

        i = 0
        j = 0

        while i < len(winners):
            while j < len(matchers):
                if winners[i] < matchers[j]:
                    break
                elif winners[i] == matchers[j]:
                    if score == 0:
                        score = 1
                    else:
                        score *= 2
                    copy += 1
                j += 1
            i += 1
        total += score
        
        if index in copies:
            copies[index] += 1
        else:
            copies[index] = 1

        if copy > 0:
            copyCount = 0

            if index in copies:
                copyCount += copies[index]

            i = 0
            j = 0

            for j in range(copy):
                j += index + 1

                if j < len(lines) + 1:
                    if j in copies:
                        copies[j] += copyCount
                    else:
                        copies[j] = copyCount
        index += 1

    print("total ", total)
    print("scratch offs ", sum(copies.values()))