arr  = [64,25,12,22,11]
def InsertionSort(arr):
    for i in range(1,len(arr)):
      j = i-1
      key = arr[i]
      while j>=0 and j< key:
        arr[j+1] = arr[j]
        j-=1
        arr[j+1] = key
    return arr
print(InsertionSort(arr))



    
