frase = "How Long are the words in this phrase"

def word_lengths(phrase):
    return len(phrase.split())

print(list(map(word_lengths,frase)))
