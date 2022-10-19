a = [1, 3, 5, 7, 9, 11]
# [2, 6, 10, 14, 18, 22]
# a.append()

b = []
b.append(10)
b.append(20)
print(b)

c = []
for x in a:
    c.append(x * 2)
print(c)

d = []
for x in a:
    d.append(x * 2)
print(d)

# [1, 4, 9, 16, 25, 36]
el = []
for x in range(1, 7):
    el.append(x ** 2)
print(el)

e2 = [x ** 2 for x in range(1, 7)]
print(e2)

# [36, 25, 16, 9, 4, 1]
for x in range(6, 0, -1):
    print(x)

fl = []
for x in range(6, 0, -1):
    fl.append(x**2)
print(fl)

f2 = [x**2 for x in range(6, 0, -1)]
print(f2)
