f = open(r'/tmp/String.txt')
digits_str = ''
for i in f.read():
    if i.isdigit():
        digits_str += i
print(digits_str)
f.close()
