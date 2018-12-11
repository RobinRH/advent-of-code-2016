# RRRLDRDUDD
#
# https://adventofcode.com/2016/day/17

import hashlib

testData = [
    ('hijkl', ''),
    ('ihgpwlah', 'DDRRRD'),
    ('kglvqrro', 'DDUDRLRRUDRD'),
    ('ulqzkmiv', 'DRURDRUDDLLDLUURRDULRLDUUDDDRR'),
    ('qtetzkpl', 'qtetzkpl')
]

# grid is 4x4
# you start at 0,0
# you need to get to 4,4

# The doors in your current room are either open or closed (and locked) based on the
# hexadecimal MD5 hash of a passcode (your puzzle input) followed by a sequence of uppercase characters
# representing the path you have taken so far (U for up, D for down, L for left, and R for right).

# Only the first four characters of the hash are used; they represent, respectively, 
# the doors up, down, left, and right from your current position. 
# Any b, c, d, e, or f means that the corresponding door is open; 
# any other character (any number or a) means that the corresponding door is closed and locked.
def getDoors(input):
    m = hashlib.md5()
    m.update(input)
    digest = m.hexdigest()
    up, down, left, right = \
        digest[0] in 'bcdef', \
        digest[1] in 'bcdef', \
        digest[2] in 'bcdef', \
        digest[3] in 'bcdef'
    #print up, down, left, right
    return up, down, left, right


for passcode, path in testData:
    print getDoors(passcode)

# a state is the path to get there and the location (row, col)
initial = ('qtetzkpl', 0, 0)
final = ('any', 3,3)
count = 0
done = False
currentLocations = [initial]
while not done:
    count += 1
    nextLocations = []
    for path, row, col in currentLocations:
        up, down, left, right = getDoors(path) 

        if up:
            newPath = path + 'U'
            newRow, newCol = row - 1, col
            if newRow >= 0:
                nextLocations.append([newPath, newRow, newCol])
            if newRow == 3 and newCol == 3:
                print count, newPath
                exit()

        if down:
            newPath = path + 'D'
            newRow, newCol = row + 1, col
            if newRow <= 3:
                nextLocations.append([newPath, newRow, newCol])
            if newRow == 3 and newCol == 3:
                print count, newPath
                exit()


        if left:
            newPath = path + 'L'
            newRow, newCol = row, col - 1
            if newCol >= 0:
                nextLocations.append([newPath, newRow, newCol])
            if newRow == 3 and newCol == 3:
                print count, newPath
                exit()


        if right:
            newPath = path + 'R'
            newRow, newCol = row, col + 1
            if newCol <= 3:
                nextLocations.append([newPath, newRow, newCol])
            if newRow == 3 and newCol == 3:
                print count, newPath
                exit()


    currentLocations = nextLocations


print count