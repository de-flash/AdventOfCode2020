file = open("D2.txt", "r")
count = 0
invalid = 0
countline = 0
for line in file:
    countline += 1
    x = line.strip().split(" ")
    rng = x[0].split("-")
    char = x[1][0]
    pw = x[2]
    if pw[int(rng[0])-1] == char and pw[int(rng[1]) - 1] != char or pw[int(rng[0])-1] != char and pw[int(rng[1]) - 1] == char:
        count += 1
        print(rng, char, pw)
    else:
        invalid += 1

print(count, invalid, countline)
file.close()