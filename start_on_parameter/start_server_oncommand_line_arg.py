import socket
import struct
import sys

server_ip 	= sys.argv[1]
server_port = int(sys.argv[2])

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (server_ip, server_port)
sock.bind(server_address)

sock.listen(1)
while True:
	connection, client_address = sock.accept()
	reply = ("Hello")
	connection.sendall(str(reply).encode('UTF-8'))
	connection.close()
