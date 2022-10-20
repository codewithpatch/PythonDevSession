# Reject duplicate elements
a = set()
print(a)

a.add(1)
print(a)
a.add(2)
print(a)
a.add(2)
print(a, "won't duplicate 2")

for x in a:
    print(x)

list1 = [1, 1, 2, 2, 3, 3]
print(list1)
# Remove duplicate elements in the List
new_set = set()
for x in list1:
    new_set.add(x)
print(new_set)

new_list = list()
for x in new_set:
    new_list.append(x)
print(new_list)

b = set()
b.add('apple')
b.add('banana')
b.add('microsoft')
b.add(1)
print(b)

given_list = [1, 3, 4, 1, 3]
total = 0
list_to_set = set()
for x in given_list:
    list_to_set.add(x)
for x in list_to_set:
    total += x
print(total)
