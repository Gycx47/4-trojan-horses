import nltk
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
    

def bag_of_words(tokenized_sentence, all_words):
    pass

#uncomment these to test the tokenize function
#a="Hello, how are you?"
#print(a)
#a=tokenize(a)
#print(a)

#uncomment these to test the stem function
#words=["Organize","orGanizes", "organizing"]
#stemmed_words=[stem(w) for w in words]
#sprint(stemmed_words)