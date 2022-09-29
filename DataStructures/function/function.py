# No parameter
def print_hello_world():
  print("Hello World!")


def get_full_name(first_name: str, middle_name: str, last_name: str) -> str:
  full_name = f"{first_name} {middle_name} {last_name}"

  # print(full_name)
  return full_name

  print(full_name)


def print_range():
  for num in range(0, 10):

    if num == 5:
      return num
      
    print(num)

  return "I hit last return"

print(print_range())



# first_name = "Chester"
# middle_name = "Dimaano"
# last_name = "de Alday"

# How to pass parameters in a function
chester_full_name = get_full_name("Chester", "Dimaano", "de Alday")
print(chester_full_name)
bryan_full_name = get_full_name(
  middle_name="Calderon",
  first_name="Bryan",
  last_name="de Alday",
)


gelo_dimaano = get_full_name("Angelo", "Calalo", "Dimaano")
# hello_world = print_hello_world()
print(gelo_dimaano)


