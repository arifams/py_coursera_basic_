greet = "Hello Bob"
print(greet)
j = greet.replace('Bob', 'Jane')
print(j)

too_much_space = '    Hello Bob.   '
print(too_much_space)
remove_left = too_much_space.lstrip()
print(remove_left)
remove_strip = too_much_space.strip()
print(remove_strip)

x = 'From marquard@uct.ac.za'
print(x[8])
x = 'From marquard@uct.ac.za'
print(x[14:17])

print(len('banana')*7)

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])