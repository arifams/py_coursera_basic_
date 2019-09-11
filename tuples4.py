name = input("Enter file:")
if len(name) < 1 : 
	name = "mbox-short.txt"
handle = open(name)

dic = {}

for line in handle:
	if not line.startswith("From ") :
	    continue
	time = line.split()
	time = time[5]
	hour = time.split(':')
	hour = hour[0]
	dic[hour] = dic.get(hour, 0) + 1

for key, value in sorted(dic.items()):
	print (key, value)