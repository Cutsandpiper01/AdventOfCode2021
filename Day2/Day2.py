from sys import argv

def countMove(filename):
	with open(filename) as f:
			down = 0
			left = 0
			aim = 0
			for line in f.readlines():
				#print(line)
				temp = line.split()[0]
				add = int(line.split()[1])
				#print(add)
				#print(temp)
				if(temp == "forward"):
					left += add
					down += aim * add
				if(temp == "down"):
					#down += add
					aim += add
				if(temp == "up"):
					#down -= add
					aim -= add
	return down*left


def countIncreaseAdv(filename):
    return 0


if __name__ == '__main__':
    #print("hello world")
    print(countMove(argv[1]))







