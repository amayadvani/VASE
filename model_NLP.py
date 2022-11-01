# This file is to experiment NLP: Natural Language Processing
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize, word_tokenize

other_symptom_string = "Emma's throat initially was itchy, last Saturday, swallow throat hurt. Took antibioatic, at night still coughing, but today swallow no pain."
sent_tokenize(other_symptom_string)

# 1. tokenizing string by word
symptom_words = word_tokenize(other_symptom_string)
print("Symptom word list: ")
print(symptom_words)

# 2. Filtering Stop Words
nltk.download("stopwords")
from nltk.corpus import stopwords

#This "english" version stopwords contain I, no, not which we do not want to remove
stop_words = set(stopwords.words("english"))

filtered_list_words = []
for word in symptom_words:
    #casefold will ignore upper cases, stop_words only has lower cases
    if word.casefold() not in stop_words:
        filtered_list_words.append(word)
print("Filtered out stopwords: ")
print(filtered_list_words)

# TBD try to download other version of stopwords? nltk.download()
# 3. Stemming
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in symptom_words]
print("Stemmed words: ")
print(stemmed_words)

# 4. Tagging the words
nltk.download('averaged_perceptron_tagger')
tagged_words = nltk.pos_tag(symptom_words)
print("Tagged words: ")
print(tagged_words)

# 5. Lemmatizing
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()

print("Lemmatized words: ")
#for word in symptom_words:
#    lemmatized_word = lemmatizer.lemmatize(word)
#    print(lemmatized_word)

lemmatized_words = [lemmatizer.lemmatize(word) for word in symptom_words]
print(lemmatized_words)

# 6. Chunking
#Start with an optional (?) determiner ('DT')
#Can have any number (*) of adjectives (JJ)
#End with a noun (<NN>)
grammar1 = "NP: {<DT>?<JJ>*<NN>}"
chunk_parser = nltk.RegexpParser(grammar1)
tree = chunk_parser.parse(tagged_words)
#tree.draw()

# 7. tree.draw()
grammar2 = """
    Chunk: {<.*>+}
           }<JJ>{"""
chunk_parser = nltk.RegexpParser(grammar2)
tree = chunk_parser.parse(tagged_words)
#tree.draw()

# 7. Using Named Entity Recognition (NER)
nltk.download("maxent_ne_chunker")
nltk.download("words")
tree = nltk.ne_chunk(tagged_words, binary=True)
#tree.draw()

# extract named entities?
def extract_ne(quote):
    words = word_tokenize(quote, language="english")
    tags = nltk.pos_tag(words)
    tree = nltk.ne_chunk(tags, binary=True)
    return set(
            " ".join(i[0] for i in t)
            for t in tree
                if hasattr(t, "label") and t.label() == "NE"
            )

name_identity = extract_ne(other_symptom_string)
print("Name Identity:")
print(name_identity)

# 8. corpus: a group of texts
nltk.download("book")
from nltk.book import *

# 8.1 Using a Concordance, you can see each time a word is used, along with its immediate context. 
text8.concordance("man")

# 8.2 see how much a particular word appears and where it appears
#text8.dispersion_plot(["woman", "lady", "girl", "gal", "man", "gentleman", "boy", "guy"])

# 8.3. Making a Frequency Distribution
from nltk import FreqDist
frequency_distribution = FreqDist(text8)
print(frequency_distribution)
frequency_distribution.most_common(20)

# Turn the list to a graph
frequency_distribution.plot(20, cumulative=True)

# 8.4 Finding Collocations
# To see pairs of words that come up often in your corpus
text8.collocations()