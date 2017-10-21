#!/usr/bin/python 
# # This is the program we believe was used to encode the intercepted message.
# some of the retrieved program was damaged (show as &&&&)
# Can you use this to figure out how it was encoded and decode it? 
# Good Luck

import string
import random
import unittest
import sys, traceback
from base64 import b64encode, b64decode
from itertools import permutations


# We are going to try to do some Reverese Engineering, since the hacker was encripting
# things randomly up to conuter times, we can try to use brute force  =all permutations 
# of the reverse part of the encoding to try to decode

secret = '&&&&&&&&&&&&&&' # We don't know the original message or length
iterations=0

def step1(s):
	_step1 = string.maketrans("zyxwvutsrqponZYXWVUTSRQPONmlkjihgfedcbaMLKJIHGFEDCBA",
							   "mlkjihgfedcbaMLKJIHGFEDCBAzyxwvutsrqponZYXWVUTSRQPON")
	return string.translate(s, _step1)

def step1r(s):
    	_step1 = string.maketrans("mlkjihgfedcbaMLKJIHGFEDCBAzyxwvutsrqponZYXWVUTSRQPON",
								   "zyxwvutsrqponZYXWVUTSRQPONmlkjihgfedcbaMLKJIHGFEDCBA")
	return string.translate(s, _step1)

def step2(s): return b64encode(s)

def step2r(s):
	value = ""
	try:
		value = b64decode(s)
	except:
		print "Error decoding string"
	return  value

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
	lines = [line.rstrip('\n') for line in open('intercepted7.txt')]
	try:
		for l in lines:
			userAlgorithm = int(l[0])
			lineToDecode = l[1:]
			print "User Algorithm: {}".format(super_dencoding[userAlgorithm-1].__name__)
			#for count in xrange(userAlgorithm):
			#for algorithm in super_dencoding:
			print super_dencoding[userAlgorithm-1](lineToDecode)
	except ValueError:
		print "Error in number"

def recover_secret_2(algorithmNumber, message):
	global iterations 
	iterations = iterations+1
	keyToQuit = raw_input('Try again? ')
	if keyToQuit.lower() == "q":
		sys.exit(0)
	decodedMessage = super_dencoding[algorithmNumber-1](message)
	print "message: [{}]".format(decodedMessage)
	print "Iteration [{}]. Used Algorithm: {}".format(iterations, super_dencoding[algorithmNumber-1].__name__)
	try:
		newIndexAlgorithm = int(decodedMessage[0])
		newMessage = decodedMessage[1:]
		recover_secret_2(newIndexAlgorithm, newMessage)
	except ValueError:
		print "The index is not an int anymore. Message should be clear now"
		sys.exit(0)

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

def main():
	try:
		print "Please press q to exit."
		lines = [line.rstrip('\n') for line in open('intercepted.txt')]
		for l in lines:
			algorithmIndex = int(l[0])
			messageToDecode = l[1:]
			recover_secret_2(algorithmIndex, messageToDecode)
	except KeyboardInterrupt:
		print "Shutdown requested...exiting"
	except Exception:
		traceback.print_exc(file=sys.stdout)
	sys.exit(0)

if __name__ == '__main__':
	#unittest.main()
	main()
	#print make_secret(secret, count=&&&)
    	

