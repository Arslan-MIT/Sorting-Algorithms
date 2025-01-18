
# Bubble Sort Algorithm

Bubble Sort is a simple comparison-based sorting algorithm suitable for small datasets. Below is a detailed explanation:

## Time Complexity
- **Worst Case**: \( O(n^2) \)
- **Average Case**: \( O(n^2) \)
- **Best Case**: \( O(n) \) (when the array is already sorted)

## Key Features
- **Simplicity**: Easy to implement and understand.
- **Stability**: Maintains the relative order of equal elements.

## When to Use Bubble Sort
- When the dataset is small.
- When simplicity in implementation is preferred over performance.

## Bubble Sort Implementation in Python
```python
# Bubble Sort Algorithm Implementation
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example Usage
if __name__ == "__main__":
    sample_array = [64, 34, 25, 12, 22, 11, 90]
    print("Original Array:", sample_array)
    bubble_sort(sample_array)
    print("Sorted Array:", sample_array)
```
