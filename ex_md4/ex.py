import bs4 as bs
import ssl
import urllib.request, urllib.error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter: ')
html = urllib.request.urlopen(url).read()
soup = bs.BeautifulSoup(html, 'html.parser')
tags = soup('span')
count = 0
s = 0
for tag in tags:
    number = tag.contents[0]
    s += int(number)
    count += 1
print('Count:',count)
print('Sum:',s)
