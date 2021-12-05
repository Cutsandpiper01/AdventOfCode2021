from sys import argv

def countIncrease(filename):
    try:
        with open(filename) as f:
                #how do I get max int?
                temp = 1000000000
                counter = 0

                for line in f.read().split():
                    line = int(line)
                    if(line > temp):
                        counter += 1
                    temp = line
                return counter
    except:
        exit("Couldn’t read numbers from file \""+filename+"\"")

def countIncreaseAdv(filename):
    with open(filename) as f:
                #how do I get max int?
                temp = 1000000000
                counter = 0
                queueCurrent = 0
                queue = []
                initial = 0

                for line in f.read().split():
                    line = int(line)
                    if initial < 2:
                        queue.append(line)
                        initial += 1
                        queueCurrent += line
                    else:
                        queue.append(line)
                        queueCurrent += line
                        print(queueCurrent)
                        if(temp < queueCurrent):
                            counter += 1
                        temp = queueCurrent
                        queueCurrent -= queue.pop(0)
                return counter


if __name__ == '__main__':
    #print("hello world")
    print(countIncreaseAdv(argv[1]))

