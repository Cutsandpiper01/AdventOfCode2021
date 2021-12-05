from sys import argv
import re

def navigate(filename,maxsize):
    mapocean = []
    valuestomap = []
    for i in range(maxsize):
        mapocean.append([])
        for j in range(maxsize):
            mapocean[i].append(0)

    with open(filename) as f:
        for line in f.readlines():
            temp = [int(d) for d in re.findall(r'\d+',line)]
            valuestomap.append(temp)
    #data is read in now
    for lines in valuestomap:
        mapocean = mapLine(lines,mapocean)

    #print(valuestomap)
    #printMap(mapocean)
    print(mapCounter(mapocean))

def mapCounter(mapocean):
    counter = 0
    for i in mapocean:
        for j in i:
            if(j >= 2):
                counter += 1
    return counter

def mapLine(line, mapocean):
    #print("Line 0 ",line[0]," to Line 1 ",line[1]," to Line 2 ", line[2]," to Line 3",line[3])
    #horizontal line means line 0 is stable
    if(line[0]-line[2] == 0):
        if(line[1] > line[3]):
            for i in range(line[1]-line[3]+1):
                mapocean[line[3]+i][line[0]] = mapocean[line[3]+i][line[0]] + 1
        else:
            for i in range(line[3]-line[1]+1):
                mapocean[line[3]-i][line[0]] = mapocean[line[3]-i][line[0]] + 1
    #vertical line means line 1 is stable
    elif(line[1]-line[3] == 0):
        if(line[0] > line[2]):
            for i in range(line[0]-line[2]+1):
                mapocean[line[1]][line[0]-i] = mapocean[line[1]][line[0]-i] + 1
        else:
            for i in range(line[2]-line[0]+1):
                mapocean[line[1]][line[2]-i] = mapocean[line[1]][line[2]-i] + 1
    #diagonal lines
    else:
        #print("invalid input")
        print("Line 0 ",line[0]," to Line 1 ",line[1]," to Line 2 ", line[2]," to Line 3",line[3])
        incrementx = 0;
        incrementy = 0;
        stablex = 0;
        if(line[0] > line[2] and line[1] > line[3]):
            #print("test got here with ",line[0], " ",line[1])
            incrementx = line[2]
            incrementy = line[3]
            stablex = line[0]
            while(incrementx != stablex+1):
               #print("making a dot at ", incrementx," ",incrementy)
                mapocean[incrementy][incrementx] = mapocean[incrementy][incrementx] + 1
                incrementx += 1
                incrementy += 1
        elif(line[0] < line[2] and line[1] < line[3]):
            #print("test got here with ",line[0], " ",line[1])
            incrementx = line[0]
            incrementy = line[1]
            stablex = line[2]
            while(incrementx != stablex+1):
                mapocean[incrementy][incrementx] = mapocean[incrementy][incrementx] + 1
                incrementx += 1
                incrementy += 1
        elif(line[0] < line[2] and line[1] > line[3]):
            #print("test got here with ",line[0], " ",line[1])
            incrementx = line[0]
            incrementy = line[1]
            stablex = line[2]
            while(incrementx != stablex+1):
                mapocean[incrementy][incrementx] = mapocean[incrementy][incrementx] + 1
                incrementx += 1
                incrementy -= 1
        else:
            #print("test got here with ",line[0], " ",line[1])
            incrementx = line[0]
            incrementy = line[1]
            stablex = line[2]
            while(incrementx != stablex-1):
                mapocean[incrementy][incrementx] = mapocean[incrementy][incrementx] + 1
                incrementx -= 1
                incrementy += 1


    return mapocean


def printMap(ocmap):
    for i in ocmap:
        print(i)

if __name__ == '__main__':
    navigate(argv[1],1000)
