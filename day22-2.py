# 230
# 
# https://adventofcode.com/2016/day/22


import sys
import pprint
#import numpy as np 
import re

class Node:
    def __init__(self, row, col, size, used, avail):
        self.row = row
        self.col = col
        self.size = size
        self.used = used
        self.avail = avail

    def __repr__(self):
        sep = '|'
        return "{0:>3}{1}{2:<3}".format(self.used, sep, self.avail)


class Cell:
    def __init__(self, size, used, avail, isPayload):
        self.size = size
        self.used = used
        self.avail = avail
        self.isPayload = isPayload

    def __repr__(self):
        sep = '*' if self.isPayload else '|'
        return "{0:>3}{1}{2:<3}".format(self.used, sep, self.avail)

def printGrid(grid, size):

    if size:
        for row in grid[0:size]:
            print ' '.join([str(a) for a in row[0:size]])
    else:
        for row in grid:
            print ' '.join([str(a) for a in row])

    print


filename = sys.argv[1]
with open(filename, 'r') as inputFile:
    lines = list(inputFile)

lines.pop(0)    # the first line is a heading

lines = [s.strip().replace('/dev/grid/node-', '').replace('T','').replace('x','').replace('y','').replace('%','').replace('-',' ') for s in lines]

# Filesystem              Size  Used  Avail  Use%
# /dev/grid/node-x0-y0     91T   71T    20T   78%
# 33 30   94   66    28   70

nodes = []
colMax = 0
rowMax = 0
emptySpace = (0,0) # (row, col)
for line in lines:
    col, row, size, used, avail, percent = [int(t) for t in line.split(' ') if t]
    # now want to reverse x and y
    nodes.append(Node(row, col, size, used, avail))
    #x,y = tokens[0:2]
    colMax = max(col, colMax)
    rowMax = max(row, rowMax)

grid = [[None for x in range(colMax + 1)] for y in range(rowMax + 1)]

def newGridFromNodes():
    global emptySpace
    newGrid = [[None for x in range(colMax + 1)] for y in range(rowMax + 1)]
    for node in nodes:
        newGrid[node.row][node.col] = Cell(node.size, node.used, node.avail, False)
        if node.used == 0:
            emptySpace = (node.row, node.col)

    newGrid[0][colMax].isPayload = True
    return newGrid


def isViable((arow, acol), a, (brow, bcol), b):
    """

    Args:
        a : Cell
        b : Cell
    """
    # Node A is not empty (its Used is not zero).
    # Nodes A and B are not the same node.
    # The data on node A (its Used) would fit on node B (its Avail).

    if a.used == 0:
        return False

    if acol == bcol and arow == brow:
        return False

    if a.used > b.avail:
        return False

    # make sure they are connected
    if (acol == bcol) and abs(arow - brow) == 1:
        return True
    elif (arow == brow) and abs(acol - bcol) == 1:
        return True
    else:
        return False


def isMoveViable(((arow, acol), (brow, bcol)), grid):
    """
    Call with (move, grid)
    Args:
        arow: 
        acol:
        brow:
        bcol:
        grid
    """
    # Node A is not empty (its Used is not zero).
    # Nodes A and B are not the same node.
    # The data on node A (its Used) would fit on node B (its Avail).
    a = grid[arow][acol]
    b = grid[brow][bcol]

    if a.used == 0:
        return False

    if acol == bcol and arow == brow:
        return False

    if a.used > b.avail:
        return False

    # make sure they are connected
    if (acol == bcol) and abs(arow - brow) == 1:
        return True
    elif (arow == brow) and abs(acol - bcol) == 1:
        return True
    else:
        return False


def applyMove(((arow, acol), (brow, bcol)), agrid):
    """
    Args:

    """
    global emptySpace
    # move a to b
    a = agrid[arow][acol]
    b = agrid[brow][bcol]
    b.used += a.used
    b.avail = b.size - b.used
    if b.avail < 0:
        print 'problem!'
    # a is now empty
    a.used = 0
    a.avail = a.size
    emptySpace = (arow, acol)

    if a.isPayload:
        a.isPayload = False
        b.isPayload = True


def applyPath(path, apgrid):
    """
    Args:
        path : array of (row, col) tuples
    """
    for move in path:
        applyMove(move, apgrid)


def getPairs(grid):
    """
    Returns:
        array of (row, col) tuples
    """
    pairs = []
    # emptySpace is the 0
    # see if the four surrounding spots can move in
    erow, ecol = emptySpace
    ecell = grid[erow][ecol]
    #b = (ex,ey, emptyCell.size, emptyCell.used, emptyCell.avail)
    neighbors = [(-1,0), (1,0), (0, -1), (0, 1)]
    for n in neighbors:
        newRow = erow + n[0]
        newCol = ecol + n[1]
        if newRow >= 0 and newRow <= rowMax and newCol >= 0 and newCol <= colMax:
            if isViable((newRow, newCol), grid[newRow][newCol], (erow, ecol), ecell):
                pairs.append(((newRow, newCol), (erow, ecol))) # this is OK, cell with stuff moves to cell without stuff
    return pairs


