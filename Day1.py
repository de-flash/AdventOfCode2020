file = open("D1.txt", "r")
nums = file.readlines()

for m in nums:
    for n in nums:
        for x in nums:
            if int(m) + int(n) + int(x) == 2020:
                print(int(m) * int(n) * int(x))
