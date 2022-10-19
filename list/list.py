list = [1, 2, 3, 'd', 'e', 'f', True, False]
print(list)

# Append List - Add Element(Last)
list.append(0)
print(list)
# Adding another list inside the list
list.append(['1', '2'])
print(list)

# Pop List - Remove Element(Last)
list.pop()
print(list)

print(list[0])
print(list[1])
print(list[2])
print(list[3])

list[0] = 'HELLO WORLDDDD!!!'
print(list)
