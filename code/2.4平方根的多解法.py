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

def fun_3(num):
    g = num/2
    while(abs(g*g-num)>0.0000001):
        g = (g+num/g)/2
    return g
# def fun_4(num):

def main():
    print(fun_1(2))
    # print(fun_2(2))
    # print(fun_3(2))
    # print(fun_4(2))

if __name__ == '__main__':
    main()