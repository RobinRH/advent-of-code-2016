# 11317278863
#
# https://adventofcode.com/2016/day/9

import sys
import pprint
import re

with open(sys.argv[1], 'r') as inputFile:
    examples = map(lambda s : s.strip(), list(inputFile))

def getLength(example):
    if example == '':
        return 0

    if not '(' in example:
        return len(example)
    
    ruleExpr = re.compile('(?P<letters>[A-Z]*)\((?P<howmany>\d+)x(?P<repeat>\d+)\)(?P<moreletters>.*)')
    match = ruleExpr.match(example)
    if match:
        letters, howmany, repeat, moreletters = \
            match.group('letters'), int(match.group('howmany')), int(match.group('repeat')), match.group('moreletters')

        length = 0
        # add the intro letters to the answer
        length += len(letters)
        # get the howmany letters from the moreletters
        chars = moreletters[0:howmany]
        # get the expanded length of that string
        length += repeat * getLength(chars)
        # remove the chars from the remaining string
        leftovers = moreletters[howmany:]
        tailLength = getLength(leftovers)
        length += tailLength

        return length
    else:
        return len(example)

for example in examples:
    answer = getLength(example)
    print answer
    print


