#BMI Calculator
name = "Jelo"
height_m = 2
weight_kg = 90

bmi = weight_kg / (height_m ** 2)
print("BMI:", bmi)

if bmi < 25:
    print(name)
    print("is not overweight")
else:
    print(name)
    print("is overweight")