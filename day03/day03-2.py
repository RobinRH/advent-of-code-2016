# 1836
#
# https://adventofcode.com/2016/day/3

import sys
import pprint
import numpy as np 

# load the file into an array, an flatten along the columns
flat = np.loadtxt(sys.argv[1]).flatten('F')
# reshape into three columns
rows = np.reshape(flat, (-1, 3))

possible = 0
for (a, b, c) in rows:
    if (a + b > c) and (a + c > b) and (b + c > a):
        possible += 1

print possible

