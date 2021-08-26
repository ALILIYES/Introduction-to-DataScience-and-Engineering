def multi(A):
    #正逆序
    tmpA,tmpB = [],[]
    tmp,n = 1,len(A)
    for i in range(n):
        tmp = tmp*A[i]
        tmpA.append(tmp)
    tmp = 1
    for i in range(n-1,-1,-1):
        tmp = tmp*A[i]
        tmpB.append(tmp)
    B = [tmpB[n-1]]
    for i in range(1,n-1):
        ta = tmpA[i-1]
        tb = tmpB[n-i-2]
        B.append(tmpA[i-1]*tmpB[n-i-2])
    B.append(tmpA[n-2])
    return B


if __name__ == "__main__":
    num = int(input("输入数组长度"))
    A = []
    for i in range(1,num):
        A.append(i)
    print(A)
    B = multi(A)