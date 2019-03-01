# -*- coding: utf-8 -*-
import nltk

from nltk.tokenize import sent_tokenize, word_tokenize

data = "All work and no play makes jack a dull boy, all work and no play"
print(word_tokenize(data))

import gensim
print(dir(gensim))


raw_documents =["I am taking the show on the road.","My socks are a force multiplier","I am the barber who cuts everyones hair who doesn't cut their own",
                "Legend has it that the mind is a mad monkey", "I make my own fun"]

print("Number of documents:",len(raw_documents))

for r in raw_documents:
    print(r)
    
gen_docs =[[w.lower() for w in word_tokenize(r)]
    for r in raw_documents]
print(gen_docs)


dictionary = gensim.corpora.Dictionary(gen_docs)
print(dictionary[5])
print(dictionary.token2id['road'])
print("Number of words in dictionary:",len(dictionary))
for i in range(len(dictionary)):
    print(i, dictionary[i])
    
    
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
print(corpus)

tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)
s = 0
for i in corpus:
    s += len(i)
print(s)

sims = gensim.similarities.Similarity('/usr/workdir/',tf_idf[corpus],
                                      num_features=len(dictionary))
print(sims)
print(type(sims))

query_doc = [w.lower() for w in word_tokenize("The barber cuts my hair.")]
print(query_doc)
query_doc_bow = dictionary.doc2bow(query_doc)
print(query_doc_bow)
query_doc_tf_idf = tf_idf[query_doc_bow]
print(query_doc_tf_idf)

sims[query_doc_tf_idf]



############################################################333

import spacy
nlp = spacy.load('en')
doc1 = nlp(u'Hello hi there!')
doc2 = nlp(u'Hello hi there!')
doc3 = nlp(u'Hey whatsup?')

print(doc1.similarity(doc2)) # 0.999999954642
print(doc2.similarity(doc3)) # 0.699032527716
print(doc1.similarity(doc3)) # 0.699032527716






