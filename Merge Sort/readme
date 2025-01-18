
# Merge Sort Algorithm

Merge Sort is a stable, comparison-based sorting algorithm that follows the divide-and-conquer paradigm. Below is a detailed explanation:

## Time Complexity
- **Worst Case**: \( O(n \log n) \)
- **Average Case**: \( O(n \log n) \)
- **Best Case**: \( O(n \log n) \)

## Key Features
- **Stability**: Maintains the relative order of equal elements.
- **Memory Usage**: Requires additional memory for temporary arrays during merging.

## When to Use Merge Sort
- When stability is required.
- When working with large datasets where memory usage is not a constraint.

## Merge Sort Implementation in Python
```python
# Merge Sort Algorithm Implementation
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Example Usage
if __name__ == "__main__":
    sample_array = [12, 11, 13, 5, 6, 7]
    print("Original Array:", sample_array)
    merge_sort(sample_array)
    print("Sorted Array:", sample_array)
```
