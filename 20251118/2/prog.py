import sys

data = sys.stdin.buffer.read()
#print(data)
data_u_by = data.decode('UTF-8', errors='replace')
data_l = data_u_by.encode('latin1', errors='replace')
data_C = data_l.decode('CP1251', errors='replace')
# with open('2.out', 'w') as f:
#     f.write(data_C)
sys.stdout.write(data_C)
