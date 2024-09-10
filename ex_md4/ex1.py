import urllib.request
import ssl
import bs4 as bs
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter URL : ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))
print('Retrieving:', url)
for c in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = bs.BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    print('Retrieving:',tags[position-1].get('href',None))
    url = tags[position-1].get('href',None)
