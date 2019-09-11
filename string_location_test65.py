text = "X-DSPAM-Confidence:    0.8475";
text = text.replace(' ', '')
semicolon = text.find(':')
latest_number = text.find('5')
numbers = text[semicolon+1:latest_number+1]

print(float(numbers))

print('----- coba cara laen ------- --------')

text = "X-DSPAM-Confidence:    0.8475";
text = text.replace(' ', '')
colon = text.find(':')
# cari angka setelah colon
numbers = text[colon+1:] 
numbers = float(numbers)
print(numbers)
type(numbers)