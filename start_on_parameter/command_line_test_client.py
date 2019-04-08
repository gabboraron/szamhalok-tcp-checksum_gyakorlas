import socket
import struct
import sys

server_ip 	= sys.argv[1]
server_port = int(sys.argv[2])

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (server_ip, server_port)
connection.connect(server_address)


data = connection.recv(1024)
print(data.decode('UTF-8'))

connection.close()