# Modifying string
school = " \t Batangas State University \n"


print(school.upper())
print(school.lower())

print(school.strip())


lpu_school = school.replace("Batangas", "Laguna")
print(lpu_school)

bsu_school = school.strip()
print(bsu_school)


# Splitting string to array
print(bsu_school.split(" "))