import nltk
import numpy as np
#uncomment these to download the punkt package
#nltk.download('punkt')
# ^ not sure if this one works anymore so try the one below
#nltk.download('punkt_tab')
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence)
    
def stem(word):
    return stemmer.stem(word.lower())
    

def bag_of_words(tokenized_sentence, all_words): #note to self:here
    tokenized_sentence = [stem(w) for w in tokenized_sentence]

    bag = np.zeros(len(all_words), dtype=np.float32)
    for idx, w in enumerate(all_words):
        if w in tokenized_sentence:
            bag[idx] = 1.0
    return bag


#uncomment these to test the tokenize function
#a = "Hello, how are you?"
#print(a)
#a = tokenize(a)
#print(a)

#uncomment these to test the stem function
#words = ["Organize","orGanizes", "organizing"]
#stemmed_words = [stem(w) for w in words]
#sprint(stemmed_words)

#uncomment these to test the bag_of_words function
#sentence = ["Hello", "how", "are", "you"]
#words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
#bag = bag_of_words(sentence, words)
#print(bag)