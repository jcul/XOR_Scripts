#!/usr/bin/env python3

import sys

# This script xors a file with an xor "key" provided on the command line

ifh = open(sys.argv[1], 'rb')
ofh = open(sys.argv[1] + ".dec", 'wb')

keystr = ''.join(sys.argv[2:]).replace(' ', '')
print("KEY:", keystr)

key = bytearray.fromhex(sys.argv[2])
key_pos = 0

packet_size = len(key)
packet = ifh.read(packet_size)

while(len(packet) != 0):
    
    new_packet = bytearray(packet)

    for i in range(len(new_packet)):
        new_packet[i] = new_packet[i] ^ key[key_pos]
        key_pos = (key_pos + 1) % packet_size

    ofh.write(new_packet)

    packet = ifh.read(packet_size)

ifh.close()
ofh.close()