def clonePath(path):
    newPath = []
    for ((a,b),(c,d)) in path:
        newPath.append(((a,b),(c,d))) 
    return newPath

def testGame(moves):

    if not moves:
        moves = [
            ((0,1), (1,1)),
            ((0,2), (0,1)),
            ((1,2), (0,2)),
            ((1,1), (1,2)),
            ((1,0), (1,1)),
            ((0,0), (1,0)),
            ((0,1), (0,0))
        ]

    grid = newGridFromNodes()
    printGrid(grid, 3)
    for move in moves:
        applyMove(move, grid)
        print move
        printGrid(grid, 3)

    return grid

def isBacktrack(path, move):
    ((a1,a2),(b1,b2)) = path[-1]
    ((c1,c2),(d1,d2)) = move    
    if a1 == d1 and a2 == d2 and b1 == c1 and b2 == c2:
        return True
    else:
        return False


def getPathToLeftOfWall():
    path = []
    grid = newGridFromNodes()
    # see if you can move in a straight line from empty space over to column 
    while True:
        erow, ecol = emptySpace
        eCell = grid[erow][ecol]
        lrow, lcol = (erow, ecol-1)
        lcell = grid[lrow][lcol]
        if isViable((lrow, lcol), lcell, (erow, ecol), eCell):
            move = ((lrow, lcol), (erow, ecol))
            applyMove(move, grid)
            path.append(move)
        else:
            print "can't move"

        # check if empty space is in col 4
        if emptySpace[1] == 4:
            break

    return path


def getPathToTop():
    path = getPathToLeftOfWall()
    grid = newGridFromNodes()
    applyPath(path, grid)
    # see if you can move in a straight line from empty space up to the top
    while True:
        erow, ecol = emptySpace
        eCell = grid[erow][ecol]
        lrow, lcol = (erow-1, ecol)
        lcell = grid[lrow][lcol]
        if isViable((lrow, lcol), lcell, (erow, ecol), eCell):
            move = ((lrow, lcol), (erow, ecol))
            applyMove(move, grid)
            path.append(move)
        else:
            print "can't move"
            break

        # check if empty space is in col 4
        if emptySpace[0] == 0:
            break

    return path


def getPathToRight():
    path = getPathToTop()
    grid = newGridFromNodes()
    applyPath(path, grid)
    # see if you can move in a straight line from empty space up to the top
    while True:
        erow, ecol = emptySpace
        eCell = grid[erow][ecol]
        lrow, lcol = (erow, ecol+1)
        lcell = grid[lrow][lcol]
        if isViable((lrow, lcol), lcell, (erow, ecol), eCell):
            move = ((lrow, lcol), (erow, ecol))
            applyMove(move, grid)
            path.append(move)
        else:
            print "can't move"
            break

        #findPayload(grid)
        # check if empty space is in col 4
        if emptySpace[1] == colMax:
            break

    return path

# empty space is now all the way over to the right

# now that you are here
# how many steps does it take to move the goal over one space

# to move the goal over one
# move empty down one
# move empty left 2
# move move empty up 1
# move goal left one

# 5 steps each
col = 29
path = getPathToRight()
grid = newGridFromNodes()
applyPath(path, grid)
#findPayload(grid)
while True:

    #findPayload(grid)

    # getting path to right
    # move empty down one
    erow, ecol = emptySpace
    eCell = grid[erow][ecol]
    nrow, ncol = (erow + 1, ecol)
    ncell = grid[nrow][ncol]
    move = ((nrow, ncol), (erow, ecol))
    if isMoveViable(move, grid):
        applyMove(move, grid)
        path.append(move)
    else:
        'bad move'

    if grid[0][0].isPayload:
        print 'goal!', len(path)
        exit()

    # move empty left 2
    for i in range(2):
        erow, ecol = emptySpace
        eCell = grid[erow][ecol]
        nrow, ncol = (erow, ecol-1)
        ncell = grid[nrow][ncol]
        move = ((nrow, ncol), (erow, ecol))
        applyMove(move, grid)
        path.append(move)

    # move move empty up 1
    erow, ecol = emptySpace
    eCell = grid[erow][ecol]
    nrow, ncol = (erow -1, ecol)
    ncell = grid[nrow][ncol]
    move = ((nrow, ncol), (erow, ecol))
    if isMoveViable(move, grid):
        applyMove(move, grid)
        path.append(move)
    else:
        'bad move'

    # move goal left one (empty right one)
    erow, ecol = emptySpace
    eCell = grid[erow][ecol]
    nrow, ncol = (erow, ecol+1)
    ncell = grid[nrow][ncol]
    move = ((nrow, ncol), (erow, ecol))
    if isMoveViable(move, grid):
        applyMove(move, grid)
        path.append(move)
    else:
        'bad move'

    if grid[0][0].isPayload:
        print 'goal!', len(path)
        exit()
    if emptySpace[1] < 0:
        break



