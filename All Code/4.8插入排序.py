def insertionSort(arr):
    for i in range(1,len(arr)):
        preindex = i-1
        cur = arr[i]
        while preindex>=0 and arr[preindex]>cur:
            arr[preindex+1] = arr[preindex]
            preindex-=1
        arr[preindex+1] = cur
    return arr

if __name__ == "__main__":
    list = [5,3,4,2,1]
    insertionSort(list)
    print(list)
