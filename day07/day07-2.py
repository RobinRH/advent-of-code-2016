# 242
#
# https://adventofcode.com/2016/day/7

import sys
import pprint

with open(sys.argv[1], 'r') as inputFile:
    lines = inputFile.readlines()

def isPalindrome(s):
    return (s[0] == s[2]) and (s[0] != s[1])

supports = 0
for example in lines:
    inTextABA = set()
    inBracketABA = set()

    inText = True
    inBrackets = False

    example = example.strip()
    for i in range(0, len(example) - 2):
        if example[i] == '[':
            inBrackets = True
            inText = False

        if example[i] == ']':
            inBrackets = False
            inText = True

        chunk = example[i:i + 3]
        if (not '[' in chunk) and (not ']' in chunk):
            if isPalindrome(chunk):
                if inText:
                    inTextABA.add(chunk)
                if inBrackets:
                    inBracketABA.add(chunk)

    # now check each inTextABA and find out if it's in inBracketABA (but reversed)
    for aba in inTextABA:
        reverseABA = ''.join([aba[1], aba[0], aba[1]])
        if reverseABA in inBracketABA:
            supports += 1
            break # only want to cont each line once

    #print example, inTextABA, inBracketABA

print supports