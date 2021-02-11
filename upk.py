import sys
import zlib
if len(sys.argv) < 3:
     print('UNBOUND UPK File')
     print('Usage: <file> <output>')
with output as open(sys.argv[1], 'wb'):
    file = open(sys.argv[2], 'rb')
    data = file.read()
    file.close()
    compressed_data = zlib.compress(data)
    output.write(b'UPK') # Header
    output.write(b'\x01') # We have one address
    output.write(b'\x00000008') # There is data at 0x8 in the file
    output.write(compressed_data) # and this is our zlib compressed data
    
