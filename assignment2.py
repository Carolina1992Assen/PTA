import nltk 

# 1(a)

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
print(longest_sent)

# 1(b)

shortest_sent = sents_list.pop()
for s in sents_list:
    if len(s) < len(shortest_sent):
        shortest_sent = s
print(shortest_sent)

# 1(c)
my_dict = {}

for item in sents_list:
    if len(item) not in my_dict:
       my_dict[len(item)] = 0
    else:
       my_dict[len(item)] += 1

for i in sorted(my_dict.keys()):
    
    if my_dict[i] != 0:
        print("number of sentences of length", i, "  :  ", my_dict[i], "sentence(s)\n")


# 1(d)

total_length = 0
list_length = len(sents_list)
for item in sents_list:
    total_length += len(item)

average_length = total_length / list_length

print("average sentence length =", round(average_length))
    


     




