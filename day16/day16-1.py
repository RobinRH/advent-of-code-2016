# 10111110010110110, 01101100001100100
#
# https://adventofcode.com/2016/day/16



def getNextString(a):

    #Make a copy of "a"; call this copy "b".
    #Reverse the order of the characters in "b".
    b = a[::-1]
    #In "b", replace all instances of 0 with 1 and all 1s with 0.
    b = b.replace('0', 'a').replace('1','0').replace('a', '1')
    #The resulting data is "a", then a single 0, then "b".
    return a + '0' + b

def getChecksum(d):

    # The checksum for some given data is created by considering each non-overlapping pair of characters in the input data. 
    # If the two characters match (00 or 11), the next checksum character is a 1. 
    # If the characters do not match (01 or 10), the next checksum character is a 0. 
    # This should produce a new string which is exactly half as long as the original. 
    # If the length of the checksum is even, repeat the process until you end up with a checksum with an odd length.
    checksum = ''
    for i in range(len(d) / 2):
        chars = d[i*2:i*2 + 2]
        checksum += '1' if chars[0] == chars[1] else '0'

    if len(checksum) % 2 == 0:
        return getChecksum(checksum)
    else:
        return checksum

# test data
#print getNextString('1')
#print getNextString('0')
#print getNextString('11111')
#print getNextString('111100001010')

# test
size = 20
data = '10000'

# real
size = 272
data = '10011111011011001'

while len(data) < size:
    data = getNextString(data)

print 'Part 1:', getChecksum(data[0:size])

size = 35651584
while len(data) < size:
    data = getNextString(data)

print 'Part 2:', getChecksum(data[0:size])
