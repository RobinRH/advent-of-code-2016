# password: f77a0e6e
# input: cxdnnyjw
# https://adventofcode.com/2016/day/5

import sys
import pprint
import hashlib

input = 'cxdnnyjw'
index = 0

password = ''
while len(password) < 8:
    string = input + str(index)
    m = hashlib.md5()
    m.update(string)
    digest = m.hexdigest()
    if str(digest).startswith("00000"):
        password += digest[5]

    index += 1

print password