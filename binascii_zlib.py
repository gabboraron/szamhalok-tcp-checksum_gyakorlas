import binascii
import zlib

test_string = 'FeketeRetek a rettenetes'

print("Input: {}".format(test_string))
print("binascii.crc32: {}".format(hex(binascii.crc32(bytearray(str(test_string).encode('UTF-8'))) % (1<<32) )) )
print("zlib.crc32:{}".format(hex(zlib.crc32((test_string).encode('UTF-8')) % (1<<32) )) )