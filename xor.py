#!/usr/bin/python3

import sys

asc = ''
hx = ''

for x,y in zip(sys.argv[1], sys.argv[2]):

    c = ord(x) ^ ord(y)
    asc += chr(c)
    hx += '{:02X}'.format(c)

print(asc, '\n', hx)
    

