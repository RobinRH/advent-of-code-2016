# 183269
#
# https://adventofcode.com/2016/day/9

import sys
import pprint
import re

with open(sys.argv[1], 'r') as inputFile:
    examples = map(lambda s : s.strip(), list(inputFile))

def expand(example):
    ruleExpr = re.compile('(?P<letters>[A-Z]*)\((?P<howmany>\d+)x(?P<repeat>\d+)\)(?P<moreletters>.*)')
    match = ruleExpr.match(example)
    if match:
        letters, howmany, repeat, moreletters = \
            match.group('letters'), int(match.group('howmany')), int(match.group('repeat')), match.group('moreletters')
        #print letters, howmany, repeat, moreletters

        answer = ''
        # add the intro letters to the answer
        answer += letters
        # get the howmany letters from the moreletters
        chars = moreletters[0:howmany]
        # repeat the letters and add them to the answer
        answer += chars * repeat
        # remove the chars from the remaining string
        leftovers = moreletters[howmany:]
        # expand the leftovers
        if leftovers != '' :            
            answer += expand(leftovers)

        return answer
    else:
        return example

for example in examples:
    answer = expand(example)
    print len(answer)

