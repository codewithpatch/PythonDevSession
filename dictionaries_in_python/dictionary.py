d = {}
# d = {"Ichiba": 19, "Andre": 20}
d["Ichiban"] = 19
d["Andre"] = 20
d["Lilith"] = 18

print(d["Ichiban"])
print(d["Andre"])
print(d["Lilith"])

d["Lilith"] = 20
print(d["Lilith"])

# keys are commonly strings or numbers
d[10] = 100
print(d[10])

# how to iterate over key-value pairs?
for key, value in d.items():
    print("key")
    print(key)
    print("value")
    print(value)
    print(" ")

