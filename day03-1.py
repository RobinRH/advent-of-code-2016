# 983
#
# https://adventofcode.com/2016/day/3

import sys
import pprint

lines = []
with open(sys.argv[1], 'r') as inputFile:
    lines = inputFile.readlines()

# each column is 5 characters
possible = 0
for line in lines:
    a, b, c = map(lambda p : int(p), (line[0:5], line[5:10], line[10:15]))
    if (a + b > c) and (a + c > b) and (b + c > a):
        possible += 1

print possible
