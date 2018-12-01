# 287
#
# https://adventofcode.com/2016/day/1

import sys

filename = sys.argv[1]
with open(filename, 'r') as inputFile:
    text = inputFile.read()

instructions = text.split(", ")
instructions = [ (i[0], int(i[1:])) for i in instructions ]

north = 1
south = 2
east = 3
west = 4

direction = north
location = (0,0)

northNext = {"L" : west, "R" : east}
southNext = {"L": east, "R": west}
eastNext = {"L" : north, "R" : south}
westNext = {"L": south, "R" : north}

nextDirections = { north: northNext, south: southNext, east: eastNext, west: westNext}

for i in instructions:
    direction = nextDirections[direction][i[0]]
    if direction == north:
        location = (location[0], location[1] + i[1])
    elif direction == south:
        location = (location[0], location[1] - i[1])
    elif direction == east:
        location = (location[0] + i[1], location[1])
    elif direction == west:
        location = (location[0] - i[1], location[1])


distance = abs(location[0]) + abs(location[1])
print distance
