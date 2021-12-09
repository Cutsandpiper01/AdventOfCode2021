from sys import argv
import re


def lowpoints(filename):
    maplow = []
    with open(filename) as f:
        for line in f.readlines():
            line = line[:-1]
            line = list(line)
            maplow.append(line)
    print(len(maplow))

    #find low points here
    result = calcbasin(maplow)

    #sumlow = 0
    #for i in result:
    #    sumlow += 1 + int(i)

    return result

def calcbasin(maplow):
    lowpoints = []
    basins = []
    for i,s in enumerate(maplow):
        flagtop = 0
        flagbottom = 0
        if(i == 0):
            flagtop = -1
        if(i == (len(maplow)-1)):
            flagbottom = -1
        for j,t in enumerate(maplow[i]):
            flagleft = 0
            flagright = 0
            if(j == 0):
                flagleft = -1
            else:
                flagleft = maplow[i][j-1] 
            if(j == len(maplow[i])-1):
                flagright = -1
            else: flagright = maplow[i][j+1] 
            if(flagtop != -1):
                flagtop = maplow[i-1][j]
            if(flagbottom != -1):
                flagbottom = maplow[i+1][j]                

            #Case for middle val top left right bottom
            #More typecasting!!! AGHHH
            #print("Thinking val ", maplow[i][j], " top ",flagtop," bottom ", flagbottom, " left ",flagleft, " right ",flagright)
            if((int(flagtop) > int(t) or int(flagtop) == -1) and (int(flagleft) > int(t) or int(flagleft) == -1) and (int(flagright) > int(t) or int(flagright) == -1) and (int(flagbottom) > int(t) or int(flagbottom) == -1)):
                #if true low point
                print("Adding val ", maplow[i][j], " top ",flagtop," bottom ", flagbottom, " left ",flagleft, " right ",flagright)
                lowpoints.append(maplow[i][j])
                #printmap(maplow)
                # Now to find the basin size
                basins.append(basinfinder(i,j,maplow))
                #print("Basin returns ",basin)

    basins.sort()
    print(basins)
    #printmap(maplow)

    return(basins[-1]*basins[-2]*basins[-3])

def basinfinder(i,j,maplow):
    #right
    sumpart = 1
    maplow[i][j] = 9
    if(j == len(maplow[i])-1):
        maplow[i][j] = 9
        #return 0
    elif(int(maplow[i][j+1]) < 9):
        maplow[i][j] = 9
        sumpart += basinfinder(i,j+1,maplow)
    #left
    if(j == 0):
        maplow[i][j] = 9
        #return 0
    elif(int(maplow[i][j-1]) < 9):
        maplow[i][j] = 9
        sumpart += basinfinder(i,j-1,maplow)
    #up
    if(i == 0):
        maplow[i][j] = 9
        #return 0
    elif(int(maplow[i-1][j]) < 9):
        maplow[i-1][j] = 9
        sumpart += basinfinder(i-1,j,maplow)
    #down
    if(i == (len(maplow)-1)):
        maplow[i][j] = 9
        #return 0
    elif(int(maplow[i+1][j]) < 9):
        maplow[i+1][j] = 9
        sumpart += basinfinder(i+1,j,maplow)
    return sumpart

def printmap(maplow):
    for i in maplow:
        print(i)


def calclowpart1(maplow):
    lowpoints = []
    for i,s in enumerate(maplow):
        flagtop = 0
        flagbottom = 0
        if(i == 0):
            flagtop = -1
        if(i == (len(maplow)-1)):
            flagbottom = -1
        for j,t in enumerate(maplow[i]):
            flagleft = 0
            flagright = 0
            if(j == 0):
                flagleft = -1
            else:
                flagleft = maplow[i][j-1] 
            if(j == len(maplow[i])-1):
                flagright = -1
            else: flagright = maplow[i][j+1] 
            if(flagtop != -1):
                flagtop = maplow[i-1][j]
            if(flagbottom != -1):
                flagbottom = maplow[i+1][j]                

            #Case for middle val top left right bottom
            #More typecasting!!! AGHHH
            #print("Thinking val ", maplow[i][j], " top ",flagtop," bottom ", flagbottom, " left ",flagleft, " right ",flagright)
            if((int(flagtop) > int(t) or int(flagtop) == -1) and (int(flagleft) > int(t) or int(flagleft) == -1) and (int(flagright) > int(t) or int(flagright) == -1) and (int(flagbottom) > int(t) or int(flagbottom) == -1)):
                #if true low point
                print("Adding val ", maplow[i][j], " top ",flagtop," bottom ", flagbottom, " left ",flagleft, " right ",flagright)
                lowpoints.append(maplow[i][j])

    return(lowpoints)


if __name__ == '__main__':
    print(lowpoints(argv[1]))
