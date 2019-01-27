# 19449262
#
# https://adventofcode.com/2016/day/20

import sys
import pprint

filename = sys.argv[1]
with open(filename, 'r') as inputFile:
    lines = list(inputFile)

def isValid(number):
    for interval in intervals:
        if number >= interval[0] and number <= interval[1]:
            return False

    return True

intervals = {}
for line in lines:
    tokens = line.strip().split('-')
    interval = [int(s) for s in tokens]
    intervals[interval[0]] = interval

sortedIntervals = sorted(intervals.keys())

lowest = 0
for ikey in sortedIntervals:
    low, high = intervals[ikey]
    if low <= lowest and lowest <= high:
        lowest = high + 1

print lowest
