file = open("D3.txt", "r")
lines = file.read().split("\n")
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
col = 0
for i in range(len(lines)):
    if lines[i][col % len(lines[i])] == "#":
        count1 += 1
    col += 1
print(count1)

col = 0
for i in range(len(lines)):
    if lines[i][col % len(lines[i])] == "#":
        count2 += 1
    col += 3
print(count2)

col = 0
for i in range(len(lines)):
    if lines[i][col % len(lines[i])] == "#":
        count3 += 1
    col += 5
print(count3)

col = 0
for i in range(len(lines)):
    if lines[i][col % len(lines[i])] == "#":
        count4 += 1
    col += 7
print(count4)

col = 0
for i in range(0, len(lines), 2):
    if lines[i][col % len(lines[i])] == "#":
        count5 += 1
    col += 1
print(count5)

print(count1 * count2 * count3 * count4 * count5)
file.close()