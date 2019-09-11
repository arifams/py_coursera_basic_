# find duplicate string using import collections
import collections

sentence = 'As far as the laws of mathematics refer to reality they are not certain as far as they are certain they do not refer to reality'

# first split the Sentence
words = sentence.split()

# print(words)
'''
But there is even something better than that... collections.Counter 
which will take your list of words and turn it into 
a dictionary (an extension of dictionary actually) 
containing the counts.
'''
words_count = collections.Counter(words)

# print(words_count)
# https://stackoverflow.com/questions/25798674/python-duplicate-words
'''
From there you want the list of words in sorted order with their counts 
so you can print them. items() will give you a list 
of tuples, and sorted will sort (by default) by the 
first item of each tuple (the word in this case)... 
which is exactly what you want.
'''
print('in the sentence of:', sentence, 'these words calculating that: \n')
for word, count in sorted(words_count.items()) :
# formatting %s as word and %d as count
	print('"%s" is repeated %d times.' % (word, count))