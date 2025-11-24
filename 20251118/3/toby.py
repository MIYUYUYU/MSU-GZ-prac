with open('phone.wav','rb') as f:
     with open('1.in','wb') as g:
         g.write(f.read())
with open('logo_msu.svg', 'rb') as f:
    with open('2.in', 'wb') as g:
        g.write(f.read())
with open('phone.wav', 'rb') as f:
    data = bytearray(f.read())
    data[0:4] = b'RFFI'
    with open('3.in', 'wb') as g:
        g.write(data)