hour = input("enter hours: ")
rate = input("enter rate: ")

try:
	fhour = float(hour)
	frate = float(rate)
except:
	print("Error, please enter numeric input")
	quit()

print(fhour, frate)

if fhour > 40:
	normal_pay = fhour * frate
	extra_pay = (fhour - 40.0) * (frate * 0.5)
	total_pay = normal_pay + extra_pay
else:
	total_pay = fhour * frate

print (total_pay)
