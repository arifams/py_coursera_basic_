print("before, this is the total number")
numbers = 3,41,15,73,9,12,7,81,2,16

for number in numbers:
	print(number)

print("now python try to find the largest number")

largest_so_far = 0

for number in numbers:
	if number > largest_so_far:
		largest_so_far = number
	print(largest_so_far, number)

print("Now the current largest is", largest_so_far)
