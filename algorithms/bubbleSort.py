def bubbleSort(arr):
    l = len(arr)
    for i in range(l):
        for j in range(0, l-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
