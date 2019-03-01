nltk.download('wordnet')
import nltk 
from nltk.corpus import wordnet 

# Let's compare the noun of "ship" and "boat:" 

w1 = wordnet.synset('ship.n.01') 
w2 = wordnet.synset('boat.n.01') # n denotes noun 
print(w1.wup_similarity(w2))


# Let's compare the verb sprint and run
 
w1 = wordnet.synset('run.v.01') # v here denotes the tag verb 
w2 = wordnet.synset('sprint.v.01') 
print(w1.wup_similarity(w2)) 
