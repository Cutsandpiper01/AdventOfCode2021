from sys import argv
import re


def readScrambled(filename):
	listio = []
	with open(filename) as f:
		for line in f.readlines():
			tempstrlist = line.split("|")
			tempstrlist[1] = tempstrlist[1][:-1]
			listio.append(tempstrlist)
	#print(listio)
	ofse = 0
	for code in listio:
		ofse += int(decode(code))
	return ofse
#   0000
#  1    2
#  1    2
#   3333
#  4    5
#  4    5
#   6666



def decode(code):
	tempofse = ""
	digitkey = ["0"] * 7
	codekey = ["0"] * 10

	keylist = code[0].split(" ")[:-1]
	keylist = sorted(keylist,key=len)
	#print(keylist)

	codekey[1] = keylist[0]
	codekey[7] = keylist[1]
	codekey[8] = keylist[9]
	codekey[4] = keylist[2]

	tempdigkey = codekey[7].replace(codekey[1][1],"")
	digitkey[0] = codekey[7].replace(tempdigkey,"")

	# solve for zero nine and six
	for i in range(6,9):
		#print(keylist[i])
		onethree = codekey[4].replace(codekey[1][0],"")
		onethree = onethree.replace(codekey[1][1],"")
		if codekey[1][0] in keylist[i] and codekey[1][1] in keylist[i]:
			# If true i must be nine
			if onethree[0] in keylist[i] and onethree[1] in keylist[i]:
				codekey[9] = keylist[i]
			#otherwise is zero
			else:
				codekey[0] = keylist[i]
				if onethree[0] in codekey[0]:
					digitkey[3] = onethree[1]
					digitkey[1] = onethree[0]
				else:
					digitkey[3] = onethree[0]
					digitkey[1] = onethree[1]
		else:
			codekey[6] = keylist[i] 
			if codekey[1][0] in keylist[i]:
				digitkey[2] = codekey[1][1]
				digitkey[5] = codekey[1][0]
			else:
				digitkey[2] = codekey[1][0]
				digitkey[5] = codekey[1][1]
	#solve for three five and 
	for i in range(3,6):
		#must be 5
		if digitkey[1] in keylist[i]:
			codekey[5] = keylist[i]
		elif digitkey[5] in keylist[i]:
			codekey[3] = keylist[i]
		else:
			codekey[2] = keylist[i]

	for j,i in enumerate(codekey):
		#print(sorted(i))
		codekey[j] = "".join(sorted(i))

	#print("Digit Letters ", digitkey)
	#print("Codes ",codekey)
	temptotal = ""

	numlist = code[1].split(" ")[1:]
	for i in numlist:
		i = "".join(sorted(i))
		for j,code in enumerate(codekey):
			#print("Code ", code, " numlist ", i, " j ",j)
			if str(code) == str(i):
				temptotal += str(j)
	print(temptotal)

	return temptotal


def decodep1(code):
	tempofse = 0
	numlist = code[1].split(" ")[1:]
	print(numlist)
	for i in numlist:
		#print(len(i))
		if(len(i) == 2 or len(i) == 4 or len(i) == 3 or len(i) == 7):
			tempofse += 1

	return tempofse
if __name__ == '__main__':
    #print("hello world")
    print(readScrambled(argv[1]))







