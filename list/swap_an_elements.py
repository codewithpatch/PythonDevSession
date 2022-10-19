# Swap two elements
list = [1, 2, 3]

# Solution
temp = list[0]
list[0] = list[2]
list[2] = temp
print(list)

# Another Solution
list[0], list[2] = list[2], list[0]
print(list)
