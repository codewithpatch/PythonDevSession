#While Loop
given_list3 = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]

total6 = 0
i = -1
while given_list3[i] < 0:
    total6 += given_list3[i]
    i -= 1
print(total6)

#for loop
given_list4 = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]

total7 = 0
for i in given_list4:
    if i < 0:
        total7 += i
print(total7)