# 33
# 11 (4), 15 (6), 25 (8), 33 (10), ?? (14) (+4, +10, +8) (+4, +14, +22, )
# https://adventofcode.com/2016/day/11

import itertools
import numpy as np 

# 33
initial = {
    'aa': 1,
    'rg': 1,
    'rm': 1,
    'bg': 2,
    'bm': 3,
    'cg': 2,
    'cm': 3,
    'tg': 2,
    'tm': 3,
    'lg': 2,
    'lm': 3
}

'''
# 25
initial = {
    'aa': 1,
    'rg': 1,
    'rm': 1,
    'bg': 2,
    'bm': 3,
    'cg': 2,
    'cm': 3,
    'tg': 2,
    'tm': 3
}
'''


'''
# 15
initial = {
    'aa': 1,
    'rg': 1,
    'rm': 1,
    'bg': 2,
    'bm': 3,
    'cg': 2,
    'cm': 3
}
'''

'''
# 11
initial = {
    'aa': 1,
    'hm': 1,
    'lm': 1,
    'hg': 2,
    'lg': 3
}
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
