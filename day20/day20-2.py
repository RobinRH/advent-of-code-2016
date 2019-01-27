# 119
#
# https://adventofcode.com/2016/day/20

import sys
import pprint

filename = sys.argv[1]
with open(filename, 'r') as inputFile:
    lines = list(inputFile)

intervals = {}
for line in lines:
    tokens = line.strip().split('-')
    interval = [int(s) for s in tokens]
    intervals[interval[0]] = interval

sortedIntervals = list(sorted(intervals.keys()))

def combine(intervals):
    combinedIntervals = {}
    sortedKeys = list(sorted(intervals.keys()))
    newIntervals = {}
    curLow, curHigh = intervals[sortedKeys[0]]

    for key in sortedKeys:
        low, high = intervals[key]
        if (low >= curLow and low <= curHigh):
            curHigh = max(curHigh, high)
        else: # save the current and start a new one
            newIntervals[curLow] = (curLow, curHigh)
            curLow, curHigh = low, high

    newIntervals[curLow] = (curLow, curHigh)

    return newIntervals


newIntervals = combine(intervals)

# max value, as defined in the problem
allNumbers = 4294967295 + 1

blockedNumbers = 0
for low, high in newIntervals.values():
    blockedNumbers += (high - low + 1)

print allNumbers - blockedNumbers
