#Function

def function1():
    print("ahhhh")
    print("ahhhhhhh2")
print("This is outside of the function")

#calling the function
function1()


#mapping
#input or an argument
def function2(x):
    return 2*x
#return value or output
a = function2(3)
print(a)
b = function2(4)
print(b)
c = function2(5)
print(c)


#multiple argument in a single function
def function3(x, y):
    return x + y

e = function3(1, 2)
print(e)


#combine the collection of code and mapping
def function4(x):
    print(x)
    print("still in this function")
    return 3*x
f = function4(4)
print(f)

def function5(some_argument):
    print(some_argument)
    print("wala tayong motivational quotes ngayon, basta wag kang mag shabu okay na yon.")

function5(4)





