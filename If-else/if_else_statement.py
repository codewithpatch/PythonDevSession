a = 100
b = 30

if a > b:
    print("a is greater than b")
    print("a is definitely greater than b")
print("Not sure if a is greater than b", "\n", "\n")

c = 50
d = 40

if c < d:
    print("c is less than d", "\n", "\n")
else:
    print("c is NOT less than d")
    print("I dont think c is less than d")
print("outside the if block", "\n", "\n")

e = 90
f = 70

if e < f:
    print("e is less than f", "\n", "\n")
elif e == f:
    print("e is equal to f", "\n", "\n")
elif e > f + 10:
    print("e is greater than f by more than ten", "\n", "\n")
else:
    print("e is greater than f", "\n", "\n")

g = 7
h = 8
if g < h:
    print("g is less than h", "\n", "\n")
else:
    if g == h:
        print("g is equal to h", "\n", "\n")
    else:
        print("g is greater than h", "\n", "\n")