arr = [64,25,12,22,11]
def selectionSort(arr):
    for i in range(len(arr)-1):
        mini_idx = i
        for j in range(i+1,len(arr)):
            if arr[j]< arr[mini_idx]:
                mini_idx = j
        arr[i],arr[mini_idx] = arr[mini_idx],arr[i]
    return arr
            



print(selectionSort(arr))


    