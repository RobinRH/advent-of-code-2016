# northpole/object/storage 548
#
# https://adventofcode.com/2016/day/4

import sys
import pprint
import re
from collections import Counter

zNumber = ord('z') # 122
aNumber = ord('a') # 97

def rotate(letter, number):
    number = number % 26
    letterNumber = ord(letter)
    letterNumber += number
    if letterNumber > zNumber:
        letterNumber = aNumber + (letterNumber - zNumber) - 1
    return chr(letterNumber)

lines = []
with open(sys.argv[1], 'r') as inputFile:
    lines = inputFile.readlines()

# example room: aaaaa-bbb-z-y-x-123[abxyz]
ruleExpr = re.compile('(?P<letters>.+)-(?P<digits>\d+)\[(?P<checksum>.+)\]')

for line in lines:
    match = ruleExpr.match(line)
    if match:
        checksum, digits, letters = match.group('checksum'), match.group('digits'), match.group('letters')

        # get the count of each letter
        counts = Counter(match.group('letters').replace('-', ""))

        # convert the counts to tuples and then sort
        # negate the count so that ascending sort works for both the count and the letter
        countTuples = map(lambda k: (-counts[k], k), counts.keys())
        sortedTuples = sorted(countTuples)

        # get the first 5
        check = ''
        for i in range(0,5):
            check += sortedTuples[i][1]

        digits = int(digits)
        if check == checksum:
            rotatedLetters = map(lambda c : rotate(c, digits), letters)
            word = ''.join(rotatedLetters)
            if word.find('pole') != -1:
                print word, digits
                break

    else:
        print 'no match'


