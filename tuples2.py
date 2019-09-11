fname = input('Enter file name: ')
if len(fname) < 1 :
	fname = 'mbox-short.txt'
handle = open(fname)

counts = dict()

for line in handle :
	words = line.split()
	for word in words :
		counts[word] = counts.get(word, 0) + 1

lst = list()
for key,val in counts.items() :
	newtup = (val, key)
	lst.append(newtup)

lst = sorted(lst, reverse=False)

for val,key in lst[:10] :
	print(key, val)