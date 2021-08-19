import time
#级数pai = 16arctan(1/5)-4arctan(1/239)
#arctanx = x-x**3/3+x**5/5-x**7/7+x**9/9
def arctanx(x,times):
    res = x
    tmp = 1
    for i in range(times):
        if(tmp>0):
            tmp = -tmp
            tmp-=2
        else:
            tmp = -tmp
            tmp+=2
        res+=x**abs(tmp)/tmp
    return res

def getpai_1(times):
    return 16*arctanx(1/5,times)-4*arctanx(1/239,times)

#pai/4 = 1-1/3+1/5-1/7+1/9...
def getpai_2(num):
    res,tmp = 1.0,1
    for i in range(1,num):
        if(i%2==0):
            tmp = -tmp
            tmp+=2
        else:
            tmp = -tmp
            tmp-=2
        res+=(1/tmp)
    return 4*res

if __name__ == '__main__':
    print(getpai_1(1000000))
    # print(getpai_2(1000000))