data = []
with open("Day 1/input.txt") as f:
    lines = f.readlines()
    for line in lines:
        data.append(line.rstrip("\n"))

# print(data)

digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

numbers = []
print("Data before: ", data)
for line in range(len(data)):
    
    for stuff in digits:
        if stuff in data[line]:
            data[line] = data[line].replace(stuff, str(digits.index(stuff)+1))
            # new_data.append(data[line])

print("Data after: ", data)


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


# for line in data:
#     print(line)
#     for stuff in digits:
#         if stuff in line:
#             numbers.append(stuff)       
#     for x in range(line.index(numbers[0])):
#         if line[x].isdigit():
#             print(line[x])
    
#     for x in range(line.index(numbers[-1]), len(line)):
#         if line[x].isdigit():
#             print(line[x])
    
#     break

# print(numbers)


# numbers = []
# maybe_number = ''
# print(data[0])
# for j in data[0]:
#     if j.isdigit():
#         #print(j)
#         numbers.append(j)


# print(numbers)
# print(maybe_number)

























# numbers = []
# for i in data:
#     print(i)
#     for j in digits:
#         if j in i:
#             numbers.append(j)
#             # print(j)
#     for j in i:
#         if j.isdigit():
#             numbers.append(j)
#             # print(j)
#     indexing = []
#     for stuff in numbers:
#         # print(stuff)
#         indexing.append(i.index(stuff))

#     indexing.sort()
#     for j in indexing:
#         print(i[j])
#     break



#Convert to actual digits
# for i in numbers:
#     print(digits.index(i)+1)