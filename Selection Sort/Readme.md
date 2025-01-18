

# Selection Sort Algorithm

Selection Sort is a simple comparison-based sorting algorithm. Below is a detailed explanation:

## Time Complexity
- **Worst Case**: \( O(n^2) \)
- **Average Case**: \( O(n^2) \)
- **Best Case**: \( O(n^2) \)

## Key Features
- **In-Place Sorting**: Does not require additional memory.
- **Simplicity**: Easy to implement and understand.

## When to Use Selection Sort
- When the dataset is small.
- When simplicity is prioritized over performance.

## Selection Sort Implementation in Python
```python
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
