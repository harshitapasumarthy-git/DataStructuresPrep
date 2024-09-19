arr  = [64,25,12,22,11]
def merge_sort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        right = arr[mid:]
        left = arr[:mid]
        merge_sort(left)
        merge_sort(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[i]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
            k+=1

        while i<len(left):
            arr[k] = left[i]
            i+=1
            k+=1
        while j<len(right):
            arr[k] = right[j]
            j+=1
            k+=1
        return arr
print(merge_sort(arr))





    