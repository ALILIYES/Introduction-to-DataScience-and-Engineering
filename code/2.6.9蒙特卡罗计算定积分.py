import random
import numpy as np

def fun(x):
    '''
    函数表达式的计算
    '''
    return x**2+4*x*np.sin(x)


def fun_max(left,right):
    '''
    计算出函数最高点
    '''
    max = 0
    for i in range(left*1000,right*1000,1):
        if(fun(i/1000)>max):max = fun(i/1000)
    return max

def ifinfun(x,y):
    '''
    判断是否在函数范围内
    '''
    if(fun(x)>=y):return True
    else:return False
#主函数
def main(left,right,times):
    count = 0
    max = fun_max(left,right)
    area = max*(right-left)
    for i in range(times):
        x = random.uniform(left,right)
        y = random.uniform(0,max)
        if(ifinfun(x,y)==True):count+=1
    return area*count/times

if __name__ == '__main__':
    print(main(2,3,10000000))