# TCP
## Alap tcp kommunikáció
fájl: `tcpclient1.py` és `tcpserver1.py`

__Server:__
szerver elstartoltatása:
````Python
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 22223)
sock.bind(server_address)
````
Kliens csatlakozására vár:
````Python
	connection, client_address = sock.accept()
````
Klienstől vár küldött szöveget amit dekódolnunk kell.
````Python
	data = connection.recv(1024)
	data = data.decode('UTF-8')
````
Kliensnek küld szöveget:
````Python
reply = ("Hello")
connection.sendall(str(reply).encode('UTF-8'))
````

__Kliens:__
kapcsolódás:
````Python
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 22223)
connection.connect(server_address)
````
konzolról olvasás és küldés:
````Python
values = input()
connection.sendall(values.encode('UTF-8'))
````
olvasás szervetől:
````Python
data = connection.recv(1024)
print(data.decode('UTF-8'))
````
Ha a kiírndó szöveget nem dekódoljuk akkor a küldéshez szükséges nyers formában kapjuk meg.

## Parancssori argumentum átvétele:
````Python
import sys

print (sys.argv)
````
Ha az első megadott elemet akarjuk lekérni akkor: 
````Python
print (sys.argv[1])
````
A `0` érték a program nevét adja vissza, ugyanis az _"a 0. elem"_.
