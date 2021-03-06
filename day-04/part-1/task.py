# cat sample | python3 task.py
# cat input | python3 task.py

#  Created by MikBac on 2021

bingoNumbersList = []
bingoNumbersList = input().strip().split(',')

ADDED_NUMBER = 'xxx'

winnerBox = []
winnerNumber = 0
winnerRestSum = 0

bingoTables = []
counter = -1
while True:
	try:
		line = input().strip().split()

		if len(line) == 0:
			bingoTables.append([])
			counter += 1
		else:
			bingoTables[counter].append(line)
	except EOFError:
		break


def getWinnerBox():
	global winnerNumber
	global winnerBox

	for randomNumber in bingoNumbersList:
		for box in range(len(bingoTables)):
			for line in range(len(bingoTables[box])):
				for numberInLine in range(len(bingoTables[box][line])):
					if randomNumber == bingoTables[box][line][numberInLine]:
						bingoTables[box][line][numberInLine] = ADDED_NUMBER

		for box in range(len(bingoTables)):
			for line in range(len(bingoTables[box])):
				lineCounter = 0
				for numberInLine in range(len(bingoTables[box][line])):
					if bingoTables[box][line][numberInLine] == ADDED_NUMBER:
						lineCounter += 1
				if lineCounter == 5:
					winnerNumber = randomNumber
					winnerBox = bingoTables[box]
					return

			for column in range(len(bingoTables[box])):
				columnCounter = 0
				for numberInColumn in range(len(bingoTables[box][column])):
					if bingoTables[box][numberInColumn][column] == ADDED_NUMBER:
						columnCounter += 1
				if columnCounter == 5:
					winnerNumber = randomNumber
					winnerBox = bingoTables[box]
					return


getWinnerBox()

for line in range(len(winnerBox)):
	for numberInLine in range(len(winnerBox[line])):
		if winnerBox[line][numberInLine] != ADDED_NUMBER:
			winnerRestSum += int(winnerBox[line][numberInLine])

print('winner Box: {}'.format(winnerBox))
print('winer number: {}'.format(winnerNumber))
print('winer rest sum: {}'.format(winnerRestSum))
print('resoult: {}'.format(winnerRestSum * int(winnerNumber)))
# winer number: 54
# winer rest sum: 639
# resoult: 34506
