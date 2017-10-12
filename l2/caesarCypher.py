import sys

ALPHABET="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBER_CHARACTERS=26
L2I = dict(zip(ALPHABET, range(NUMBER_CHARACTERS)))
I2L = dict(zip(range(NUMBER_CHARACTERS), ALPHABET))


if len(sys.argv) != 4:
    print "Usage: caesarCypher.py e/d key message"
    sys.exit()

mode,key,plaintext=sys.argv[1],int(sys.argv[2]),sys.argv[3]
key if key is not None else 3

def applyLogic(multiplier):
    ciphertext = ""
    for c in plaintext.upper():
        if c.isalpha(): ciphertext += I2L[ (L2I[c] + (multiplier * key) ) % NUMBER_CHARACTERS ]
        else: ciphertext += c
    print ciphertext

# encryption
if mode == "e": 
    applyLogic(1)

# decryption
if mode == "d": 
    applyLogic(-1)