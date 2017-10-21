# This is the program we believe was used to encode the intercepted message.
# some of the retrieved program was damaged (show as &&&&)
# Can you use this to figure out how it was encoded and decode it? 
# Good Luck

import string
import random
import unittest
from base64 import b64encode, b64decode
from itertools import permutations


# We are going to try to do some Reverese Engineering, since the hacker was encripting
# things randomly up to conuter times, we can try to use brute force  =all permutations 
# of the reverse part of the encoding to try to decode

secret = '&&&&&&&&&&&&&&' # We don't know the original message or length

def step1(s):
	_step1 = string.maketrans("zyxwvutsrqponZYXWVUTSRQPONmlkjihgfedcbaMLKJIHGFEDCBA",
							   "mlkjihgfedcbaMLKJIHGFEDCBAzyxwvutsrqponZYXWVUTSRQPON")
	return string.translate(s, _step1)

def step1r(s):
    	_step1 = string.maketrans("mlkjihgfedcbaMLKJIHGFEDCBAzyxwvutsrqponZYXWVUTSRQPON",
								   "zyxwvutsrqponZYXWVUTSRQPONmlkjihgfedcbaMLKJIHGFEDCBA")
	return string.translate(s, _step1)

def step2(s): return b64encode(s)

def step2r(s): return b64decode(s)

def step3(plaintext, shift=4):
    loweralpha = string.ascii_lowercase
    shifted_string = loweralpha[shift:] + loweralpha[:shift]
    converted = string.maketrans(loweralpha, shifted_string)
    return plaintext.translate(converted)

def step3r(plaintext, shift=4):
    loweralpha = string.ascii_lowercase
    shifted_string = loweralpha[shift:] + loweralpha[:shift]
    converted = string.maketrans(shifted_string, loweralpha)
    return plaintext.translate(converted)

secret_encoding = ['step1', 'step2', 'step3']
super_dencoding = [step1r, step2r, step3r]

def make_secret(plain, count):
	a = '2{}'.format(b64encode(plain))
	for count in xrange(count):
		r = random.choice(secret_encoding)
		si = secret_encoding.index(r) + 1
		_a = globals()[r](a)
		a = '{}{}'.format(si, _a)
	return a

def recover_secret():
	lines = [line.rstrip('\n') for line in open('intercepted.txt')]
	try:
		for l in lines:
			iterations = int(l[0])
			print "Number of iterations are: {}".format(iterations)
			for count in xrange(iterations):
				for al in super_dencoding:
    					print "function: {} => {}".format(al.__name__, al(l))
	except ValueError:
		print "Error in number"

	#print '2{}'.format(b64encode(plaintext))
	

class MyTest(unittest.TestCase):
    def test_step1(self):
    	s = 'Hola companeros'
        self.assertEqual(s, step1r(step1(s)))

    def test_step2(self):
        s = 'Hola companeros'
        self.assertEqual(s, step2r(step2(s)))

    def test_step3(self):
        s = 'Hola companeros'
        self.assertEqual(s, step3r(step3(s)))




if __name__ == '__main__':
	#unittest.main()
	#print make_secret(secret, count=&&&)
	#313312
	recover_secret()
    	

