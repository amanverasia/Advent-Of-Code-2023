data = []
with open("Day 1/input.txt") as f:
    lines = f.readlines()
    for line in lines:
        data.append(line.rstrip("\n"))


sum = 0
for i in (data):
    # print(i)
    number = []
    for j in i:
        mini_sum = 0
        if j.isdigit():
            number.append(j)
    mini_sum = number[0] + number[-1]
    sum += int(mini_sum)
print(sum)