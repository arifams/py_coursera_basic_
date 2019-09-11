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
		# jika key tidak ada, maka value adalah 0
		# kata_berhitung = kamus.get(kata, 0)
		# print(kata, 'lama', kata_berhitung)
		# kata_baru = kamus.get(kata, 0) + 1
		# print(kata, 'baru', kata_baru)
		# ini script lebih sederhana untuk
		# update/retrieve/menciptakan hitungan
		kamus[kata] = kamus.get(kata, 0) + 1
		# print(kata, 'baru', kamus[kata])

print(kamus)