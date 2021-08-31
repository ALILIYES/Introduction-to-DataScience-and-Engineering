def selectionSort(arr):
    for i in range(len(arr)-1):
        minindex = i
        for j in range(i+1,len(arr)):
            if(arr[j]<arr[minindex]):
                minindex = j
        if i != minindex:
            arr[i],arr[minindex] = arr[minindex],arr[i]
    return arr

if __name__ == "__main__":
    list = [5,3,1,2,4]
    selectionSort(list)
    print(list)
