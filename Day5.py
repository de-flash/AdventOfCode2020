file = open("D5.txt", "r")
seatIDs = []
rows_remove = [64,32,16,8,4,2,1]
cols_remove = [4,2,1]
for line in file:
    row = [0,127]
    col = [0,7]
    line.strip()
    print(line)
    for i in range(7):
        if line[i] == "B":
            row[0] += rows_remove[i]
        elif line[i] == "F":
            row[1] -= rows_remove[i]
    for i in range(7, 10):
        if line[i] == "R":
            col[0] += cols_remove[i-7]
        else:
            col[1] -= cols_remove[i - 7]
    seatIDs.append(row[0] * 8 + col[0])

seatIDs = sorted(seatIDs)
print(seatIDs)
for i in range(len(seatIDs)-1):
    if seatIDs[i] + 1 != seatIDs[i+1]:
        print(seatIDs[i])

