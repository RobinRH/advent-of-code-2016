# gbhafcde
#
# https://adventofcode.com/2016/day/21

import sys
import pprint


filename = sys.argv[1]
with open(filename, 'r') as passwordFile:
    lines = [line.strip() for line in list(passwordFile)]

# input file has password, correct correctAnswer, and instrutions
password = lines[0]
correctAnswer = lines[1]

instructions = lines[2:]

# for all these, instruction is a string, password is a list
def swapPosition(instruction, password):
    # swap position 4 with position 0
    # swap position X with position Y : swap the letters at indexes X and Y (counting from 0)
    tokens = instruction.split(' ')
    x, y = int(tokens[2]), int(tokens[5])
    temp = password[x]
    password[x] = password[y]
    password[y] = temp
    return password

def swapLetter(instruction, password):
    # swap letter X with letter Y : the letters X and Y should be swapped (regardless of where they appear in the string).
    # swap letter d with letter b
    tokens = instruction.split(' ')
    x, y = tokens[2], tokens[5]
    password = ''.join(password)
    password = password.replace(x, '?')
    password = password.replace(y, x)
    password = password.replace('?', y)
    return list(password)


def reversePositions(instruction, password):
    # reverse positions X through Y : the span of letters at indexes X through Y 
    # (including the letters at X and Y) should be reversed in order.
    # reverse positions 0 through 4
    tokens = instruction.split(' ')
    x, y = int(tokens[2]), int(tokens[4])
    first = password[0:x]
    last = password[y+1:]
    middle = list(reversed(password[x:y+1]))
    password = first + middle + last
    return password

def rotateLR(instruction, password):
    # rotate left/right X steps : the whole string should be rotated; for example, e.g right 1, abcd -> dabc.
    # rotate left 1
    tokens = instruction.split(' ')
    direction, y = tokens[1], int(tokens[2])
    if direction == 'right':
        for i in range(y):
            last = list(password.pop())
            password = last + password
    else:
        for i in range(y):
            front = list(password.pop(0))
            password = password + front
    
    return password

def rotatePosition(instruction, password):
    # rotate based on position of letter X :
    # the whole string should be rotated to the right based on the index of letter X (counting from 0)
    # as determined before this instruction does any rotations. 
    # Once the index is determined, 
    # rotate the string to the right one time, plus a number of times equal to that index, 
    # plus one additional time if the index was at least 4.
    # rotate based on position of letter b
    # rotate based on position of letter d
    tokens = instruction.split(' ')
    x = tokens[6]
    location = password.index(x)
    times = 1 + location + (1 if location >= 4 else 0)
    for i in range(times):
        last = list(password.pop())
        password = last + password
    return password


def moveXY(instruction, password):
    # move position X to position Y : the letter which is at index X should be removed from the string,
    # then inserted such that it ends up at index Y.
    #move position 1 to position 4
    #move position 3 to position 0
    tokens = instruction.split(' ')
    x, y = int(tokens[2]), int(tokens[5])
    letter = password.pop(x)
    password.insert(y, letter)
    return password


functionMap = {
    'swap position' : swapPosition,
    'swap letter' : swapLetter,
    'reverse positions' : reversePositions,
    'rotate left' : rotateLR,
    'rotate right' : rotateLR,
    'move position' : moveXY,
    'rotate based' : rotatePosition
}


password = list(password)

for instruction in instructions:
    words = instruction.split(' ')
    command = ' '.join(words[0:2])
    password = functionMap[command](instruction, list(password))

print ''.join(password), correctAnswer

