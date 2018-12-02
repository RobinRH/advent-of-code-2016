# qqqluigu
#
# https://adventofcode.com/2016/day/6

import sys
import pprint
import numpy as np 
from collections import Counter

with open(sys.argv[1], 'r') as inputFile:
    lines = inputFile.readlines()

# convert each word into an array of chars
# then transpose so that each column becomes a row
lines = map(lambda word : list(word.strip()), lines)
data = np.transpose(lines)

# get the counts for each row (which is a column in the input file)
# find the char with the highest count
answer = ''
for row in data:
    counts = Counter(row)
    countTuples = map(lambda k: (counts[k], k), counts.keys())
    sortedTuples = sorted(countTuples, reverse=True)
    answer += sortedTuples[0][1]

print answer
