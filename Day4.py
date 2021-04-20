import re
file = open("D4.txt", "r")
valid = 0
count = 0
keys = 0
for line in file:
    line = line.strip().split(" ")
    if line == ['']:
        if keys == 7:
            valid += 1
        keys = 0
    else:
        for m in line:
            m = m.split(":")
            if m[0] == "byr" and 1920 <= int(m[1]) <= 2002:
                keys += 1
            if m[0] == "iyr" and 2010 <= int(m[1]) <= 2020:
                keys += 1
            if m[0] == "eyr" and 2020 <= int(m[1]) <= 2030:
                keys += 1
            if m[0] == "hgt" and ((m[1][-2:] == "in" and 59 <= int(m[1][:-2]) <= 76) or (m[1][-2:] == "cm" and 150 <= int(m[1][:-2]) <= 193)):
                keys += 1
            if m[0] == "hcl" and m[1][0] == "#":
                keys += 1
            if m[0] == "ecl" and m[1] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                keys += 1
            if m[0] == "pid" and m[1].isdigit() and len(m[1]) == 9:
                print(m[1], m[1].isdigit())
                keys += 1


print(valid)