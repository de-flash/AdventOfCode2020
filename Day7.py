from collections import deque
import re
file = open("D7.txt", "r")
lines = file.readlines()
file.close()


def part1(lines):
    count = 0
    checked = ["shiny gold bag"]
    queue = deque(["shiny gold bag"])
    while len(queue) != 0:
        color = queue.pop()
        checked.append(color)
        for line in lines:
            line = line.split("s contain")
            if color in line[1]:
                if line[0] not in checked:
                    queue.append(line[0])
                    count += 1
    print(count)


def part2(lines, bag):
    count = 0
    checked = []
    bags = deque([bag])
    bag_amount = deque([1])
    while len(bags) != 0:
        color = bags.popleft()
        amount = bag_amount.popleft()
        checked.append(color)
        for line in lines:
            line = line.split("bags contain")
            if color in line[0]:
                cols = re.findall(r"\d+ \w+ \w+", line[1])
                checked.append(cols)
                for m in cols:
                    count += int(m[:2]) * amount
                    bag_amount.append(int(m[:2]) * amount)
                    bags.append(m[2:])
    return count

print(part2(lines, "shiny gold"))
