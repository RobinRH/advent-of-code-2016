# 12803
#
# https://adventofcode.com/2016/day/10
# run until there is one chip in outputs 0, 1, and 2

import sys
import pprint
import re

with open(sys.argv[1], 'r') as inputFile:
    lines = map(lambda s : s.strip(), list(inputFile))

#print '\n'.join(sorted(lines))

# value 23 goes to bot 208
# bot 125 gives low to bot 58 and high to bot 57
# bot 131 gives low to output 6 and high to bot 151
# bot 21 gives low to output 12 and high to output 19
valueExpr = re.compile('value (?P<value>\d+) goes to bot (?P<bot>\d+)')
giveExpr = re.compile('bot (?P<botId>\d+) gives low to (?P<lowWhich>[a-z]+) (?P<lowId>\d+) and high to (?P<highWhich>[a-z]+) (?P<highId>\d+)')

botRules = {}
botValues = []
for line in lines:
    valueMatch = valueExpr.match(line)
    giveMatch = giveExpr.match(line)
    if valueMatch:
        botValues.append((int(valueMatch.group('bot')), int(valueMatch.group('value'))))
    elif giveMatch:
        botId = int(giveMatch.group('botId'))
        lowWhich = giveMatch.group('lowWhich')
        lowId = int(giveMatch.group('lowId'))
        highWhich = giveMatch.group('highWhich')
        highId = int(giveMatch.group('highId'))
        botRules[botId] = (lowWhich, lowId, highWhich, highId)
    else:
        print "Error:", line
        exit()

# create output list
outputs = {}
for i in range(0, 21):
    outputs[i] = []

# create the bot list
bots = {}
for id in botRules.keys():
    bots[id] = []

# hand out all the values
for bot, value in botValues:
    bots[bot].append(value)

def botWithTwo():
    for id in bots.keys():
        if len(bots[id]) == 2:
            return id
        
    return -1

# now run rules until you find the bot that makes the 17, 61 comparison
while True:
    id = botWithTwo()
    chips = bots[id]
    (lowChip, highChip) = (chips[0], chips[1]) if (chips[0] < chips[1]) else (chips[1], chips[0])

    #if lowChip == 17 and highChip == 61:
    #    print 'found:', id
    #    #break

    if len(outputs[0]) == 1 and len(outputs[1]) == 1 and len(outputs[2]) == 1:
        print 'found: ', outputs[0][0] * outputs[1][0] * outputs[2][0]
        exit()

    lowWhich, lowId, highWhich, highId = botRules[id]
    # give the low chip
    if lowWhich == 'bot':
        bots[lowId].append(lowChip)
    else: 
        # it goes into outputs
        # we're not doing anything with the outputs
        outputs[lowId].append(lowChip)

    # give the high chip
    if highWhich == 'bot':
        bots[highId].append(highChip)
    else:
        outputs[highId].append(highChip)

    bots[id] = []

print outputs[0], outputs[1], outputs[2]

