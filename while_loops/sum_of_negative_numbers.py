# Using while loop
list_num = [5, 4, 3, 2, 1, -1, -2 , -3, -4, -5]
total2 = 0
i = len(list_num) - 1
while list_num[i] < 0:
        total2 += list_num[i]
        i -= 1
print(total2)
