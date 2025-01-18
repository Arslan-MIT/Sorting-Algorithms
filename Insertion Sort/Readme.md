
# Insertion Sort Algorithm

Insertion Sort is an efficient algorithm for small or partially sorted datasets. Below is a detailed explanation:

## Time Complexity
- **Worst Case**: \( O(n^2) \)
- **Average Case**: \( O(n^2) \)
- **Best Case**: \( O(n) \)

## Key Features
- **Stability**: Maintains the relative order of equal elements.
- **Simplicity**: Easy to implement and intuitive.

## When to Use Insertion Sort
- For small datasets.
- For nearly sorted datasets.

## Insertion Sort Implementation in Python
```python
# Insertion Sort Algorithm Implementation
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example Usage
if __name__ == "__main__":
    sample_array = [12, 11, 13, 5, 6]
    print("Original Array:", sample_array)
    insertion_sort(sample_array)
    print("Sorted Array:", sample_array)
```
