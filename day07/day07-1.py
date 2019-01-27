# 110
#
# https://adventofcode.com/2016/day/7

import sys
import pprint

with open(sys.argv[1], 'r') as inputFile:
    lines = inputFile.readlines()

def isPalindrome(s):
    return (s[0] == s[3]) and (s[1] == s[2] and (s[0] != s[1]))

supports = 0
for example in lines:
    inText = True
    inBrackets = False

    hasTextAbba = False
    hasBracketAbba = False

    example = example.strip()
    for i in range(0, len(example) - 3):
        if example[i] == '[':
            inBrackets = True
            inText = False

        if example[i] == ']':
            inBrackets = False
            inText = True

        chunk = example[i:i + 4]
        if isPalindrome(chunk):
            if inText:
                hasTextAbba = True
            if inBrackets:
                hasBracketAbba = True

    if hasTextAbba and (not hasBracketAbba):
        supports +=1 

    # print example, hasTextAbba, hasBracketAbba

print supports