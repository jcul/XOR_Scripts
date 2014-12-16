#!/usr/bin/python3

import os
import sys
import struct

# Simple script to xor two files together

with open(sys.argv[1], 'rb') as fh1, open(sys.argv[2], 'rb') as fh2:

    file1Data = fh1.read()
    file2Data = fh2.read()

length = min(len(file1Data), len(file2Data))

with open("output.xor", 'wb') as outFH:

    for i in range(length):
            outFH.write(struct.pack('B', file1Data[i] ^ file2Data[i]))
