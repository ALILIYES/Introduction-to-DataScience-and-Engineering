def quicksort(arr,l,r):
    '''快速排序'''
    if l>=r:return
    i,j,x = l,r,arr[l+r>>1]
    while i<j:
        while(arr[i]<x):i+=1
        while(arr[j]>x):j-=1
        if i<j:
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
            j-=1
    quicksort(arr,l,j)
    quicksort(arr,j+1,r)

def insertionSort(arr):
    '''插入排序'''
    for i in range(1,len(arr)):
        preindex = i-1
        cur = arr[i]
        while preindex>=0 and arr[preindex]>cur:
            arr[preindex+1] = arr[preindex]
            preindex-=1
        arr[preindex+1] = cur
    return arr

def selectionSort(arr):
    '''选择排序'''
    for i in range(len(arr)-1):
        minindex = i
        for j in range(i+1,len(arr)):
            if(arr[j]<arr[minindex]):
                minindex = j
        if i != minindex:
            arr[i],arr[minindex] = arr[minindex],arr[i]
    return arr

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
    list = [5,3,4,2,1]
    quicksort(list,0,len(list)-1)
    print(list)