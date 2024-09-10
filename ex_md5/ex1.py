import urllib.request
import xml.etree.ElementTree as ET
url = input('Enter: ')
if len(url) < 1 :
    url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
print('Retrieving',url)
html = urllib.request.urlopen(url).read()
data = html.decode()
print('Retrieved',len(data),'characters')
tree = ET.fromstring(data)
nums = []
print(tree)
counts = tree.find('comments').findall('comment')
c = 0
s = 0
for count in counts:
    number = count.find('count').text
    nums.append(int(number))
print('Count:', len(nums))
print('Sum:', sum(nums))