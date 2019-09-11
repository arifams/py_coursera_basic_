fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for text in fh : 
	text = text.rstrip()
	text = text.split()
	for words in text :
		if words not in lst :
			lst.append(words)
lst.sort()
print(lst)