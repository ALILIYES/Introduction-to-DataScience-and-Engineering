#循环
def M_1(a):
    m = a[0]
    for i in range(1,len(a)):
        if(a[i]<m):m = a[i]
    return m
#递归
def M_2(a):
    if(len(a)==1):return a[0]
    return min(a[len(a)-1],M_2(a[0:len(a)-1]))
#分治
def M_3(a):
    print(a)
    if(len(a)==1):return a[0]
    return min(M_3(a[0:int(len(a)/2)]),M_3(a[len(a)//2:len(a)]))

# L = [4,1,3,5]
# print(M_1(L))
# L = [4,1,3,5]
# print(M_2(L))
L = [4,1,3,5]
print(M_3(L))