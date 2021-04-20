file = open("D10.txt", "r")
lines = sorted(int(i) for i in file.read().splitlines())
lines.append(lines[-1]+3)
ones = 1
threes = 0

for i in range(len(lines) - 1):
    if lines[i+1] - lines[i] == 1:
        ones += 1
    if lines[i+1] - lines[i] == 3:
        threes += 1

print(threes * ones)


print(lines)
result = {0:1}
for adapt in lines:
    result[adapt] = result.get(adapt - 1, 0) + result.get(adapt - 2, 0) + result.get(adapt - 3, 0)
print(result)

