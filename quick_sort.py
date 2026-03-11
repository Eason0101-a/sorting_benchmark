from typing import List

TIME_COMPLEXITY = {
    "best": "O(n log n)",
    "average": "O(n log n)",
    "worst": "O(n^2)",
}


def quick_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr.copy()

    pivot = arr[len(arr) // 2]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return quick_sort(less) + equal + quick_sort(greater)


if __name__ == "__main__":
    sample = [5, 3, 8, 4, 2, 7, 1, 6]
    print("Time Complexity:", TIME_COMPLEXITY)
    print("Original:", sample)
    print("Sorted  :", quick_sort(sample))
