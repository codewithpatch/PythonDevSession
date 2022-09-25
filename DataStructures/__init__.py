"""
Data Structures

1. String
2. List - Array
3. Dictionary - Hash/JSON
4. Tuple - Array like datastructure
5. Set
6. Integer
7. Float
8. Byte / binary
"""

# String
string_double = "Loren Ipsum"
string_single = 'Loren Ipsum'

# list - mutable
['string', 1, 1.54, ['another string', 2, 3], {"key":"value"}]
  # best practice
counts = [1, 2, 3, 4, 5, 6, 7, 8]
counts.append(9)

'[1, 2, 3, 4, 5, 6, 7, 8, 9]'

counts[0] = 25
'[25, 2, 3, 4, 5, 6, 7, 8, 9]'



# Dictionary
{
  "name": "Gelo",
  "age": 15,
  "school": "BSU",
  "friends": ["Ichiban", "Elon Musk"],
  "family_tree0": {
    "father": "Angelo",
    "mother": "Janet",
    "sister": "Gela"
  }
}


# Tuple - immutable
('string', 1, 1.54, ['another string', 2, 3], {"key":"value"})
# Best practice
(125, 23) # coordinates



# Set
thisset = {"apple", "banana", "cherry"}


# Integer
1
2
3

#Float
1.5
1.7
0.21251234123541235


# Byte/binary
b'Python is interesting.'