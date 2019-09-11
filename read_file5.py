# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

for text in fh :  
    text = text.rstrip()
    text = text.upper()
    if 'SIEVE 2.3' in text :
    	break
    print(text)

print('--- another try with "with" ---')

with open(fname) as input :
	for text in input :
		text = text.rstrip()
		text = text.upper()
		if 'CMU' in text :
			break
		print(text)