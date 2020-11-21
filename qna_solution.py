import re
import collections

with open('Tempest.txt') as f:
    text = f.read()


words = re.compile(r"[\w']+", re.U).findall(text.lower())
most_common = collections.Counter(words).most_common(10)
print(most_common)