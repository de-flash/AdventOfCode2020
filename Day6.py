file = open("D6.txt", "r")
answers = []
chars = "qwertyuiopasdfghjklzxcvbnm"
total = 0
for line in file:
    line = line.strip("\n")
    if len(line) == 0:
        for c in chars:
            check = True
            for ans in answers:
                if c not in ans:
                    check = False
            if check:
                total += 1
        answers = []
    else:
        answers.append(line)
print(total, answers)