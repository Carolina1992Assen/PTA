#import nltk
import nltk

# tell python we want to use gutenberg corpus
from nltk.corpus import gutenberg

# Assignment 1

# which files are in this corpus
print(gutenberg.fileids())

# get the raw text of a corpus (one string)
emmaText = gutenberg.raw('austen-emma.txt')

# print the first 289 characters of a text
emmaText[:289]

# get the words of a corpus as a list
emmaWords = gutenberg.words('austen-emma.txt')

# print the first 30 words of the text
print(emmaWords[:30])

# get the sentences of a corpus as a list of lists
# one list of words per sentence
senseSents = gutenberg.sents('austen-emma.txt')

# print out the first four sentences
print(senseSents[:4])

# print and split the text up into sentences
sents = nltk.sent_tokenize(emmaText)
print(sents[20:22])

# tokenize sentence with nltk
tokens = []
for sent in sents:
	tokens += nltk.word_tokenize(sent)
print(tokens[300:350])

# print bigrams list
print(list(nltk.bigrams(emmaWords)))

# make bigrams of given list
bigrams = nltk.bigrams(emmaWords)

# count frequencies of bigrams and print bigram + frequency
fdist = nltk.FreqDist(bigrams)
for b,f in fdist.items():
	print(b,f)

