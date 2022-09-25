print("Hello World!")

# Multiline string
print("""
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
""")

print('''
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
''')

# String indexing
print("String indexing")
name = "Gelo Dimaano"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print()

# String Slicing
print("String Slicing")
print(name[5:12])
print(name[5:-1])
print(name[5:-2])
print()


# Concatenation and formatting
first_name = "Gelo"
last_name = "Dimaano"
full_name = first_name + " " + last_name
print(full_name)
print()

# f string
print("String Formatting")
full_name_fstring = f"{last_name}, {first_name}"
print(full_name_fstring)

full_name_format = "{} {}".format(first_name, last_name)
print(full_name_format)