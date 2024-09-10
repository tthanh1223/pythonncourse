import json
import urllib.request
import ssl
url = input('Enter: ')
if len(url) <1 :
    url = 'http://py4e-data.dr-chuck.net/comments_42.json'
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
handle = urllib.request.urlopen(url, context=ctx)
data = handle.read()
tree = json.loads(data)
nums = []
for item in tree['comments']:
    number = item["count"]
    number = int(number)
    nums.append(number)
print('Count:',len(nums))
print('Sum:',sum(nums))