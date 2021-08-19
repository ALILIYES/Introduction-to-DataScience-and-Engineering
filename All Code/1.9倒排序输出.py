def for_sort(q,l,r):
    # 冒泡排序
    n = len(q)
    for i in range(n):
        for j in range(0,n-i-1):
            if(q[j]<q[j+1]):
                q[j],q[j+1] = q[j+1],q[j]

def while_sort(q,l,r):
    # 快速排序
    if(l>=r):return 0
    i,j,x=l,r,q[l+r>>1]
    while(i<j):
        while(q[i]>x):i+=1
        while(q[j]<x):j-=1
        if(i<j):
            q[i],q[j] = q[j],q[i]
            i+=1
            j-=1
    while_sort(q,l,j)
    while_sort(q,j+1,r)

if __name__ == "__main__": 
    L = [1,2,3,4,5]
    for_sort(L,0,len(L)-1)
    print(L)
    L = [1,2,3,4,5]
    while_sort(L,0,len(L)-1)
    print(L)