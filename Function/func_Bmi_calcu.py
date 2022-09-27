#BMI Calculator

name1 = "Berna"
height_m1 = 1.70
weight_kg1 = 90

name2 = "Vernadetta"
height_m2 = 1.50
weight_kg2 = 70

name3 = "Zasha"
height_m3 = 2.1
weight_kg3 = 69

def bmi_calculator(name, height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2)
    print(name)
    print("bmi:", bmi)

    if bmi < 25:
        return name + " is not overweight"
    else:
        return name + " is overweight"
result1 = bmi_calculator(name1, height_m1, weight_kg1)
result2 = bmi_calculator(name2, height_m2, weight_kg2)
result3 = bmi_calculator(name3, height_m3, weight_kg3)

print("\n", result1)
print("\n", result2)
print("\n", result3)