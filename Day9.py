file = open("D9.txt", "r")
lines = [int(line) for line in file.read().splitlines()]


def findS(pole, s, min, max):
    if pole[min] == pole[max]:
        return False
    if pole[min] + pole[max] == s:
        return True
    if pole[min] + pole[max] > s:
        return findS(pole, s, min, max - 1)
    if pole[min] + pole[max] < s:
        return findS(pole, s, min+1, max)


target = 70639851


for i in range(len(lines)):
    checked = []
    target = 70639851
    wi = 0
    while target > 0 and i + wi < len(lines):
        target -= lines[i + wi]
        checked.append(lines[i+ wi])
        wi += 1
    if target == 0:
        print(sorted(checked))





