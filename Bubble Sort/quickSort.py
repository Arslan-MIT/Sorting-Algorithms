
def quickSort(arr, low, high):
    if low < high:
        pidx = partition(arr, low, high)
        quickSort(arr, low, pidx - 1)
        quickSort(arr, pidx+1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    i+=1
    arr[i], arr[high] = arr[high], arr[i]

    return i

array = [6,3,9,5,2,8]
n = len(array)
quickSort(array, 0, n-1)