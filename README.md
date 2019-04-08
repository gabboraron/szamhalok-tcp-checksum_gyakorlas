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
fájl: `command_line_arg.py`
````Python
import sys

print (sys.argv)
````
Ha az első megadott elemet akarjuk lekérni akkor: 
````Python
print (sys.argv[1])
````
A `0` érték a program nevét adja vissza, ugyanis az _"a 0. elem"_.

## Parancssori argumentumként elstartoltatni a servert, klienst
A kliens és a szerver egy-egy parancssori argumentumban kapja meg az IP-t és a portot amin elstartotl, pl: `kliens.py ip port`. Ekkor ha a korábbi tcpt használjuk figyleni kell, hogy a `server_address = (server_ip, server_port)`-nek a második argumentuma _szám_ kell legyen, azaz, így vegyük át például: `server_port = int(sys.argv[2])`

fájlok: `start_on_parameter/start_server_oncommand_line_arg.py` és `start_on_parameter/command_line_test_client.py`
