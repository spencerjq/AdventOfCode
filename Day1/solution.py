import csv
import re

#Function for Part 2
def replace_num(row, num, dig):
    sample = row
    index = 0
    count = 0
    newnum = ""

    while index > -1:
        index = row.find(num, index)
        
        if index > -1:
            sample = sample[:index+count+1] + dig + sample[index+count+1:]
            index = index + len(num)
            print(sample)
            count = count + 1

    return sample

with open("input.txt", newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    total = 0
    
    for row in reader:
        sample = str(row)
        #Answer for Part 2
        """
        sample = replace_num(sample, "nine", "9")
        sample = replace_num(sample, "eight", "8")
        sample = replace_num(sample, "seven", "7")
        sample = replace_num(sample, "six", "6")
        sample = replace_num(sample, "five", "5")
        sample = replace_num(sample, "four", "4")
        sample = replace_num(sample, "three", "3")
        sample = replace_num(sample, "two", "2")
        sample = replace_num(sample, "one", "1") """
        
        num = re.sub("[^0-9]", "", str(sample))
        sub = (int(num[0])*10) + int(num[len(num)-1])
        total += sub

    print(total)
