# password: 999828ec
# input: cxdnnyjw
# https://adventofcode.com/2016/day/5

import sys
import pprint
import hashlib

input = 'cxdnnyjw'
index = 0

#input = 'abc'

password = list('--------')
while '-' in password:
    string = input + str(index)
    m = hashlib.md5()
    m.update(string)
    digest = m.hexdigest()
    if str(digest).startswith("00000"):
        location = digest[5]
        newChar = digest[6]
        print index, location, newChar
        if (ord(location) <= ord('7')) and (password[int(location)] == '-'):
            password[int(location)] = newChar
        print ''.join(password)

    index += 1

print ''.join(password)