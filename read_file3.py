# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

for text in fh:
    text = text.rstrip()
    text = text.upper()
    print(text)