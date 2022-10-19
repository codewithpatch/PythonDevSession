print("Hello,World")

from array import *

arr = array ('i',[])

n = int(input("Enter the length of the array"))

for i in range(5):
    x = int(input("Enter the next value"))
    arr.append(x)

print(arr)