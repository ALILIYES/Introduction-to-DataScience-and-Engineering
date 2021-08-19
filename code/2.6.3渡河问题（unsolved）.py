import numpy as np
path = []
def crossriver(arr,take):
    if(arr==np.ones(4,dtype=np.int32)):
        print(path)

def isobey(arr):
    #狼羊，羊菜不能在一起
    for i in arr:
        if(i[1]==1 and i[2]==1):return False
        if(i[1]==1 and i[3]==1):return False
    return True

def main():
    #索引从小到达分别表示人羊狼菜
    a = np.zeros(4,dtype=np.int32)
    print(a)

if __name__ == '__main__':
    main()