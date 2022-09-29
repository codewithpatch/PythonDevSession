from typing import Optional, Union


def calculate_age(birthyear: int, name: Optional[str] = "Gelo") -> Union[int, float]:
  year_now = 2022
  age = year_now - birthyear
  if name:
    print(f"Hey {name}, you are {age} years old!")
  else:
    print(f"You are {age} years old!")
  
  return age


my_age = calculate_age(1995, "Chester")
print(my_age)


random_age = calculate_age(2003)
print(random_age)