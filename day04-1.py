# 173787
#
# https://adventofcode.com/2016/day/4

import sys
import pprint
import re
from collections import Counter

lines = []
with open(sys.argv[1], 'r') as inputFile:
    lines = inputFile.readlines()

# example room: aaaaa-bbb-z-y-x-123[abxyz]
ruleExpr = re.compile('(?P<letters>.+)-(?P<digits>\d+)\[(?P<checksum>.+)\]')

checksumTotal = 0
for line in lines:
    match = ruleExpr.match(line)
    if match:
        checksum, digits, letters = match.group('checksum'), match.group('digits'), match.group('letters')

        # get the count of each letter
        counts = Counter(match.group('letters').replace('-', ""))

        # convert the counts to tuples and then sort
        # negate the count so that ascending sort works for both the count and the letter
        countTuples = []
        for letter in counts.keys():
            countTuples.append((-counts[letter], letter))

        sortedTuples = sorted(countTuples)
        # get the first 5
        check = ''
        for i in range(0,5):
            check += sortedTuples[i][1]

        if check == checksum:
            checksumTotal += int(digits)
        else:
            print check

    else:
        print 'no match'


print checksumTotal