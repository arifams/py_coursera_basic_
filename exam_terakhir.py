smallest = None
largest = None

while True :
	numbers = input('Enter a number: ')
	if numbers == 'done' : 
		break
	try :
		fnum = float(numbers)
	except : 
		print ('Error, input is not numeric number') 
		continue
	else :
		if smallest is None :
			smallest = fnum
			largest = fnum
		elif fnum < smallest :
			smallest = fnum
		elif fnum > largest :
			largest = fnum

print('Invalid input')
print('Maximum is', int(largest))
print('Minimum is', int(smallest))
