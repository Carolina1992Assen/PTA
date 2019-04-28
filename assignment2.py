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
print("There have been {0} word types found.\n\nThe list below shows them all:\n\n{1}\n\n".format(len(types), sorted(types)))


print("*Assignment 2(c)*\n")

print("\n\nTop 20 character level unigrams(ordered by descending frequency):\n")
print(sorted(ch_types_list)[0:21])

print("\n\nTop 20 character level bigrams(ordered by descending frequency):\n")
ch_tokens_list = []
for i in range(len(rawText)):
    ch_tokens_list.append(rawText[i])

bigrams = nltk.bigrams(ch_tokens_list)
bigrams_list = []

fdist = nltk.FreqDist(bigrams)
for b,f in fdist.items():
	bigrams_list.append((b,f))

bigrams_list = sorted(bigrams_list, key=lambda tup: tup[1], reverse = True)

for b, f in bigrams_list[:21]:
	print(b, f)

print("\n\nTop 20 character level trigrams(ordered by descending frequency):\n")

trigrams = nltk.trigrams(ch_tokens_list)
trigrams_list = []

fdist = nltk.FreqDist(trigrams)
for t,f in fdist.items():
	trigrams_list.append((t,f))

trigrams_list = sorted(trigrams_list, key=lambda tup: tup[1], reverse = True)

for t, f in trigrams_list[:21]:
	print(t, f)

print("\n\n*Assignment 2(d)*\n")

print("\n\nTop 20 unigrams(ordered by descending frequency):\n")
tokens = []
for sent in sents:
	tokens += nltk.word_tokenize(sent)

unigrams_list = []
fdist = nltk.FreqDist(tokens)
for b,f in fdist.items():
	unigrams_list.append((b,f))

unigrams_list = sorted(unigrams_list, key=lambda tup: tup[1], reverse = True)

for b, f in unigrams_list[:20]:
	print(b, f)

print("\n\nTop 20 bigrams(ordered by descending frequency):\n")

bigrams = nltk.bigrams(tokens)
bigrams_list = []

fdist = nltk.FreqDist(bigrams)
for b,f in fdist.items():
	bigrams_list.append((b,f))

bigrams_list = sorted(bigrams_list, key=lambda tup: tup[1], reverse = True)

for b, f in bigrams_list[:20]:
	print(b, f)


print("\n\nTop 20 trigrams(ordered by descending frequency):\n")


trigrams = nltk.trigrams(tokens)
trigrams_list = []

fdist = nltk.FreqDist(trigrams)
for b,f in fdist.items():
	trigrams_list.append((b,f))

trigrams_list = sorted(trigrams_list, key=lambda tup: tup[1], reverse = True)


for b, f in trigrams_list[:20]:
	print(b, f)

print("\n\n\nWord groups, like bigrams, are useful for checking the meaning of words which are ambiguous. By knowing what kind of words surround a particular word it is easier to determine if a word is for example a noun or a verb.")









