import socket
import re

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

data_buffer = ''
while True:
    data = mysock.recv(1024)
    if len(data) < 1:
        break
    data_buffer += data.decode()

mysock.close()

# Split headers and body
headers, body = data_buffer.split('\r\n\r\n', 1)

# Extract headers
last_modified = re.findall(r'^Last-Modified:\s*(.*)\s*', headers, re.MULTILINE)
etag = re.findall(r'^ETag:\s*"(.*?)"', headers, re.MULTILINE)
content_length = re.findall(r'^Content-Length:\s*(\d+)', headers, re.MULTILINE)
cache_control = re.findall(r'^Cache-Control:\s*(.*)', headers, re.MULTILINE)
content_type = re.findall(r'^Content-Type:\s*(.*)', headers, re.MULTILINE)

for value in last_modified:
    print(value)
for value in etag:
    print(value)
for value in content_length:
    print(value)
for value in cache_control:
    print(value)
for value in content_type:
    print(value)