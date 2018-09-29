import socket
import multiprocessing
import os

def handle(connection, client_address):
	print('servicing', client_address)

	content = ''

	while True:
		data = connection.recv(1)

		if data:
			content += data.decode()
		else:
			break;

		if content[-4:] == '\r\n\r\n': break

	path_line = content.split('\n')[0]
	path = path_line.split(' ')[1]
	filename = path.split('/')[-1]

	mime = 'text/html'

	body = ''

	# handle html
	if path.endswith('.html'):
		with open(filename) as file:
			body = file.read()

	# handle jpg
	if path.endswith('.jpg'):
		mime = 'image/jpeg'
		with open(filename, 'rb') as file:
			body = file.read()

	# handle python
	if path.endswith('.py'):
		body = os.popen('python3 %s' % filename).read()

	if body == '':
		body = '404'

	try:
		body = body.encode()
	except:
		pass

	connection.send(b'HTTP/1.1 200 OK\r\n')
	connection.send('Content-Type: {0}\r\n'.format(mime).encode())
	connection.send('Content-Length: {0}\r\n'.format(len(body)).encode())
	connection.send(b'\r\n')
	connection.send(body)
	connection.send(b'\r\n\r\n')

	connection.close()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 8080))
sock.listen(1)

while True:
	connection, client_address = sock.accept()
	print('accepted new connection')

	process = multiprocessing.Process(target=handle, args=(connection, client_address))
	process.start()
