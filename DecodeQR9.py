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
#horace = "6BFOXN%TSMAHN-HLVK5BK V4G:MR8EQP4ZVS92P%2F-%2HWCT-TAVDEJHC*2K1JZZPQA36S4HZ6SH9X5QF36FY1OSMNV1L8VNF6O M.5F4H6.DEAL6+96Z EUJE746V EXDM%/E/XED46LI6LS6IS6GPEHNAEN932QLOJ9ZILAPZXI$MI1VCSWC%PDGZK.9D.XIN$JN9T%XL.ZJV3CTTIC7JIZI.EJJ14B2MZ8DC8C6P10%C:XIBEIVG395EV3EVCK09D5WCFVA.QO5VA81K0ECM8CXVDC8C90JK.A+ C/8DXEDKG0CGJ5AL5:4A93ULJZI0LEQ8G6Q3QR$P*NIV1JK+2*JT.VSYZJ92KR8TCET4RLBUJC0J%B04T9.+0HD8J-6WKP/HLIJLKNF8JF172T0QMN6GTDWEDDJBUR540WG T+5I+VR9GJQZLW-431BERVTUJO%P/BN3+K.0K4LA9$UP SH7Q7BFJWK4QI2.T%O7U4L*67ZSQ/.TUCR700Y$2F0"
print("decoding payload: "+ horace)
decoded = base45.b45decode(horace)
decompressed = zlib.decompress(decoded)
cose = CoseMessage.decode(decompressed)
#print(cose)
partridge = (json2.dumps(cbor2.loads(cose.payload), indent=2))
print (partridge)
print (len(partridge))
with open('pheasant.txt', 'w') as f:
    f.write(partridge)
b = 0
length = len(partridge)
#PAUSEbit = input("Press return to continue program:")
while b < length:    
    if (partridge[b] == "c") and (partridge[b + 1] =="i"):
        print (partridge[(b + 6):(b +28)])
    b = b + 1
a = 0
#while a < 20:
 #   print (partridge[a])
  #  a = a + 1
#print (partridge[10],partridge[11])
#print (partridge[513:519]," ",end='')
#print (partridge[489:495])
ENDbit = input("Press return to end program:")