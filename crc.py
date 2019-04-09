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