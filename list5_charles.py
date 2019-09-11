# open the text file
fname = open("mbox-short.txt")
# make counter
counter = 0

# print the text file with 'for' loop
for line in fname :
	# remove the next line with right strip function
	line = line.rstrip()
	# split the lines with strip function
	words = line.split()
	# guardian -> if words blank then continue
	if len(words) < 1 :
		continue
	# guardian -> if first word not from 'From', continue
	if words[0] != 'From' :
		continue
	# make counter counting how many lines the words after 'From'
	counter = counter + 1
	#print the second word, the words after 'From'
	print(words[1])

print('There are:', counter, 'emails')