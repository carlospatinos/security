#!/bin/env python
import argparse

#Frobnicate a string
def frobnicate(s):
    y = ''
    for x in s:
        y += chr(ord(x) ^ 42)
    return y

#Rotate by 0x80000 (UTF-16 rot)
def rot524288(s):
    y = ''
    for x in s:
        y += chr(ord(x) ^ 0x80000)
    return y

#Rotate by 0x8000 (UTF-8 rot)
def rot32768(s):
    y = ''
    for x in s:
        y += chr(ord(x) ^ 0x8000)
    return y

#Rotate by 47 (ASCII rot)
def rot47(s):
    x = []
    for i in range(len(s)):
        j = ord(s[i])
        if j >= 33 and j <= 126:
            x.append(chr(33 + ((j + 14) % 94)))
        else:
            x.append(s[i])
    return ''.join(x)

#Rotate by 13 (a-z  classic rot)
def rot13(s):
    for char in s:
        d = {}
        for c in (65, 97):
            for i in range(26):
                d[chr(i+c)] = chr((i+13) % 26 + c)
    return "".join([d.get(c, c) for c in s])

#Get arguments
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--frob', required=False)
parser.add_argument('-t', '--rot13', required=False)
parser.add_argument('-s', '--rot47', required=False)
parser.add_argument('-e', '--rot8000', required=False)
parser.add_argument('-y', '--rot80000', required=False)
parser.add_argument('-a', '--all', required=False)
args = parser.parse_args()

argsAsDictionary = vars(args)

def all(s):
    for key, value in argsAsDictionary.iteritems():
        try:
            print("    {}: {}".format(key, simpleDispatcher[key](s)))
        except:
            print("    Cannot parse the string using '{}' cypher.".format(key))
    return ""


dispatcher = {'rot47': rot47, 'frob': frobnicate, 'rot8000': rot32768, 'rot13': rot13, 'rot80000': rot524288, 'all': all}
simpleDispatcher = {'rot47': rot47, 'frob': frobnicate, 'rot8000': rot32768, 'rot13': rot13, 'rot80000': rot524288}

for key, value in argsAsDictionary.iteritems():
    if value is not None:
        print "======", key, "======"
        try:
            print(dispatcher[key](value))
        except:
            print("Cannot use {} string".format(key))
