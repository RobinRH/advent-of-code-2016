# 57
# we know it's 57 because there are 12 additional
# steps between 2 sets on floor 1 and 3 sets on floor
# 1, so we just need to add 2*12, or 24 steps
# for these new items
# https://adventofcode.com/2016/day/11

import itertools
import numpy as np 

# 27
initial = {
    'aa': 1,
    'rg': 1,
    'rm': 1,
    'dg': 1,
    'dm': 1,
    'eg': 1,
    'em': 1
}
'''
27
.. .. .. .. .. .. ..
.. .. .. .. .. .. ..
.. .. .. .. .. .. ..
aa dg dm eg em rg rm
'''

# 15
initial = {
    'aa': 1,
    'rg': 1,
    'rm': 1,
    'eg': 1,
    'em': 1
}
'''
15
.. .. .. .. ..
.. .. .. .. ..
.. .. .. .. ..
aa eg em rg rm
'''

chips = filter(lambda s: s[-1]== 'm', initial.keys())
gens = filter(lambda s: s[-1]== 'g', initial.keys())

def printComponents(state):
    # create an array of items and then print it
    strings = ['..' for i in range(5 * len(state))]
    array = np.array(strings, dtype=np.dtype(str))
    array = array.reshape((5, len(state)))
    column = 0
    for c in sorted(state.keys()):
        array[state[c], column] = c
        column += 1

    print ' '.join(list(array[4, :]))
    print ' '.join(list(array[3, :]))
    print ' '.join(list(array[2, :]))
    print ' '.join(list(array[1, :]))
    return array

def isDone(state):
    # done when all components on the 4th floor
    return sum(state.values()) == 4 * len(state)

def isValidState(state):
    # state is a dictionary
    # the rules are pretty much just about mic
    for chip in chips:
        gen = chip.replace('m', 'g')
        # if m and c are on the same floor, it's all good
        if state[gen] == state[chip]:
            pass
        else: # make sure there are no other gens on the floor
            for g in gens:
                if state[g] == state[chip]: # on the same floor
                    return False

    return True

# get the set of all 1, 2 items you can move either up or down
def getValidMoves(state):
    # find all the items on the same floor
    onfloor = filter(lambda c : (state[c] == state['aa']) and (c != 'aa'), state.keys())

    # find all combinations of the comps on the floor
    moves = []
    possibleMoves = itertools.combinations(onfloor, 1)
    for pm in possibleMoves:
        moves.append(list(pm))
    possibleMoves = itertools.combinations(onfloor, 2)
    for pm in possibleMoves:
        moves.append(list(pm))

    return moves

def cloneState(state):
    newState = {}
    for c in state.keys():
        newState[c] = state[c]
    return newState

def getNextStates(state, moves):
    floor = state['aa']
    validStates = []

    # check going up
    if floor < 4:
        for move in moves:
            newState = cloneState(state)
            for m in move:
                newState[m] = newState[m] + 1
            newState['aa'] = newState['aa'] + 1
            if isValidState(newState):
                validStates.append(newState)

    # check going down
    if floor > 1:
        for move in moves:
            newState = cloneState(state)
            for m in move:
                newState[m] = newState[m] - 1
            newState['aa'] = newState['aa'] - 1
            if isValidState(newState):
                validStates.append(newState)

    return validStates

def stateToString(state):
    output = ''
    for c in sorted(state.keys()):
        output += str(state[c])
    return output

printComponents(initial)
print stateToString(initial)

visited = []
count = 0
done = False
currentStates = [initial]
while not done:
    count += 1
    moreStates = []
    for state in currentStates:
        moves = getValidMoves(state)
        nextStates = getNextStates(state, moves)
        #moreStates.extend(nextStates)
        for ns in nextStates:
            stateStr = stateToString(ns)
            if not stateStr in visited:
                visited.append(stateStr)
                moreStates.append(ns)
            if isDone(ns):
                print count
                exit()

    currentStates = moreStates

    print count, len(currentStates)
    if count > 60:
        exit()

print count

