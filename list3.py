# fname = input("Enter file name: ")
# fh = open(fname)
# lst = list()
# for line in fh:
# print(line.rstrip())

fname = input("Enter file name: ")

with open(fname) as input :
	for text in input :
		text_split = text.split()
		print(text_split)


print('another try')

with open(fname) as input :
	# text = text.split()
	for text in input :
	    lst.append(text)
	print(lst)