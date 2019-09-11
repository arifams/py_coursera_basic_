numberList = []

while  True :
	masukan = input('Isi angka: ')
	if masukan == 'done' :
		break
	try : 
		angka = float(masukan)
		if angka >= 7.0 and angka <= 65.0 :
			print('bagus masih idup')
		else :
			print('anjir tua bangka siah')
	except : 
	    print("Error, please enter numeric input")
	    continue
	numberList.append(angka)
	print('total jumlah angka yang dimasukkan adalah', numberList)
	print('total jumlah isian:', len(numberList))
	print('rata-rata', sum(numberList)/len(numberList))