a = [1, 3, 5, 7, 9, 11]
print(a)

c = []
for x in a:
    c.append(x * 2)
print(c)

d = [x * 2 for x in a]
print(d)

e = list(range(1,10))
f = [x ** 2 for x in e]
print(f)

g = [x ** 2 for x in range(1, 7)]
print(g)

a1 = [x ** 2 for x in range(6, 0, -1)]
print(a1)