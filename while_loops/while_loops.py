# Sum all the numbers using while loop
total = 0
j = 1
while j < 5:
    total += j
    j += 1
print(total)

given_list = [5, 1, 1, 1, 5, -1 , 1, 3, -4]
total1 = 0
i = 0
while given_list[i] > 0:
    total1 += given_list[i]
    i += 1
print(total1)

# Using break statement
# Break in For Loop
list = [5, 4, 3, 2, 1, -1, -2, -3, -4, -5]
total2 = 0
for i in list:
    if i <= 0:
        break
    total2 += i
print(total2)

# Break in While Loop
list2 = [5, 4, 3, 2, 1, -1, -2, -3, -4, -5]
total4 = 0
i = 0

while True:
    total4 += list2[i]
    i += 1
    if list2[i] <= 0:
        break
print(total4)