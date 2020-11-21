#import regex
import re
#import collections
import collections
#read text file
with open('Tempest.txt') as f:
    text = f.read()

#find all the words in the text file
words = re.compile(r"[\w']+", re.U).findall(text.lower())
#printing the most frequent words
print('most 10 common words on this file are :')
i = 1
for value, count in collections.Counter(words).most_common(10):
    print(str(i)+'. ', value, '(' +str(count)+')')
    i += 1