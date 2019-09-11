#find smallest number
print("before, this is the total number")
numbers = 3,41,15,73,9,12,7,81,2,16

for number in numbers :
	print(number)

print("now python try to find the smallest number")

smallest_so_far = None

for number in numbers:
	if smallest_so_far is None :
		smallest_so_far = number
	elif number < smallest_so_far :
		smallest_so_far = number
	print(smallest_so_far, number)

print("Now the current smallest is", smallest_so_far)
