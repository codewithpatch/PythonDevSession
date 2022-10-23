# 5kyu
# Your job is to write a function which increments a string, to create a new string.

# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.

# Examples:
# foo -> foo1
# foobar23 -> foobar24
# foo0042 -> foo0043
# foo9 -> foo10
# foo099 -> foo100

# Attention: If the number has leading zeros the amount of digits should be considered.

def increment_string(strng):
    strip_str = strng.rstrip('1234567890')
    e = strng[len(strip_str):]
    if len(e) == 0: return strng + '1'
    return strip_str + str(1 + int(e)).zfill(len(e))