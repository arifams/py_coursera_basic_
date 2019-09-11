# file = open('mbox-short.txt', 'r')
# lst = list()
# count = 0
# for line in file :
# 	# line = line.rstrip()
# 	if not line.startswith('From')  :
# 		continue
# 	text = line.split()
# 	lst.append(text[1])
# 	count = count + 1
# print(lst, '\n')

# print("There were", count, "lines in the file with From as the first word")


fname = input("Enter file name: ")

if len(fname) < 1 : 
	fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    if not line.startswith("From:") : 
    	continue
    line = line.strip().split()
    print(line[1])
    count = count + 1
print("There were", count, "lines in the file with From as the first word")