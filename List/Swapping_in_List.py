a = ["I", "am", "sorry"]
print(a)

temp1 = a[0]
a[0] = a[1]
a[1] = temp1

print(a)

a[0], a[1] = a[1], a[0]
print(a)