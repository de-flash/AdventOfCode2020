file = open("D8.txt", "r")
lines = [line.split() for line in file.read().splitlines()]
length = 626
acc = 0
pointer = 0
used = []

for i in range(length):
    acc = 0
    used = []
    lines[223][0] = "nop"
    while True:
        if pointer % length in used:
            break
        used.append(pointer % length)
        if lines[pointer % length][0] == "acc":
            acc += int(lines[pointer % length][1])
            pointer += 1
        if lines[pointer % length][0] == "jmp":
            pointer += int(lines[pointer % length][1])
        if lines[pointer % length][0] == "nop":
            pointer += 1
    print(acc)



