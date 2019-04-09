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

## Checksum számítás
### 32 bites CRC
Ehhez tudnunk kell, hogy a `>>`, `<<` és `^` operátorok mit csinálnak:
- `x << y` Returns `x` with the **bits shifted to the left by y places** (and new bits on the right-hand-side are zeros). _This is the same as `multiplying x by 2**y`. _
- `x >> y` Returns `x` with the **bits shifted to the right by y places**. _This is the same as `//'ing x by 2**y`. _
- `x & y` Does a **"bitwise and"**. Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0. 
- `x | y` Does a **"bitwise or"**. Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1. 
- `~ x` Returns the **complement of `x`** - the number you get by switching each 1 for a 0 and each 0 for a 1. This is the same as `-x- 1`. 
- `x ^ y` Does a **"bitwise exclusive or"**. Each bit of the output is the same as the corresponding bit in x if that bit in y is 0, and it's the complement of the bit in x if that bit in y is 1. 
bővebben: https://wiki.python.org/moin/BitwiseOperators
    
fájl: `crc.py`
````Python
def create_table(poly):
	a = []
	for i in range(256):
		k = i
		for j in range(8):
			if k & 1:
				k ^= poly
			k >>= 1
		a.append(k)
	return a

def crc32(buf, crc_table):
	crc = 0xffffffff
	buf = bytearray((buf).encode('UTF-8'))
	for k in buf:
		crc = (crc >> 8) ^ crc_table[(crc & 0xff) ^ k]
	return crc ^  0xffffffff

gen_poly = 0x1db710640
crctable = create_table(gen_poly)

test_string = 'FeketeRetek a rettenetes'

print("Input: {}".format(test_string))
print("crc32: {}".format(hex(crc32(test_string, crctable) % (1<<32) )) )
````

## binascii és zlib

Ugyanezt elérhetjük úgy is, hogy nem kell mindezt implementálnunk, csupán a `binascii`-t vagy a `zlib`-et kell importálnunk és azokat helyesen használnunk, előbbit: `print("binascii.crc32: {}".format(hex(binascii.crc32(bytearray(str(test_string).encode('UTF-8'))) % (1<<32) )) )` utóbbit: `print("zlib.crc32:{}".format(hex(zlib.crc32((test_string).encode('UTF-8')) % (1<<32) )) )`. Mindkét, vagy mindhárom eljárás ugyanat a _checksum_ -ot számolja ki természetesen.
fájl: `binascii_zlib.py`
