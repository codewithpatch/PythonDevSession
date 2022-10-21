# You are going to be given a word.Your job is to return the middle character of the word
# If the word's length is odd, return the middle character
# If the word'slength is even, return the middle 2 characters

def get_middle(s):
    word = list(s)
    x = len(word) / 2
    if len(word) % 2 == 0 or len(word) == 2:
        return "".join(word[int(x) - 1] + word[int(x)])
    if len(word) % 2 == 1 or len(word) == 1:
        return "".join(word[int(x)])
