# Import modules
import spacy

# load npl model
nlp = spacy.load('en_core_web_sm')

# Similarity
# define words
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

# print similarity
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))


# Vector examples
# define tokens - zoo added as 4th
tokens = nlp("cat apple monkey banana zoo")

"""
Zoo - monkey similarity was 0.45, zoo - cat similarity was 0.40
This is logical as its more likely to see a monkey in a zoo compared 
to a regular cat. 
"""

# for each token, compare to all other tokens and print similarity
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# Working with sentences
# define main sentence to compare against
sentence_to_compare = "Why is my cat on the car"

# define comparison sentences in a list
sentences = ["where did my dog go",
             "Hello, there is my car",
             "I\'ve lost my car in my car,"
             "I\'d like my boat back,"
             "I will name my dog Diana"]

# process model sentence
model_sentence = nlp(sentence_to_compare)

# Loop through each sentence and compare against comparison sentences
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(f"{sentence}-{similarity}")

"""
Comparing md and sm models
- sm models didn't have word vectors loaded, so similarity was based upon the tag
- This was evident as the delta between similarity values was smaller than when using the larger md model """