# 479007760
#
# https://adventofcode.com/2016/day/23

import sys
from pprint import pprint
import re
import string

# This is the new code, using the two new opcode mul.
# There is also an add opcode, but when optimized, it's not needed
# Use the file input23-multiply.txt.

'''
cpy a b
dec b
cpy a d
cpy 0 a
cpy b c
mul d c
cpy c a
cpy 0 c 
cpy 0 d 
dec b
cpy b c
cpy c d
dec d
inc c
jnz d -2
tgl c
cpy -15 c
jnz 1 c
cpy 80 c
jnz 77 d
inc a
inc d
jnz d -2
inc c
jnz c -5
'''

def readInstructions():
    with open(sys.argv[1], 'r') as inputFile:
        instructions = map(lambda s : s.strip(), list(inputFile))

    instructions = [line.split(' ') for line in instructions]
    return instructions


registers = {}
for letter in 'abcd':
    registers[letter] = 0

def cpy(instruction, x, y):
    # copy x (int or register) to register y
    if not y in string.ascii_lowercase:
        return instruction + 1

    if x[0] in '-0123456789':
        registers[y] = int(x)
    else:
        registers[y] = registers[x]
    instruction += 1
    return instruction

def inc(instruction, x, y):
    if not x in string.ascii_lowercase:
        return instruction + 1

    registers[x] += 1    
    instruction += 1
    return instruction

def dec(instruction, x, y):
    if not x in string.ascii_lowercase:
        return instruction + 1

    registers[x] -= 1    
    instruction += 1
    return instruction

def add(instruction, x, y):
    # add x to y and assign to register y
    registers[y] += int(registers[x])
    return instruction + 1

def mul(instruction, x, y):
    # add x to y and assign to register y
    registers[y] *= int(registers[x])
    return instruction + 1

def jnz(instruction, x, y):
    # if x (register or number) is not 0 then jump y (register or number)
    testvalue = int(x) if x[0] in '-0123456789' else registers[x]
    jump = int(y) if y[0] in '-0123456789' else registers[y]
    return instruction + jump if (testvalue != 0) else instruction + 1

def tgl(instruction, x, y):

    target = instruction + registers[x]

    if target < 0 or target >= len(instructions):
        return instruction + 1

    #For one-argument instructions, inc becomes dec, and all other one-argument instructions become inc.
    #For two-argument instructions, jnz becomes cpy, and all other two-instructions become jnz.

    if instructions[target][0] == 'inc':
        instructions[target][0] = 'dec'
    elif instructions[target][0] == 'dec':
        instructions[target][0] = 'inc'
    elif instructions[target][0] == 'tgl':
        instructions[target][0] = 'inc'
    elif instructions[target][0] == 'jnz':
        instructions[target][0] = 'cpy'
    elif instructions[target][0] == 'cpy':
        instructions[target][0] = 'jnz'
    else:
        print target, 'bad instruction'

    return instruction + 1


opcodes = {
    'cpy' : cpy,
    'inc' : inc,
    'dec' : dec,
    'jnz' : jnz,
    'tgl' : tgl,
    'add' : add,
    'mul' : mul
}


for eggs in range(7, 13):
    registers = {'a': eggs, 'c': 0, 'b': 0, 'd': 0}
    instructions = readInstructions()
    instruction = 0
    while instruction < len(instructions) and instruction >= 0:
        tokens = instructions[instruction]
        opcode, x, y = tokens[0], tokens[1], tokens[2] if len(tokens) == 3 else None
        operator = opcodes[opcode]
        instruction = operator(instruction, x, y)

    print eggs, registers['a']

'''
7:      11200
8:      46480
9:     369040
10:   3634960
11:  39922960
12: 479007760
'''