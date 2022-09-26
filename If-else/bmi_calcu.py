name = "zushi"
height_m = 1.70
weight_kg = 94

bmi = weight_kg / (height_m ** 2)
print("bmi: ")
print(bmi, "\n")

if bmi < 25:
    print(name)
    print("is not overweight")
else:
    print(name)
    print("is overweight")