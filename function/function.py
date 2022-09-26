#This is a comment
#Pang pogi na comment ito

def function1():
    print("ahhhh")
    print("ahhhhhhh2")
print("This is outside of the function")

#Calling the function
function1()
function1()

#Mapping
def function2(x):#<<<(Input or Argument)
    return 5*x

#Return value or output
a = function2(3)
print(a)

b = function2(4)
print(b)

c = function2(5)
print(c)

#Multiple argument in a single function
def function3(x, y):
    return x + y

e = function3(1, 2)
print(e)

#Combined (Collection of code and Mapping)
def function4(x):
    print(x)
    print("still in this function")
    return 3*x
f = function4(4)
print(f)

def function5(some_argument):
    print(some_argument)
    print("yo what ang pogi ko")

function5(4)