# -*- coding: utf-8 -*-
###################################Demo1##############################################################################
####################################Word and Sentence Tokenizer#######################################################
import nltk
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk import ne_chunk, pos_tag

print("~~~~~~~~~~~~~~~~~~~~~~~~~~Tokenizing~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
example_text= "Hello World this is a test. Mr. Jack and Ms. Jill went up the hill to fetch some water."
example_sentence = sent_tokenize(example_text)
print(example_sentence)

words=word_tokenize(example_text)
print(words)

#print(nltk.wordpunct_tokenize(text))

########################################POS Tagging#######################################################################
print("~~~~~~~~~~~~~~~~~~~~~~~~~~POS Tagging~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
nltk.download('averaged_perceptron_tagger')
print(nltk.pos_tag(words))



#######################################Stopword Removal###################################################################
from nltk.corpus import stopwords
print("~~~~~~~~~~~~~~~~~~~~~~~~~~Stopword Removal~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
example_Sentence=" This is an exampe showing off stop word filtration"

stop_words= set(stopwords.words("english"))
words1=word_tokenize(example_Sentence)
#print(stop_words) #prints all the stopwords which will be removed after processing text

filtered_sentence =[]

for w in words1:
    if w not in stop_words:
        filtered_sentence.append(w)
print(filtered_sentence)


#######################################Stemming##########################################################################
print("~~~~~~~~~~~~~~~~~~~~~~~~~~Stemming~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 
ps = PorterStemmer() 
 # choose some words to be stemmed 
words2 = ["program", "programs", "programer", "programing", "programers"] 
for w in words2: 
    print(w, " : ", ps.stem(w))


#######################################Lemmatizing#######################################################################
print("~~~~~~~~~~~~~~~~~~~~~~~~~~Lemmatization~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer 
lemmatizer = WordNetLemmatizer() 
print("rocks :", lemmatizer.lemmatize("rocks")) 
print("corpora :", lemmatizer.lemmatize("corpora")) 
# a denotes adjective in "pos" 
print("better :", lemmatizer.lemmatize("better", pos ="a")) 


        
