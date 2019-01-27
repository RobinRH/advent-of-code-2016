# 1913, 19993564
# 
# https://adventofcode.com/2016/day/18

import sys
import pprint
import re
import string


with open(sys.argv[1], 'r') as inputFile:
    rows = map(lambda s: s.strip().split(' '), list(inputFile))

#Its left and center tiles are traps, but its right tile is not.
#Its center and right tiles are traps, but its left tile is not.
#Only its left tile is a trap.
#Only its right tile is a trap.
def isTrap(abc):
    #print abc
    return abc in ['^^.', '.^^', '^..', '..^']

def getRows(nRows, firstRow):
    grid = []
    firstRow = '.' + firstRow + '.'
    grid.append(firstRow)
    for row in range(1, int(nRows)):
        previousRow = grid[row - 1]
        nextRow = ''
        for i in range(1, len(firstRow) - 1):
            nextRow += '^' if isTrap(previousRow[i-1:i+2]) else '.'
        nextRow = '.' + nextRow + '.'
        grid.append(nextRow)
    return grid

def countTraps(grid):
    total = 0
    for row in grid:
        total += row.count('^')
    return total

for label, nRows, firstRow in rows:
    size = int(nRows) * len(firstRow)
    newGrid = getRows(nRows, firstRow)
    print label + ':', size - countTraps(newGrid)
    #pprint.pprint(newGrid)