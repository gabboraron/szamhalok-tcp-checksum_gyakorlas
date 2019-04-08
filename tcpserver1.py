import socket
import struct

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 22223)
sock.bind(server_address)

sock.listen(1)
while True:
	connection, client_address = sock.accept()
	data = connection.recv(1024)
	
	data = data.decode('UTF-8')
	print(data)
	reply = ("Hello, " + str(data) + " from Server")
	connection.sendall(str(reply).encode('UTF-8'))
	connection.close()
