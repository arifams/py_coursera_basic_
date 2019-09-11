# Write a program to prompt the user for hours and rate per hour using input
# to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5
# times the hourly rate for all hours worked above 40 hours. Use 45 hours and
# a rate of 10.50 per hour to test the program (the pay should be 498.75). You
# should use input to read a string and float() to convert the string to a
# number. Do not worry about error checking the user input - assume the user
# types numbers properly.

hours = input("How many hours do you work this week?")
hours = float(hours)
extra_hours = hours - 40

rate = input("How much your rate per hour?")
rate = float(rate)
extra_rate = rate * 1.5

paid_normal = 40 * rate

if hours > 40 :
	extra_paid = extra_hours * extra_rate
	print (paid_normal + extra_paid)
else :
	print(rate * hours)
