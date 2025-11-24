# with open('2.in','rb') as f:
#      data = f.read()
import sys
data = sys.stdin.buffer.read()
if data[8:12] != b'WAVE' or data[0:4] != b'RIFF' or data[12:16] != b"fmt ":
    print('NO')
    exit(0)
Size = int.from_bytes(data[4:8], byteorder='little')
Type = int.from_bytes(data[20:22], byteorder='little')
Channels = int.from_bytes(data[22:24], byteorder='little')
Rate = int.from_bytes(data[24:28], byteorder='little')
Bits = int.from_bytes(data[34:36], byteorder='little')
size = int.from_bytes(data[40:44], byteorder='little')
print(f'{Size=}, {Type=}, {Channels=}, {Rate=}, {Bits=}, Data {size=}')