name = input('Enter file name: ')
if len(name) < 1 :
	name = 'mbox-short.txt'
handle = open(name)

kamus = dict()

for line in handle :
	if not line.startswith('From') :
	    continue
	line = line.split()
	for words in line :
		kamus[words] = kamus.get(words, 0) + 1

listo = list()

for k,v in kamus.items() :
	if not (':') in k :
		continue
	if v > 1 :
		continue
	k = int(k[:2])
	newtuple = k
	listo.append(newtuple)

listo = sorted(listo)

for k,v in listo :
	print(k,v)