# summing two variables: the zork and the number
# with counter
count = 0
zork = 0
print("before", count, zork)

for number in [3,12,19,74,33,7,19,86,76,2]:
	count = count + 1
	zork = zork + number
	print(count, zork, number)

print("after", count, zork)