#Swapping Two Variables
a = 2
b = 1
print(a, b)

#Using two temporary variables
temp1 = a
temp2 = b
a = temp2
b = temp1
print(a, b)

#Using one temporary variable
temp = a
a = b
b = temp
print(a, b)
