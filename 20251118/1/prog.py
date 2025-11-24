import sys

data = sys.stdin.buffer.read()

if len(data) == 0:
    sys.exit(0)

N = data[0]
tail = data[1:]
L = len(tail)

parts = []
for i in range(N):
    start = int(i * L / N)
    end = int((i + 1) * L / N)
    part = tail[start:end]
    parts.append(part)

parts.sort()
result = bytes([N]) + b''.join(parts)
sys.stdout.buffer.write(result)