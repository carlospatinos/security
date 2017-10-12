import string
import sys

rot13 = string.maketrans( 
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")

if len(sys.argv) != 2:
    print "Usage: rot13.py message"
    sys.exit()

text=sys.argv[1]

def applyLogic(value):
    print string.translate(value, rot13)

applyLogic(text)