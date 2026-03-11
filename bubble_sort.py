from typing import List

TIME_COMPLEXITY = {
    "best": "O(n)",
    "average": "O(n^2)",
    "worst": "O(n^2)",
}


def bubble_sort(arr: List[int]) -> List[int]:
    a = arr.copy()
    n = len(a)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break

    return a


if __name__ == "__main__":
    sample = [5, 3, 8, 4, 2, 7, 1, 6]
    print("Time Complexity:", TIME_COMPLEXITY)
    print("Original:", sample)
    print("Sorted  :", bubble_sort(sample))
