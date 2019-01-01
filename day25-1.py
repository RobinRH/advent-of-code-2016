# 175
#
# https://adventofcode.com/2016/day/25

import sys
from pprint import pprint
import re
import string


with open(sys.argv[1], 'r') as inputFile:
    instructions = [s.strip() for s in list(inputFile)]

instructions = [line.split(' ') for line in instructions]

registers = {}
for letter in 'abcd':
    registers[letter] = 0

output = ''

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


def jnz(instruction, x, y):
    # if x (register or number) is not 0 then jump y (register or number)
    testvalue = int(x) if x[0] in '-0123456789' else registers[x]
    jump = int(y) if y[0] in '-0123456789' else registers[y]
    return instruction + jump if (testvalue != 0) else instruction + 1

def tgl(instruction, x, y):

    target = instruction + registers[x]

    if target < 0 or target >= len(instructions):
        print 'toggle had no effect'
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


def out(instruction, x, y):
    global output
    if x in string.ascii_lowercase:
        #print(registers[x])
        output += str(registers[x])
    else:
        #print(x)
        output += str(x)


    instruction += 1
    return instruction


opcodes = {
    'cpy' : cpy,
    'inc' : inc,
    'dec' : dec,
    'jnz' : jnz,
    'tgl' : tgl,
    'out' : out
}


def runWith(x):
    global output
    global registers

    instruction = 0
    output = ''
    registers = {}
    for letter in 'abcd':
        registers[letter] = 0
    
    registers['a'] = x

    count = 0
    while instruction < len(instructions) and instruction >= 0:
        tokens = instructions[instruction]
        opcode, x, y = tokens[0], tokens[1], tokens[2] if len(tokens) == 3 else None
        operator = opcodes[opcode]
        instruction = operator(instruction, x, y)
        #print registers
        if opcode == 'out':
            count += 1
        if count > 20:
            return

for x in range(200):
    runWith(x)
    #print x, ':', ''.join(output)
    if output.startswith('010101010101010101') or output.startswith('101010101010101010'):
        print 'found!', x
        exit()


