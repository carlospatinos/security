import string
rot13 = string.maketrans( 
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
print string.translate("Uryyb Jbeyq!", rot13)   

if len(sys.argv) != 3:
    print "Usage: rot13.py e/d message"
    sys.exit()

mode,plaintext=sys.argv[1],sys.argv[2]