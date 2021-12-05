from sys import argv
import copy

def countMoveOne(filename):
	pos = []
	flagt = 0

	with open(filename) as f:
			tempi = 0
			for line in f.readlines():
				tempj = 0
				for c in line:
					if(flagt == 0):
						pos.append([])
					#print(c)
					pos[tempj].append(line[tempj])
					tempj += 1

				flagt = 1
				tempi += 1
	pos.pop()
	print(pos)
	gamma = ""
	epsilon = ""

	for i in pos:
		ones = 0
		zeros = 0
		for j in i:
			if(j == "1"):
				ones += 1
			else:
				zeros += 1
		#print(ones)
		#print(zeros)
		if(ones > zeros):
			gamma += "1"
			epsilon += "0"
		else:
			gamma += "0"
			epsilon += "1"

	gamma = int(gamma,2)
	epsilon = int(epsilon,2)

	return gamma * epsilon

def countMove(filename):
	pos = []
	flagt = 0

	with open(filename) as f:
			tempi = 0
			for line in f.readlines():
				tempj = 0
				for c in line:
					if(flagt == 0):
						pos.append([])
					#print(c)
					pos[tempj].append(line[tempj])
					tempj += 1

				flagt = 1
				tempi += 1
	pos.pop()
	#print(pos)
	oxy = ""
	co2 = ""

	#controller
	#looper = 0
	delta = copy.deepcopy(pos)

	for theta in range(len(delta)):
		theta = findCo(delta,theta)

	for looper in range(len(pos)):
		pos = findOxy(pos,looper)

	#print(pos)

	for jz in pos:
		oxy += jz[0]

	for jy in theta:
		co2 += jy[0]


	return int(co2,2) * int(oxy,2)



def findOxy(pos2,targetdigit):
	ones = 0
	zeros = 0
	for j in pos2[targetdigit]:
		if(j == "1"):
			ones += 1
		else:
			zeros += 1

	#we know which to save here
	location = 0
	#print(ones)
	#print(zeros)
	todelete = [];
	if(zeros > ones):
		for digitplace in pos2[targetdigit]:
			if (digitplace == "1"):
				todelete.append(location)
			location += 1
	else:
		for digitplace in pos2[targetdigit]:
			if (digitplace == "0"):
				todelete.append(location)
			location += 1

	removed = 0
	for toremove in todelete:
		for iz in pos2:
			del iz[toremove-removed]
		removed += 1

	return pos2

def findCo(pos2,targetdigit):
	ones = 0
	zeros = 0
	for j in pos2[targetdigit]:
		if(len(pos2[targetdigit]) == 1):
			return pos2
		if(j == "1"):
			ones += 1
		else:
			zeros += 1

	#we know which to save here
	location = 0
	#print(ones)
	#print(zeros)
	todelete = [];
	if(zeros <= ones):
		for digitplace in pos2[targetdigit]:
			if (digitplace == "1"):
				todelete.append(location)
			location += 1
	else:
		for digitplace in pos2[targetdigit]:
			if (digitplace == "0"):
				todelete.append(location)
			location += 1

	removed = 0
	for toremove in todelete:
		for iz in pos2:
			del iz[toremove-removed]
		removed += 1

	return pos2


if __name__ == '__main__':
    #print("hello world")
    print(countMove(argv[1]))







