fname = input('Enter file name: ')
if len(fname) < 1 :
	fname = 'mbox-short.txt'
handle = open(fname)

daftar_email = list()

for line in handle :
	if not line.startswith("From:") : 
		continue
	line = line.rstrip()
	email = line.split()
	daftar_email.append(email[1])

kamus = dict()

for pengirim in daftar_email :
	kamus[pengirim] = kamus.get(pengirim, 0) + 1
	# print(pengirim)

kirim_terbanyak = -1
email_terbanyak = None 

for kunci,isi in kamus.items() :
	if isi > kirim_terbanyak :
		kirim_terbanyak = isi
		email_terbanyak = kunci 

print(email_terbanyak, kirim_terbanyak)