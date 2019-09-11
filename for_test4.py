# summing two variables: the zork and the number
zork = 0
print("before", zork)

for number in [3,12,19,74,33,7,19,86,76,2]:
	zork = zork + number
	print(zork, number)

print("after", zork)