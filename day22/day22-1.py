#  1024
#
# https://adventofcode.com/2016/day/22

import sys
import pprint
import numpy as np 
import re

filename = sys.argv[1]
with open(filename, 'r') as inputFile:
    lines = list(inputFile)

lines.pop(0) # first line is a heading

lines = [s.strip().replace('/dev/grid/node-', '').replace('T','').replace('x','').replace('y','').replace('%','').replace('-',' ') \
    for s in lines]


# Filesystem              Size  Used  Avail  Use%
# /dev/grid/node-x0-y0     91T   71T    20T   78%
# 33 30   94   66    28   70

nodes = []
for line in lines:
    tokens = [int(t) for t in line.split(' ') if t]
    nodes.append(tokens[0:5])

def isViable(a, b):
    # Node A is not empty (its Used is not zero).
    # Nodes A and B are not the same node.
    # The data on node A (its Used) would fit on node B (its Avail).
    ax, ay, asize, aused, aavail = a
    bx, by, bsize, bused, bavail = b
    if aused == 0:
        return False

    if ax == bx and ay == by:
        return False

    if aused < bavail:
        return True
    else:
        return False


viablePairs = 0
for a in nodes:
    for b in nodes:
        if isViable(a, b):
            viablePairs += 1

print viablePairs

