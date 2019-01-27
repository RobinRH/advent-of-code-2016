# 1841611
# 
# https://adventofcode.com/2016/day/19

class Elf:

    def __init__(self, id):

        self.next = None
        self.elfId = id

# Solution uses a circlar linked list.

nElves = 5  # test case
nElves = 3017957

root = Elf(1)

current = root
for id in range(2, nElves + 1):
    newElf = Elf(id)
    current.next = newElf
    current = newElf
    newElf.next = root

elfCount = nElves
current = root
while elfCount > 1:
    current.next = current.next.next
    elfCount -= 1
    current = current.next

print current.elfId

