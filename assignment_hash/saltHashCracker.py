#!/usr/bin/env python 
import sqlite3 as lite
import sys
import hashlib
from itertools import product
from string import *

# The purpose of the script is to use multiple convinations of values to generate hashes and find one in the db
# It is believed that cyrpto function was something like: CommonHash($salt,$pass)
# To generate salt we will 
# 1- Use commonWords and everyword in a dictionary
# 2- Use commonWords and a comma and everyword in a dictionary
# 3- Use Join_date and everyword in a dictionary
# 4- Use Join_date and a comma and everyword in a dictionary
# 5- Use Username and everyword in a dictionary
# 6- Use Username and a comma and everyword in a dictionary
# 7- Use Role and everyword in a dictionary
# 8- Use Role and a comma and everyword in a dictionary
# We are not using the Last_accessed and Pass_modified since that will mean that the system has to hash
# every time.

#https://github.com/carlospatinos/SecLists
#PASWORD_DICTIONARY_FILE="/home/ecapati/development/security/pass/10_million_password_list_top_1000.txt"
#PASWORD_DICTIONARY_FILE="password.lst"
#PASWORD_DICTIONARY_FILE="numbers5.txt"
#PASWORD_DICTIONARY_FILE="numbers6.txt"
PASWORD_DICTIONARY_FILE="numbers7.txt"


class DataOutput:
    found = []
    notFound = []

class TableData:
    passwords = []
    users = []
    
dataOutput = DataOutput()
tableData = TableData()

commonWords = ["www.exploringsecurity.com", "exploringsecurity.com", "exploringsecurity"]

def generateArrayOfPossibleValuesBasedOnPolicy(modifiedDate):
    #if date is before May 2010 => 5-7 digits
    #if after => alphanumeric, 5-7 chars in length
    return 0

def computeCryptoHash(stringVal):
    #print "Encoding {}".format(stringVal)
    m = hashlib.sha1()
    m.update(stringVal.encode('utf-8'))
    return m.hexdigest()
    
def combineCommonWordsAndPass(passwordFromDictionary, allHashList):
    for commonWord in commonWords:
        wordAndPass = commonWord + passwordFromDictionary;
        wordCommaAndPass = commonWord + ',' + passwordFromDictionary

        hashedCommonWordAndPass = computeCryptoHash(wordAndPass)
        hashedCommonWordAndPassWithComma = computeCryptoHash(wordCommaAndPass)

        if hashedCommonWordAndPass in allHashList.passwords:
            index = allHashList.passwords.index(hashedCommonWordAndPass)
            dataOutput.found.append("[{}] from: [sha1({}{}) for {}]".format(hashedCommonWordAndPass, commonWord, passwordFromDictionary, allHashList.users[index]))
            return True
        else:
            dataOutput.notFound.append("INVALID [{}] from: [sha1( {}{} )]".format(hashedCommonWordAndPass, commonWord, passwordFromDictionary))

        if hashedCommonWordAndPassWithComma in allHashList.passwords:
            dataOutput.found.append("[{}] from: [sha1({}{} for {})]".format(hashedCommonWordAndPassWithComma, commonWord, passwordFromDictionary, allHashList.users[index]))
            return True
        else:
            dataOutput.notFound.append("INVALID [{}] from: [sha1( {}{} )]".format(hashedCommonWordAndPassWithComma, commonWord, passwordFromDictionary))    
    return dataOutput

def generateLetterNumberCombinations():
    #keywords = (''.join(i) for i in product(ascii_letters + digits, repeat = 5))
    keywords = (''.join(i) for i in product(digits, repeat = 5))
    with open("numbers5.txt", "w") as f:
        for item in keywords: 
            f.write(item)
            f.write('\n')
    keywords = (''.join(i) for i in product(digits, repeat = 6))
    with open("numbers6.txt", "w") as f:
        for item in keywords:
            f.write(item)
            f.write('\n')
    keywords = (''.join(i) for i in product(digits, repeat = 7))
    with open("numbers7.txt", "w") as f:
        for item in keywords: 
            f.write(item)
            f.write('\n')

con = None
try:
    con = lite.connect('garda.sqlite')
    cur = con.cursor()    
    #cur.execute('SELECT SQLITE_VERSION()')
    #data = cur.fetchone()
    #print "SQLite version: %s" % data    

    cur.execute("SELECT * FROM recovered")
    while True:
        row = cur.fetchone()    
        if row == None:
            break
        realUserFromDB = row[1];
        realHashPasswordFromDB = row[2];
        tableData.users.append(realUserFromDB)
        tableData.passwords.append(realHashPasswordFromDB)


    with open(PASWORD_DICTIONARY_FILE) as f:
        for line in f:
            passwordFromDictionary = line.rstrip('\n')
            combineCommonWordsAndPass(passwordFromDictionary, tableData)

    print "#############################################"
    print "############### SOLUTION ####################"
    print "#############################################"
    for solution in dataOutput.found:
        print solution
    
except lite.Error, e:
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    if con:
        con.close()
