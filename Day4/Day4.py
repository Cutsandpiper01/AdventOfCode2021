from sys import argv
import copy


def readBingo(filename):
		firstlinefile = 0
		numbersreadin = []
		groupby5 = 0
		boardholder = [[]]
		indexofboards = 0
		with open(filename) as f:
			for line in f.readlines():
				if(firstlinefile == 0):
					firstlinefile = 1
					numbersreadin = line.split(",")
				#elif(line == "\n"):
				#	print("Empty Line")	
				elif(groupby5 <= 4 and groupby5 >= 0):
					if(line != "\n"):	
						boardholder[indexofboards].append([])	
						#print(line)
						temparrread = line.split()
						#print(temparrread)
						#print("trying to index at " , indexofboards ," at 5s " , groupby5)
						for i1 in temparrread:
							boardholder[indexofboards][groupby5].append(int(i1))
						groupby5 += 1
				else:
					boardholder.append([])
					indexofboards += 1
					groupby5 = 0
		#bingoPrinter(boardholder)
		#for numin in numbersreadin:
		#print(len(boardholder))
		boardholder = playBingoToLose(boardholder,numbersreadin)
		#ifBingoMatch(boardholder[0])
		#bingoPrinter(boardholder)

def playBingoToLose(boards,numbers):
	remembernum = 0
	flagwinner = 0
	boardwinner = 0
	totalwonboards = 0
	numberofboards = len(boards)-1
	flagtrytowin = 0
	wonboards = []
	for number in numbers:
		for i,s in enumerate(boards):
			for j,t in enumerate(s):
				for k,u in enumerate(t):
						#print(u, " and ",number, " Exist?")
						if(int(u) == int(number)):
							#print(u, " and ",number, " Match!")
							#this may be my downfall depending on part 2 I really should use objects
							#Very not pretty
							boards[i][j][k] = -1

		#Here all boards are now updated with -1 where matches may be
		#print("Checking for win")
		boardindexer = 0
		for i in boards:
			#print(i)
			if(ifBingoMatch(i) and flagtrytowin == 0 and not boardindexer in wonboards):
				totalwonboards += 1
				#print(boardindexer)
				wonboards.append(boardindexer)
				print("Total won ",totalwonboards," total remain ", numberofboards-1)
				if(totalwonboards == numberofboards):
					print("One Board Remains")
					flagtrytowin = 1
			if(ifBingoMatch(i) and flagtrytowin == 1 and not boardindexer in wonboards):
				print("Made it into last match case")
				print("Last number ", number," Last Board ",boardindexer)
				print(boards[boardindexer])
				remembernum = number
				flagwinner = 1
				boardwinner = boardindexer;	
				wonboards.sort()
				print(wonboards)
			boardindexer += 1
		if(flagwinner == 1):
			break;

	#print("Match at ", remembernum, " on board ",boardwinner)
	print(calcBingoScore(boards[boardwinner],remembernum))
	return(boards)

def playBingoToWin(boards,numbers):
	remembernum = 0
	flagwinner = 0
	boardwinner = 0;
	for number in numbers:
		for i,s in enumerate(boards):
			for j,t in enumerate(s):
				for k,u in enumerate(t):
						#print(u, " and ",number, " Exist?")
						if(int(u) == int(number)):
							#print(u, " and ",number, " Match!")
							#this may be my downfall depending on part 2 I really should use objects
							#Very not pretty
							boards[i][j][k] = -1
		#Here all boards are now updated with -1 where matches may be
		#print("Checking for win")
		boardindexer = 0
		for i in boards:
			#print(i)
			if(ifBingoMatch(i)):
				#print("Bingo match ret true")
				remembernum = number
				flagwinner = 1
				boardwinner = boardindexer;	
			boardindexer += 1
		if(flagwinner == 1):
			break;
	#print("Match at ", remembernum, " on board ",boardwinner)
	print(calcBingoScore(boards[boardwinner],remembernum))
	return(boards)

def calcBingoScore(winboard,winnumber):
	sumt = 0
	for i in winboard:
		for j in i:
			if(j != -1):
				sumt += j
	return sumt * int(winnumber)

def ifBingoMatch(board):
	for i,s in enumerate(board):
		if(sum(s) == -5):
			return True
	colsboard = [sum(x) for x in zip(*board)]
	for i in colsboard:
		if(i == -5):
			return True
	return False


def bingoPrinter(boardlist):
	for i in boardlist:
		for j in i:
			print(j)
		print()


if __name__ == '__main__':
    #print("hello world")
    readBingo(argv[1])







