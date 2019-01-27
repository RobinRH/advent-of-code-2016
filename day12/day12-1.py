# 318077
#
# https://adventofcode.com/2016/day/12

import sys
import pprint
import re
import string


with open(sys.argv[1], 'r') as inputFile:
    instructions = map(lambda s : s.strip(), list(inputFile))

'''
cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a
'''

registers = {}
for letter in string.ascii_lowercase:
    registers[letter] = 0

pprint.pprint(registers)

instruction = 0
while instruction < len(instructions):
    inst = instructions[instruction]
    tokens = inst.split(' ')
    if tokens[0] == 'cpy':
        if tokens[1][0] in '0123456789':
            registers[tokens[2]] = int(tokens[1])
        else:
            registers[tokens[2]] = registers[tokens[1]]
        instruction += 1
    elif tokens[0] == 'inc':
        registers[tokens[1]] += 1
        instruction += 1
    elif tokens[0] == 'dec':
        registers[tokens[1]] -= 1
        instruction += 1
    elif tokens[0] == 'jnz':
        if tokens[1][0] in '0123456789':
            if int(tokens[1]) != 0:
                instruction += int(tokens[2])
            else:
                instruction += 1
        else:
            if registers[tokens[1]] != 0:
                instruction += int(tokens[2])
            else:
                instruction += 1
    else:
        print 'instruction error'

print registers['a']
