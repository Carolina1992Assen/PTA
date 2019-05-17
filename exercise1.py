#!/usr/bin/python3
# name: Carlijn Assen
# date: 17/05/2019

import nltk
import os

filename = "en.tok.off"
file_list = []

for root, dirs, files, in os.walk(".", topdown=False):
    for name in files:
        if name == filename:
            file_list.append(os.path.abspath(str(root[2::]) + "/" + name))


for item in file_list:

    tokens = []
    pos = []
    columns = []

    with open(item) as f:
        for line in f:
            line = line.split()
            tokens.append(line[3])
            columns.append(line)
        pos = nltk.pos_tag(tokens)

        outfile = open(item + '.pos', 'w')
        for i in range(len(columns)):
            outfile.write(
                "{0} {1}".format(
                    (" ".join(columns[i])), (pos[i][1])))
            outfile.write("\n")
        outfile.close()
