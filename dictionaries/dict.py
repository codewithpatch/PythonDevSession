# Dictionaries - Key value pair
d = {}
d["Jelo"] = 19
d["Mariel"] = 18

print(d["Jelo"])
print(d)

d["Bien"] = "bonak"

print(d["Bien"])

d["Bien"] = "super bonak"
print(d["Bien"])

d[10] = 100
print(d[10])

# Iterate over a key value pair
for key, value in d.items():
    print("key:")
    print(key)
    print("value:")
    print(value)
    print("")