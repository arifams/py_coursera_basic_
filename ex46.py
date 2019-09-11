h = input("Enter Hours:")
r = input("Enter rate")

def computepay(h,r) :
	try:
		h = float(h)
		r = float(r)
	except:
		return "Error, input is not numeric number"
		quit()
	if h > 40.0 :
		reg_paid = h * r
		ext_paid = (h - 40.0) * (r * 0.5)
		total_paid = reg_paid + ext_paid
	else :
		total_paid = h * r
	print (total_paid)

computepay(h,r)