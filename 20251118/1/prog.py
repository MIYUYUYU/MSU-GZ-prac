import sys

data = sys.stdin.buffer.read()
#print(data)
N = data[0]
tail = data[1:]
length = len(tail)
output = []
if length < N:
    for i in range(N):
        if i < length:
            output.append(tail[i:i+1].strip(b'\n'))
        else:
            output.append(b'')
else:
    for i in range(N):
        start = int(i * length / N)
        end = int((i + 1) * length / N)
        output.append(tail[start:end].strip(b'\n'))
output.sort()
#print(output)
out_by = bytes([N]) + b''.join(output)

sys.stdout.buffer.write(out_by)