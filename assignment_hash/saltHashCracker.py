#!/usr/bin/env python 
import sqlite3 as lite
import sys
import hashlib

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

commonWords = ["www.exploringsecurity.com", "exploringsecurity.com", "exploringsecurity"]

def generateArrayOfPossibleValuesBasedOnPolicy(modifiedDate):
    #if date is before May 2010 => 5-7 digits
    #if after => alphanumeric, 5-7 chars in length
    return 0

def computeCryptoHash(stringVal):
    m = hashlib.sha1()
    m.update(stringVal.encode('utf-8'))
    return m.hexdigest()
    
def combineCommonWordsAndPassToCompare(passwordFromDictionary, allHashList):
    for commonWord in commonWords:
        wordAndPass = commonWord + passwordFromDictionary;
        wordCommaAndPass = commonWord + ',' + passwordFromDictionary

        hashedCommonWordAndPass = computeCryptoHash(wordAndPass)
        hashedCommonWordAndPassWithComma = computeCryptoHash(wordCommaAndPass)

        if hashedCommonWordAndPass in allHashList:
            print "[{}] from: [sha1( {}{} )]".format(hashedCommonWordAndPass, commonWord, passwordFromDictionary)
            return True
        else:
            print "INVALID [{}] from: [sha1( {}{} )]".format(hashedCommonWordAndPass, commonWord, passwordFromDictionary)
        if hashedCommonWordAndPassWithComma in allHashList:
            print "[{}] from: [sha1( {}{} )]".format(hashedCommonWordAndPassWithComma, commonWord, passwordFromDictionary)
            return True
        else:
            print "INVALID [{}] from: [sha1( {}{} )]".format(hashedCommonWordAndPassWithComma, commonWord, passwordFromDictionary)
    
    return False


con = None
try:
    con = lite.connect('garda.sqlite')
    cur = con.cursor()    
    #cur.execute('SELECT SQLITE_VERSION()')
    #data = cur.fetchone()
    #print "SQLite version: %s" % data    

    allHashList = []
    cur.execute("SELECT * FROM recovered")
    while True:
        row = cur.fetchone()    
        if row == None:
            break
        realHashPasswordFromDB = row[2];
        allHashList.append(realHashPasswordFromDB)

    with open("password.lst") as f:
        for line in f:
            passwordFromDictionary = line.rstrip('\n')
            
            matchFound = combineCommonWordsAndPassToCompare(passwordFromDictionary, allHashList)
            if matchFound:
                break
    
except lite.Error, e:
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    if con:
        con.close()