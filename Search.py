# Binary Search implementation in python


def binarySearch(target,arr):
    low = 0
    high = len(arr) - 1
    while(low<= high):
        mid = (low + high) //2
        if(arr[mid]==target):
            print("Element is in index",mid)
            return mid
        elif arr[mid]<target:   #update low
            low = mid+1
        else:
            high= mid-1 #update high
    return -1
 

arr = [1,3,4,5,6,7,9]
target = 5
result = binarySearch(target,arr)
if result == -1:
    print("Element not present")


