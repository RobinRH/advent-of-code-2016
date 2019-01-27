# 92
#
# https://adventofcode.com/2016/day/13

import sys
import pprint
import re
import string
import numpy as np 

# test
inputKey = 10 # test
dest = (4, 7) # (row, col)

# real
inputKey = 1350
dest = (39, 31) # (row, col)

def isWall(x, y, key):
    #Find x*x + 3*x + 2*x*y + y + y*y.
    calc = (x * x) + (3 * x) + (2 * x * y) + y + (y * y)
    #Add the office designer's favorite number (your puzzle input).
    calc += key
    #Find the binary representation of that sum; count the number of bits that are 1.
    binary = "{0:b}".format(calc)
    #If the number of bits that are 1 is even, it's an open space.
    #If the number of bits that are 1 is odd, it's a wall.`
    ones = binary.count('1')
    return (ones % 2) != 0

size = 100
array = np.zeros((size,size), dtype=np.int8)
for row in range(size):
    for col in range(size):
        array[row, col] = 1 if isWall(col, row, inputKey) else 0

print array[0:10, 0:10]
print array[dest[0], dest[1]]
visited = set()
frontier = set()
frontier.add((1,1))

neighbors = [(0, 1), (-1, 0), (1, 0), (0, -1)]
count = 0
found = False
while not found:
    # remove items from the frontier
    if dest in frontier:
        found = True
        break

    newFrontier = set()
    for row, col in frontier:
        # find all the places you can go from there and add them to the new frontier
        for rowOff, colOff in neighbors:
            newRow, newCol = row + rowOff, col + colOff
            print newRow, newCol
            if (newRow >= 0) and (newCol >= 0) and (array[newRow, newCol] == 0):
                if (not (newRow, newCol) in visited) and (not (newRow, newCol) in newFrontier):
                    newFrontier.add((newRow, newCol))
        visited.add((row, col))

    #print 'count:', count
    #print 'frontier:', frontier
    #print 'new frontier:', newFrontier
    #print 'visited:', visited

    if dest in frontier:
        found = True
    else:
        frontier = newFrontier

    count += 1
    #if count > 10:
    #    break

    if count % 1000000:
        print count

print count

