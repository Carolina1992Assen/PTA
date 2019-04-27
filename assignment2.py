import nltk 


print("*Assignment 1(a)*\n")

path = "holmes.txt"
f =open(path)
rawText = f.read()
f.close()

sents = nltk.sent_tokenize(rawText)
sents_list = []
for sen in sents:
    sents_list.append(sen)
longest_sent = sents_list.pop()
for s in sents_list:
    if len(s) > len(longest_sent):
        longest_sent = s
print("The longest sentence is: \n" + longest_sent + "\n\n")


print("*Assignment 1(b)*\n")

shortest_sent = sents_list.pop()
for s in sents_list:
    if len(s) < len(shortest_sent):
        shortest_sent = s
print("The shortest sentence is: \n" + shortest_sent + "\n\n")


print("*Assignment 1(c)*\n")

my_dict = {}
for item in sents_list:
    if len(item) not in my_dict:
       my_dict[len(item)] = 0
    else:
       my_dict[len(item)] += 1

for i in sorted(my_dict.keys()):
    if my_dict[i] != 0:
        print("number of sentences of length", i, "  :  ", my_dict[i], "sentence(s)")
print("\n")


print("*Assignment 1(d)*\n")

total_length = sum([len(line) for line in sents])
list_length = len(sents_list)
average_length = total_length / list_length
print("average sentence length =", round(average_length), "\n\n")


print("*Assignment 2(a)*\n")

ch_types_list = []
ch_types = "".join(set(rawText))
for item in ch_types:
    ch_types_list.append(item)
print("There have been {0} character types found.\n\nThe list below shows them all:\n\n{1}\n\n".format(len(ch_types_list), sorted(ch_types_list)))


print("*Assignment 2(b)*\n")

types = []
for sent in sents: 
    for word in nltk.word_tokenize(sent):
        if word not in types:
           types.append(word)
"""print("There have been {0} word types found.\n\nThe list below shows them all:\n\n{1}\n\n".format(len(types), sorted(types)))"""


print("*Assignment 2(c)*\n")

print("Top 20 character level unigrams(ordered by descending frequency:\n")
print(sorted(ch_types_list)[0:21])

print("Top 20 character level bigrams(ordered by descending frequency:\n")
bigrams = nltk.bigrams(nltk.word_tokenize(sent))
fdist = nltk.FreqDist(bigrams)
n = 0
for i in sorted(fdist.keys()):
    print(i, fdist[i])
    n += 1
    if n == 20:
        break
    else:
        continue



# is het nu descending???????????? dit klopt niet helemaal

""">>> sent = ['The', 'cat', 'that', 'sat', 'on', 'the', 'mat',2...    'also', 'sat', 'on', 'the', 'sofa']
3>>>list(nltk.bigrams(sent))4[('The', 'cat'), ('cat', 'that'), ('that', 'sat'), ('sat', 'on'),5...    ('on', 'the'), ('the', 'mat'), ('mat', 'also'), ('also',6...    'sat'), ('sat', 'on'), ('on', 'the'), ('the', 'sofa')]

Words and TokenisationBigrams’ countsLet’s get frequencies...1>>> sent = ['The', 'cat', 'that', 'sat', 'on', 'the', 'mat',2...    'also', 'sat', 'on', 'the', 'sofa']3>>> bigrams = nltk.bigrams(sent)4>>> fdist = nltk.FreqDist(bigrams)5>>>forb,finfdist.items():6...print(b,f)7...8('mat', 'also') 19('The', 'cat') 110('on', 'the') 211('the', 'sofa') 112('sat', 'on') 213('cat', 'that') 114('that', 'sat') 115('also', 'sat') 116('the', 'mat') 

c)  the top 20character-level unigrams, bigrams, and trigrams, ordered by descend-ing frequency (from the most frequent to the least).  Please, add a comment speci-fying what you think this information could be useful for.(d)  the top 20word-level unigrams, bigrams and trigrams, ordered by descending fre-quency.  Please, add a comment specifying what you think this information couldbe useful for."""








