import sys

data = sys.stdin.read()
data_b = data.encode('cp1251', errors='replace')
data_l = data_b.decode('latin1', errors='replace')
data_u = data_l.encode('UTF-8', errors='replace')
sys.stdout.buffer.write(data_u)
#print(data_u)