#BMI Calculator
name = "Ichiban"
height_m = 2
weight_kg = 90

bmi = weight_kg / (height_m ** 2)
print("bmi:", bmi)

if bmi < 25:
    print(name)
    print("is not overweight")
else:
    print(name)
    print("is overweight")

