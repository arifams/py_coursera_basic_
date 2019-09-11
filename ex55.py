counter = 0
tot = 0.0

while True:
    sval = input('Input number: ')
    if sval == 'done' :
    	break
    try:
        fval = float(sval)
    except:
        print ('Error, input is not numeric number')
        continue
    # print (sval)
    counter = counter + 1
    tot = tot + fval
print ('ALL DONE', tot, counter, tot/counter)
