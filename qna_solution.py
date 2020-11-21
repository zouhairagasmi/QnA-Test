# Python program to find the 10 most frequent words 
# from a text file


import re
import collections

#Read input file
with open('Tempest.txt') as f:
    text = f.read()

#retrieve the words in the text file using regex
words = re.compile(r"[\w']+", re.U).findall(text.lower())
#counting the each word's occurence and printing the 10 most frequent words using collections counter
print('The 10 most common words in this file are as follows: ')
i = 1
for value, count in collections.Counter(words).most_common(10):
    print(str(i)+'. ', value, '(' +str(count)+')')
    i += 1