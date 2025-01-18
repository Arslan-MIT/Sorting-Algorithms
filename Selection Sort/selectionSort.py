
# Selection Sort Algorithm Implementation
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Example Usage
if __name__ == "__main__":
    sample_array = [64, 25, 12, 22, 11]
    print("Original Array:", sample_array)
    selection_sort(sample_array)
    print("Sorted Array:", sample_array)
```
