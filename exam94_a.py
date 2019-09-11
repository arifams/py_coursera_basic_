play = "MARCELLUS Horatio says 'tis but our fantasy, And will not let belief take hold of him Touching this dreaded sight, twice seen of us: Therefore I have entreated him along With us to watch the minutes of this night; That if again this apparition come, He may approve our eyes and speak to it. HORATIO Tush, tush, 'twill not appear. BERNARDO Sit down awhile; And let us once again assail your ears, That are so fortified against our story What we have two nights seen."

fname = input('Enter file name: ')
if len(fname) < 1 :
	fname = 'romeo.txt'
handle = open(fname)

kamus = dict()

for line in handle :
	hoho = line.rstrip()
	hihi = hoho.split()
	for kata in hihi :
		# update/retrieve/menciptakan hitungan
		# info urutan logika lengkap lihat exam94.py
		kamus[kata] = kamus.get(kata, 0) + 1

# print(kamus)

# mencari kalimat yang paling umum/banyak
# pakai variabel iterator 'k' (singkatan dari kunci)
# dan i (singkatan dari 'isi')
# menggunakan metode items()

angka_terbesar = -1 # ini trik sebab setelah itu angka 0, harus pakai integer 
kata_terbanyak = None # trik menghitung string yang kita tidak tahu ada berapa banyak

for kunci,isi in kamus.items() :
	if isi > angka_terbesar :
		angka_terbesar = isi
		kata_terbanyak = kunci # untuk menghitung kata sama yang terbanyak muncul

print('Selesai. Kata yang paling sering muncul adalah "', kata_terbanyak, '" dengan jumlah sebanyak:', angka_terbesar)



