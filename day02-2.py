# AC8C8
#
# https://adventofcode.com/2016/day/2

import sys

filename = sys.argv[1]
lines = []
with open(filename, 'r') as inputFile:
    lines = map(lambda s: s.strip(), inputFile.readlines())

o = 'X'
keypad = [
    [o,  o,   o,   o,   o,   o,  o],
    [o,  o,   o,  '1',  o,   o,  o],
    [o,  o,  '2', '3', '4',  o,  o],
    [o, '5', '6', '7', '8', '9', o],
    [o,  o,  'A', 'B', 'C',  o,  o],
    [o,  o,   o,  'D',  o,   o,  o],
    [o,  o,   o,   o,   o,   o,  o]
]

# start at 5
x = 1
y = 3

rules = {
    'U' : (0, -1),
    'D' : (0,  1),
    'L' : (-1, 0),
    'R' : (1, 0)
}

answer = ''
for line in lines:
    for step in line:
        rule = rules[step]
        if keypad[y + rule[1]][x + rule[0]] == 'X':
            pass
        else:
            x += rule[0]
            y += rule[1]
        # print step, x, y
    # print x, y
    answer += keypad[y][x]
    print answer

print answer
