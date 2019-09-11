# find duplicate string

Sentence = 'As far as the laws of mathematics refer to reality they are not certain as far as they are certain they do not refer to reality'

# first split the Sentence
words = Sentence.split()
# test it and we'll find out it devided
print(words)
# make dictionary counter
counter = {}
# make loop
for word in words : 
	if word not in counter :
		counter[word] = 0
	counter[word] = counter[word] + 1
	print(counter[word])
