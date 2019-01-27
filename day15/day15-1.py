# 148737 with 6 disks
# 2353212 with 7 disks
#
# https://adventofcode.com/2016/day/15

import sys
import pprint
import re

with open(sys.argv[1], 'r') as inputFile:   
    lines = map(lambda s : s.strip(), list(inputFile))

disks = {}
#Disc #1 has 5 positions; at time=0, it is at position 4.
for line in lines:
    line = line.replace('Disc #', '').replace('has ', '').replace('positions; at time=0, it is at position ', '').replace('.', '')
    tokens = line.split(' ')
    disk, positions, position = int(tokens[0]), int(tokens[1]), int(tokens[2])
    disks[disk] = [positions, position] 

pprint.pprint(disks)

def diskAtTime(positionAt0, positions, time):
    position = positionAt0
    time = time % positions
    for t in range(time):
        position += 1
        if position == positions:
            position = 0

    return position

def testTime(time):
    for diskNum in sorted(disks.keys()):
        d = disks[diskNum]
        time += 1
        position = diskAtTime(d[1], d[0], time)
        if position == 0:
            pass
        else:
            return False

    return True

def findTime():
    time = 0
    found = False
    while not found:
        success = testTime(time)
        if success:
            found = True
        else:
            time += 1
    return time


time7 = findTime()
del disks[7]
time6 = findTime()

print 'Part 1:', time6
print 'Part 2:', time7