#Swapping a List

a = ["I", "Love", "You"]
print(a)

temp = a[0]
a[0] = a[2]
a[2] = temp
print(a)

a[0], a[2] = a[2], a[0]
print(a)
