def fun_1(num):
    tmp = num/2
    while(tmp*tmp<num):
        tmp+=1
    while(tmp*tmp-num>1e-4):
        tmp-=0.00001
    return tmp
if __name__ == '__main__':
    print(fun_1(2))