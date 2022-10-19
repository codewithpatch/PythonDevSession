# Using while loop
from typing import List

list2 = [5, 4, 3, 2, 1, -1, -2, -3, -4, -5]
total2 = 0
i = 0
while 1 < 2:
    if list2[i] >= 0:
        continue
    total2 -= list2[i]
    i -= 1
print(total2)
