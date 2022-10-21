# 6kyu
# Write a function that takes in a string of one or more words,
# and returns the same string, but with all five or more letter
# words reversed (Just like the name of this Kata). Strings passed
# in will consist of only letters and spaces. Spaces will be included

#Examples
#spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
#spinWords( "This is a test") => returns "This is a test"
# spinWords( "This is another test" )=> returns "This is rehtona test"
# only when more than one word is present.

def spin_words(sentence):
    # Your code goes here
    # split sentence
    sentence_split = sentence.split()
    length_sentence = len(sentence_split)
    # check each element's length
    for i in range(length_sentence):
        if len(sentence_split[i]) >= 5:
            word = sentence_split[i]
            reverse_word = word[::-1]
    # replace word
            sentence_split[i] = reverse_word
    return " ".join(sentence_split)