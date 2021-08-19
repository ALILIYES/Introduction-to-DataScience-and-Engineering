import random
def rollDie():
    return random.choice([1,2,3,4,5,6])

def checkPascal(numTrials):
    numwins = 0
    for i in range(numTrials):
        for i in range(24):
            if(rollDie()==6 and rollDie()==6):
                numwins+=1
                break
    print(numwins/numTrials)

def main():
    checkPascal(1000000)

if __name__ == '__main__':
    main()