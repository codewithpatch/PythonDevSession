# 6kyu
# The main idea is to count all the occurring characters in a string. If you have a string like aba,
# then the result should be {'a': 2, 'b': 1}.

# What if the string is empty? Then the result should be empty object literal, {}.

def count(string):
    x = list(string)
    d = {}
    for i in range(0, len(string)):
        z = string.count(x[i])
        d.update({x[i] : z})
    return {} if len(string) == 0 else d