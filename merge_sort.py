from typing import List

TIME_COMPLEXITY = {
    "best": "O(n log n)",
    "average": "O(n log n)",
    "worst": "O(n log n)",
}


def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr.copy()

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    merged: List[int] = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


if __name__ == "__main__":
    sample = [5, 3, 8, 4, 2, 7, 1, 6]
    print("Time Complexity:", TIME_COMPLEXITY)
    print("Original:", sample)
    print("Sorted  :", merge_sort(sample))
