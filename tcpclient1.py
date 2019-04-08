import socket
import struct

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 22223)

connection.connect(server_address)


values = "bela"
values = input()
connection.sendall(values.encode('UTF-8'))

data = connection.recv(1024)
print(data.decode('UTF-8'))

connection.close()
