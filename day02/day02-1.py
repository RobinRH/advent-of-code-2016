# 78293
#
# https://adventofcode.com/2016/day/2

import sys

filename = sys.argv[1]
lines = []
with open(filename, 'r') as inputFile:
    lines = inputFile.readlines()

lines = map(lambda s : s.strip(), lines)

keypad = [[1,2,3], [4,5,6], [7,8,9]]

# make the center, 5, the origin
x = 0
y = 0

total = 0
for line in lines:
    for step in line:
        if step == 'U':
            y -= 1
            if y < -1 : y = -1
        elif step == 'D':
            y += 1
            if y > 1 : y = 1
        elif step == 'R':
            x += 1
            if x > 1 : x = 1
        else: # step == 'L'
            x -= 1
            if x < -1 : x = -1
        # print step, x, y
    # print x, y
    answer = keypad[y + 1][x + 1]
    total = (total * 10) + answer
    print answer

print total

