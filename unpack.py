import zlib
import sys
if len(sys.argv) < 3:
    print('UNBOUND UPK Unpacker')
    print('Usage: <upk> <output>')

with output as open(sys.argv[2], 'wb'):
    upk = open(sys.argv[1], 'rb')
    header = upk.read(3)
    if header != b'UPK':
        print('This is not a UPK')
        exit(1)
    number_of_addrs = int(upk.read(1))
    offsets = []
    for i in range(number_of_addrs):
        offsets.append(int(upk.read(4))
    ...
        
        
    
