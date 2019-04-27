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

#rest moet nog, ik weet niet welke textfile ik hiervoor moet gebruiken of hoe ik daarbij kom met path.


# Assignment 2

# A
path = (/home/carlijn/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin/
'sherlock.txt')

# kom  er niet uit met path



