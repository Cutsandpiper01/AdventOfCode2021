from sys import argv
import re


def navigate(filename,day):
    fishlist = [0,0,0,0,0,0,0,0,0]
    daysrun = 0
    with open(filename) as f:
        for line in f.readlines():
            #print(line)
            fishlisttemp = [int(d) for d in re.findall(r'\d+',line)]
            for tempfish in fishlisttemp:
                fishlist[tempfish] = fishlist[tempfish] + 1
    #print(fishlist)

    while(day != daysrun):
        #print("Day ", daysrun)
        #print(fishlist)
        fishlist = daySimFast(fishlist)
        daysrun += 1

    #print("Day ", daysrun)
    #print(fishlist)
    print(sum(fishlist))

def daySimFast(fishlist):
    tempzerofish = 0;
    for i,buckets in enumerate(fishlist):
        if(i == 0):
            tempzerofish = fishlist[0]
        else:
            fishlist[i-1] = fishlist[i]


    fishlist[6] += tempzerofish
    fishlist[8] = tempzerofish
    return fishlist



    return fishlist    

def daySim(fishlist):
    for i,fish in enumerate(fishlist):
        #print(fish)
        if(fishlist[i] == 0):
            fishlist[i] = 6
            fishlist.append(9)
            #print("zeroFish")
        else:
            #other things need to happen when young fish
            fishlist[i] = fishlist[i] - 1
    return fishlist


if __name__ == '__main__':
    navigate(argv[1],256)
