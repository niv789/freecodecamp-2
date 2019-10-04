# Python program for implementation of Bubble Sort
def bubbleSort(arr):
    l = len(arr)
    # Traverse through all array elements
    for i in range(l):
         # Last i elements are already in place
        for j in range(0, l-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
