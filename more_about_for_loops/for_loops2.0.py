a = ["apple", "banana", "grapes"]

for element in a:
    print(element)

for i in range(len(a)): #0, 1, 2
    for j in range(i + 1):
        # i = 0 _> j = 0
        # i = 1 _> j = 0, 1
        # i = 2 _> j = 0,1,2
        print(a[i])

total = 0
for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print(total)

