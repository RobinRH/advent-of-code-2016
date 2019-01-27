# 1423634
# 
# https://adventofcode.com/2016/day/19

class Elf:

    def __init__(self, id):

        self.next = None
        self.prev = None
        self.elfId = id

# This solution uses a doubly-linked circular list.
# One pointer points to the elf whose turn it is.
# Another pointer points to the middle elf.

nElves = 5 # test case
nElves = 11 # test case
nElves = 3017957

root = Elf(1)
a = 1

current = root
for id in range(2, nElves + 1):
    newElf = Elf(id)
    current.next = newElf
    newElf.prev = current
    current = newElf
    newElf.next = root
    a += 1

print a
root.prev = current


# find the half elf
halfElf = current
for i in range(nElves / 2 + 1):
    halfElf = halfElf.next

print 'first half elf', halfElf.elfId

ahead = 2
while nElves > 1:
    #print 'removed:', halfElf.elfId
    halfElf.prev.next = halfElf.next
    halfElf.next.prev = halfElf.prev
    if ahead == 2:
        halfElf = halfElf.next.next
    else:
        halfElf = halfElf.next

    if ahead == 2:
        ahead = 1
    else:
        ahead = 2

    nElves -= 1

print halfElf.elfId