#Use a built-in function to return the words from a list of words which start with a target letter (use a lambda function).

l = ['hello','are','cat','dog','ham','hi','go','to','heart']

def filter_words(word_list, letter):
    return list(filter(lambda word: word[0] == letter, word_list))

print(filter_words(l,'h'))