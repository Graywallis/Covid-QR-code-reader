#! /usr/bin/env python3
import json2
import sys
import zlib
import base45
import cbor2
from cose.messages import CoseMessage
horace = "ab"
horace = input("Enter your value: ")
horace = horace.replace("HC1:", "")
print("decoding payload: "+ horace)
decoded = base45.b45decode(horace)
decompressed = zlib.decompress(decoded)
cose = CoseMessage.decode(decompressed)
partridge = (json2.dumps(cbor2.loads(cose.payload), indent=2))
print (partridge)
print (len(partridge))
with open('pheasant.txt', 'w') as f:
    f.write(partridge)
b = 0
length = len(partridge)
while b < length:    
    if (partridge[b] == "c") and (partridge[b + 1] =="i"):
        print (partridge[(b + 6):(b +28)])
    b = b + 1
a = 0
ENDbit = input("Press return to end program:")