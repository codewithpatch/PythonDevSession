# 6kyu
# The corresponding sums are (put together in a list): [20, 20, 19, 16, 10, 0]

# The function parts_sums (or its variants in other languages) will take as
# parameter a list ls and return a list of the sums of its parts as defined above.

# ls = [1, 2, 3, 4, 5, 6]
# parts_sums(ls) -> [21, 20, 18, 15, 11, 6, 0]

# ls = [744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358]
# parts_sums(ls) -> [10037855, 9293730, 9292795, 9292388, 9291934, 9291504, 9291414, 9291270, 2581057, 2580168, 2579358, 0]

def parts_sums(ls):
    list_sum = [0]
    x = 0
    for i in ls[::-1]:
        x += i
        list_sum.append(x)
    return list_sum[::-1]
