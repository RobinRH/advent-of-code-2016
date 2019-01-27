# 20092
#
# https://adventofcode.com/2016/day/14

import sys
import pprint
import re
import string
import numpy as np 
import hashlib

# test
inputKey = 'abc'


# real
inputKey = 'ngcjuoqr'

def findFirstTriple(s):

    letter = ''
    s = list(s)
    for x in range(len(s) - 2):
        if s[x] == s[x+1] and s[x] == s[x+2]:
            letter = s[x]
            return letter

    return ''

def hasQuintuple(s, letter):
    return letter * 5 in s

hashes = []
# create a whole bunch of keys
for i in range(30000):
    string = inputKey + str(i)
    m = hashlib.md5()
    m.update(string)
    digest = str(m.hexdigest()).lower()
    # then has that 2016 times
    currentHash = digest
    #print currentHash
    for repeats in range(2016):
        m = hashlib.md5()
        m.update(currentHash)
        currentHash = str(m.hexdigest()).lower()

    hashes.append(currentHash)
    #print currentHash
    if i % 1000 == 0:
        print i

keys = []
while len(keys) < 64:
    for j in range(len(hashes)):
        letter = findFirstTriple(hashes[j])
        if letter != '':
            found = False
            for k in range(j+ 1, j+1001):
                if hasQuintuple(hashes[k], letter):
                    keys.append(hashes[j])
                    found = True
                    print j, k, k - j, len(keys), hashes[j], hashes[k]
                    if len(keys) == 64:
                        exit()
                    break



 