"""
This file consists of functions used for text processing  
"""

import nltk
import numpy as np
nltk.download('punkt')

from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence)


def stem(word):
    return stemmer.stem(word.lower())


def bag_of_words(tokenized_sentence, all_words):
    tokenized_sentence = [stem(w) for w in tokenized_sentence]
    bag = np.zeros(len(all_words), dtype=np.float32)
    
    for index, w, in enumerate(all_words):
        if w in tokenized_sentence:
            bag[index] = 1.0
    
    return bag



# sentence = ["how", "are", "you"]
# words = ["how", "hello", "hi", "namaste", "be", "go", "are", "is", "am", "are", "you", "they"]
# bag = bag_of_words(sentence, words)
# print(bag)


# a = "How long does it take for shipping?"
# print(a)
# a = tokenize(a)
# print(a)

# stemmed_words = [stem(w) for w in a]
# print(stemmed_words)
