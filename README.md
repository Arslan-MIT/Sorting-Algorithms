# Quick Sort Algorithm

Quick Sort is an efficient, in-place sorting algorithm that uses the divide-and-conquer paradigm. Below is a detailed explanation:

## Time Complexity
- **Worst Case**: \( O(n^2) \)
  - Occurs when the pivot is always the smallest or largest element in the array.
- **Average Case**: \( O(n \log n) \)
  - Expected in most scenarios with a good pivot selection strategy.

## Key Features
- **Memory Efficiency**: Quick Sort uses in-place partitioning, requiring minimal additional memory compared to other sorting algorithms.
- **Versatile Performance**: Offers \( O(n \log n) \) average case time complexity, making it suitable for a wide range of applications.

## When to Use Quick Sort
- When memory usage needs to be minimized.
- When the average-case performance of \( O(n \log n) \) is acceptable for your application.

## Quick Sort Implementation in Python
```python
# Quick Sort Algorithm Implementation
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]  # Choosing the middle element as pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# Example Usage
if __name__ == "__main__":
    sample_array = [10, 7, 8, 9, 1, 5]
    print("Original Array:", sample_array)
    sorted_array = quick_sort(sample_array)
    print("Sorted Array:", sorted_array)
```

## Tips for Optimizing Quick Sort
- Use **randomized pivoting** to reduce the chances of encountering the worst-case scenario.
- Consider switching to a different sorting algorithm like **Insertion Sort** for small subarrays to improve efficiency.

---

Happy Sorting! :rocket:
