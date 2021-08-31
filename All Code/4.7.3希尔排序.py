def shellsort(arr):
    step = len(arr) // 2
    while step > 0:
        for i in range(step, len(arr)):
            # 在索引为step到len（L）上，比较L[i]和L[i-step]的大小
            while i >= step and arr[i] < arr[i - step]:
                # 这里可以调整step从小到大或者从大到小排列
                arr[i], arr[i - step] = arr[i - step], arr[i]
                i -= step
        step //= 2
arr = [12,34,54,2,3]
shellsort(arr)
print(arr)
#pip install vprof -i https://pypi.tuna.tsinghua.edu.cn/simple