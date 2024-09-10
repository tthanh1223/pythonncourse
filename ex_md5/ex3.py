import urllib.request, urllib.parse
import json, ssl
service_url = 'https://py4e-data.dr-chuck.net/opengeo?'
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    location = input('Enter location: ')
    if len(location) < 1: break
    location = location.strip()
    params = dict()
    params['q'] = location
    url = service_url + urllib.parse.urlencode(params)
    print('Retrieving', url)
    html = urllib.request.urlopen(url, context=ctx).read()
    data = html.decode()
    print('Retrieved', len(data), 'characters\n',data[:20].replace('\n',' '))
    try:
        js = json.loads(data)
    except:
        js = None
    if not js or 'features' not in js:
        print('===Download Error')
        print(data)
        break
    if len(js['features']) == 0:
        print('===Object not Found===')
        print(data)
        break
    print(json.dumps(js, indent=4))
    plus_code = js['features'][0]['properties']['plus_code']
    print('Plus code:', plus_code)