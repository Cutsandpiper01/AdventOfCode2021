from sys import argv
import re


def crabMove(filename):
    crabpos = []
    with open(filename) as f:
        for line in f.readlines():
            crabpos = [int(d) for d in re.findall(r'\d+',line)]
    crabpos.sort()
    #median = int(len(crabpos)/2)
    #median = crabpos[median]
    median = int(sum(crabpos)/len(crabpos))
    print(median)
            
    movesum = 0;

    for crab in crabpos:
    	#print("absolute value is ", abs(crab-median), " of crab ", crab , " and median ",median)
    	temp = abs(crab-median)
    	tempVal = 0
    	for i in range(temp+1):
    		tempVal += i
    	#print("Fuel Cost is: ",tempVal)
    	movesum += tempVal

    return movesum

def crabMovePart1(filename):
    crabpos = []
    with open(filename) as f:
        for line in f.readlines():
            crabpos = [int(d) for d in re.findall(r'\d+',line)]
    crabpos.sort()
    median = int(len(crabpos)/2)
    median = crabpos[median]
            
    movesum = 0;

    for crab in crabpos:

    	print("absolute value is ", abs(crab-median), " of crab ", crab , " and median ",median)
    	movesum += abs(crab-median)
    return movesum



if __name__ == '__main__':
    print(crabMove(argv[1]))
