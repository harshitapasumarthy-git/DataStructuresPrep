arr = [64,25,12,22,11]
def partition(arr,low,high):
    pivot = high
    i = low -1
    for j in range(low,high):
        if arr[j] <= pivot:
            i+=1
            arr[i],arr[j]= arr[j],arr[i]
    arr[high],arr[i+1]= arr[i+1],arr[high]
    return i+1


def quick_sort(arr,low,high):
    if low<high:
        pivot = partition(arr,low,high)
        quick_sort(arr,low,pivot-1)
        quick_sort(arr,pivot+1,high)
    return arr

print(quick_sort((arr),0,len(arr)-1))


