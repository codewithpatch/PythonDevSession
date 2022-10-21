# 6kyu
# Complete the method/function so that it converts dash/underscore delimited words into camel casing.
# The first word within the output should be capitalized only if the original word was capitalized
# (known as Upper Camel Case, also often referred to as Pascal case).

# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

def to_camel_case(text):
    if text == '':
        return ''
    camel = ''.join(e for e in text.title() if e.isalnum())
    return camel[0].lower() + camel[1:] if text[0].islower() else camel
