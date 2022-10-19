
given_list = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]

total2 = 0
j = len(given_list) - 1
while given_list[j] < 0:
    total2 += given_list[j]
    j -= 1
print(total2)

