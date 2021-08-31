def quicksort(arr,l,r):
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
if __name__ == "__main__":
    list = [5,3,4,2,1]
    quicksort(list,0,len(list)-1)
    print(list)