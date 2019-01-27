# 115
#
# https://adventofcode.com/2016/day/8

import sys
import pprint
import numpy as np 
import re

rectangle = 1
row = 2
column = 3


# create the rules
with open(sys.argv[1], 'r') as inputFile:
    rules = map(lambda s : s.strip(), list(inputFile))

array = np.zeros((6, 50))

# rect 1x2
# rotate row y=1 by 13
# rotate column x=0 by 1
recRule = re.compile('rect (?P<width>\d+)x(?P<height>\d+)')
rowRule = re.compile('rotate row y=(?P<row>\d+) by (?P<n>\d+)')
colRule = re.compile('rotate column x=(?P<column>\d+) by (?P<n>\d+)')


for rule in rules:
    recMatch = recRule.match(rule)
    rowMatch = rowRule.match(rule)
    colMatch = colRule.match(rule)

    if recMatch:
        width, height = int(recMatch.group('width')), int(recMatch.group('height'))
        array[0:height, 0:width] = 1
    elif rowMatch:
        row, n = int(rowMatch.group('row')), int(rowMatch.group('n'))
        array[row] = np.roll(array[row], n, axis = 0)
    elif colMatch:
        column, n = int(colMatch.group('column')), int(colMatch.group('n'))
        array[:, column] = np.roll(array[:, column], n, axis = 0)

print array
print np.sum(array)