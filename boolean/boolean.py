type("microsoft")
type(4)
type(True)

a = 3
b = 1

if a > b: #a > b are evaluated to be either True or False
    print("a is greater than b")
if True:
    print("a is greater than b")

bool_val = a > b
print(bool_val)

def are_you_sad(is_rainy, has_umbrella):
    return is_rainy and not has_umbrella
q = are_you_sad(True, False)
w = are_you_sad(True, True)
e = are_you_sad(False, True)
r = are_you_sad(False, False)
print(q ,w ,e , r)

def c_greater_than_d_plus_e(c, d, e):
    return c > d + e

t = c_greater_than_d_plus_e(3, 1, 1)
y = c_greater_than_d_plus_e(1, 3, 3)
print(t, y)
