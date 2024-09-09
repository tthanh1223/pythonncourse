import re
file = input("Enter filename:")
if len(file) < 1:
    file = 'text1.txt'
handle = open(file)
S = 0
for line in handle:
    number = re.findall('[0-9]+' ,line)
    for num in number:
        num = int(num)
        S += num
print(S)
handle.close()