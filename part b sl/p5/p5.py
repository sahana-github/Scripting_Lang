import pprint
import re
import functools as ft

file = open('sample.txt', 'r')
l = file.read()
l = re.findall(r"[\w']+", l)
words = {}

print(l)

for i in l:
    if i not in words.keys():
        words[i] = 1
    else:
        words[i] += 1
        
sorted_words = dict(sorted(words.items(), key = lambda x:x[1], reverse=True))

top10_words = {x: sorted_words[x] for x in list(sorted_words)[:10]}
print("Top 10 words with most occurrences:")

for i in top10_words:
    print(i, ":", top10_words[i])

word_len = []
for x in words.keys():
    word_len.append(len(x))
    
avg = ft.reduce(lambda a,b: a+b, word_len) / len(word_len)

odd_squares = [x**2 for x in word_len if x%2 == 1]

print("Average length of words are: {:.2f}".format(avg))
print("Squares of odd length in words are: ", odd_squares)

file.close()


