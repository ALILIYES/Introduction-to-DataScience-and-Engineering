#牛顿法
def fun_1(num):
    g = num/4
    while(abs(g*g*g-num)>0.0000001):
        g = (g+num/g)/2
    return g
if __name__ == '__main__':
    print(fun_1(8))