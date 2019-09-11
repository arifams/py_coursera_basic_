file_text = open('hatta.txt', 'r')
counter = 0
for text in file_text :
    counter = counter + 1
    text = text.replace('\n', '')
    print(text)
print('Line text:', counter)

print('----- another try with function rstrip ----')

file_text = open('hatta.txt', 'r')
counter = 0
for text in file_text :
    counter = counter + 1
    text = text.replace('\n', '')
    print(text)
print('Line text:', counter)