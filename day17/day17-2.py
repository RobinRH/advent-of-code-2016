# 706
# find the longest path
# https://adventofcode.com/2016/day/17

import hashlib

testData = [
    ('hijkl', ''),
    ('ihgpwlah', 370),
    ('kglvqrro', 492),
    ('ulqzkmiv', 830),
    ('qtetzkpl', 0)
]

# grid is 4x4
# you start at 0,0
# you need to get to 4,4

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
maxPath = 0
while currentLocations:
    count += 1
    nextLocations = []
    for path, row, col in currentLocations:
        up, down, left, right = getDoors(path) 

        if up:
            newPath = path + 'U'
            newRow, newCol = row - 1, col
            if newRow == 3 and newCol == 3:
                print count, len(newPath)
                maxPath = max(maxPath, count)
            elif newRow >= 0:
                nextLocations.append([newPath, newRow, newCol])

        if down:
            newPath = path + 'D'
            newRow, newCol = row + 1, col
            if newRow == 3 and newCol == 3:
                print count, len(newPath)
                maxPath = max(maxPath, count)
            elif newRow <= 3:
                nextLocations.append([newPath, newRow, newCol])


        if left:
            newPath = path + 'L'
            newRow, newCol = row, col - 1
            if newRow == 3 and newCol == 3:
                print count, len(newPath)
                maxPath = max(maxPath, count)
            elif newCol >= 0:
                nextLocations.append([newPath, newRow, newCol])


        if right:
            newPath = path + 'R'
            newRow, newCol = row, col + 1
            if newRow == 3 and newCol == 3:
                print count, len(newPath)
                maxPath = max(maxPath, count)
            elif newCol <= 3:
                nextLocations.append([newPath, newRow, newCol])

    currentLocations = nextLocations
    print count, len(currentLocations)


print count
print maxPath