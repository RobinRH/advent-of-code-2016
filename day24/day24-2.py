# 724
# 
# https://adventofcode.com/2016/day/24

import sys
import itertools
import numpy as np 

'''
###########
#0.1.....2#
#.#######.#
#4.......3#
###########
'''

def manhattanDistance(a, b):
    ay, ax = a
    by, bx = b
    return (abs(ay - by) + abs(ax - bx))

def reconstructPath(cameFrom, current, start):

    path = [current]
    while not path[-1] == start:
        path.append(cameFrom[path[-1]])
    return path

def getLowestFScore(openset, fscore):
    # fscore is dictionary of (y, x) and cost to get to (y, x)
    # openset is an array of (y, x)
    lowestValue = fscore[openset[0]] # pick any random value in fscore
    lowestKey = None
    # find the key for the lowest value
    for key in openset:
        if fscore[key] <= lowestValue:
            lowestValue = fscore[key]
            lowestKey = key
    return lowestKey

def distanceBetween(a, b):
    return 1

neighbors = [(-1,0), (0,-1), (0,1), (1,0)]
def getNeighbors((y, x), cave):
    goodNeighboors = []
    for n in neighbors:
        newPoint = (y + n[0], x + n[1])
        if cave[newPoint[0], newPoint[1]] in '.0123456789':
            goodNeighboors.append(newPoint)
    return goodNeighboors


def astar(start, goal, cave):
    # pseudocode from wikipedia
    visited = set()
    frontier = [start]
    cameFrom = {}
    gScore = {}
    gScore[start] = 0   # cost to current point
    fScore = {}         # minimun cost to goal

    fScore[start] = manhattanDistance(start, goal)

    while len(frontier) > 0:
        current = getLowestFScore(frontier, fScore)
        if current == goal:
            return reconstructPath(cameFrom, current, start)

        frontier.remove(current)
        visited.add(current)

        neighbors = getNeighbors(current, cave)
        for neighbor in neighbors:
            if neighbor in visited:
                continue

            currentCost = gScore[current] + distanceBetween(current, neighbor)

            if not neighbor in frontier:
                frontier.append(neighbor)
            elif currentCost >= gScore[neighbor]:
                continue       

            cameFrom[neighbor] = current
            gScore[neighbor] = currentCost
            fScore[neighbor] = gScore[neighbor] + manhattanDistance(neighbor, goal)

with open(sys.argv[1], 'r') as inputFile:
    lines = [line.strip() for line in list(inputFile)]

alldata = ''.join(lines)
nrows = len(lines)
ncols = len(lines[0])

cave = np.array(list(alldata), dtype = str)
cave = cave.reshape((nrows, ncols))

interests = {}
for r in range(nrows):
    for c in range(ncols):
        if cave[r,c] in list('0123456789'):
            interests[cave[r,c]] = (r,c)

routes = list(itertools.permutations(interests.keys(), len(interests)))
routes = [list(route) for route in routes if route[0] == '0']
for route in routes:
    route.append('0')


lengths = {}
for ainterest in interests.keys():
    for binterest in interests.keys():
        apoint = interests[ainterest]
        bpoint = interests[binterest]
        path = astar(apoint, bpoint, cave)
        length = len(path) - 1
        lengths[(ainterest, binterest)] = length

distances = {}
for route in routes:
    legs = [(route[i],route[i + 1]) for i in range(len(route) -1)]
    total = 0
    for leg in legs:
        total += lengths[leg]
    distances[tuple(route)] = total


print min(distances.values())