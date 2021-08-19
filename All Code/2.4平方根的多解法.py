import random
import math
#循环迭代
def fun_1(num):
    guess = 0
    for i in range(num+1):
        if(i*i>=num):
            guess = i-1
            break
    while(abs(guess*guess-num)>=0.0001):
        guess += 0.00001
    return guess
#二分查找
def fun_2(num):
    if(num>=0):
        left,right = -num,num
    else:
        left,right = num,-num
    while((right-left)>1e-5):
        mid = (left+right)/2
        if(mid*mid>num):
            right = mid
        else:
            left = mid
    return right
#牛顿法
def fun_3(num):
    g = num/4
    while(abs(g*g-num)>0.0000001):
        g = (g+num/g)/2
    return g
#蒙特卡罗随机模拟
def fun_4(num):
    sum = 0
    for i in range(num):
        x = random.uniform(0,2)
        y = random.uniform(0,2)
        d = math.sqrt(x)-y
        if d > 0:sum+=1
    #area/(c*c) = sum/times
    #area = 4*sqrt(2)/3
    #sqrt(2) = 3*sum/times
    return (3*sum)/num

def main():
    # print(fun_1(2))
    # print(fun_2(2))
    print(fun_3(2000))
    # print(fun_4(100000))

if __name__ == '__main__':
    main()