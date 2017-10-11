import sys
import random

if len(sys.argv) != 5:
    print "Usage: streamCypherUtility.py e/d longintkey [path]inputFileName [path]outputFileName"
    sys.exit()

mode,longIntKey,inputFileName,outputFileName=sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]

def applyLogic(multiplier, valueAdded):
    inputFile = open( inputFileName, "rb")
    bytearr = map (ord, inputFile.read () )
    outoutFile = open( outputFileName, "wb" )
    for i in range(len(bytearr)):
        byt = (bytearr[i] + (multiplier * random.randint(0, 255)) + valueAdded) % 256
        outoutFile.write(chr(byt))
    outoutFile.close()
    inputFile.close()

key = long(longIntKey) 
random.seed(key)

# encryption
if mode == "e": 
    applyLogic(1, 0)

# decryption
if mode == "d": 
    applyLogic(-1, 256)