import socket
mock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mock.send(cmd)

while True:
	data = mock.recv(512)
	if len(data)<1:
		break
	print(data.decode())
mock.close()