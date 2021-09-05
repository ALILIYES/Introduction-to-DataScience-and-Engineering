import random

def randomlist(length):
    '''随机数列生成'''
    list = []
    for i in range(length):
        list.append(random.randint(1,100))
    return list

def bubblesort(list):
    '''冒泡排序'''
    n = len(list)
    for i in range(n):
        for j in range(n-i-1):
            if list[j]>list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]

def quicksort(list,l,r):
    '''快速排序'''
    if l>=r: return 0
    i,j,x = l,r,list[l+r>>1]
    while(i<j):
        while(list[i]<x):i+=1
        while(list[j]>x):j-=1
        if(i<j):
            list[i],list[j] = list[j],list[i]
            j-=1
            i+=1
    quicksort(list,l,j)
    quicksort(list,j+1,r)

def mergesort(list,tmp,l,r):
    '''归并排序'''
    if l>=r:return
    mid = l+r>>1
    mergesort(list,tmp,l,mid)
    mergesort(list,tmp,mid+1,r)
    i,j,k = l,mid+1,0
    while(i<=mid and j<=r):
        if(list[i]<list[j]):
            tmp[k]=list[i]
            k+=1;i+=1
        else:
            tmp[k]=list[j]
            k+=1;j+=1
    while(i<=mid):
        tmp[k] = list[i]
        k+=1;i+=1
    while(j<=r):
        tmp[k] = list[j]
        k+=1;j+=1
    j=0
    for i in range(l,r+1):
        list[i]=tmp[j]
        j+=1

if __name__ == "__main__":
    num = int(input("输入随机数列长度:"))
    list = randomlist(num)
    # bubblesort(list)
    # print(list)
    # quicksort(list,0,num-1)
    # print(list)
    tmp = [0]*(num+1)
    mergesort(list,tmp,0,num-1)
    print(list)
