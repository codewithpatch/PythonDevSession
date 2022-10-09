d = {}
# d = {"George" : 25, "Tom": 32}

d["George"] = 25
d["Tom"] = 32
d["Jenny"] = 16

print(d["Jenny"])
print(d["George"])
print(d["Tom"])

d["Jenny"] = 20
print(d["Jenny"])

#keys are commonly strings or numbers

d[10] = "Sam"
print(d[10],"\n")

for key, value in d.items():
    print("key")
    print(key)
    print("value")
    print(value)
    print("")