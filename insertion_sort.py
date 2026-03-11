from typing import List

TIME_COMPLEXITY = {
    "best": "O(n)",
    "average": "O(n^2)",
    "worst": "O(n^2)",
}


def insertion_sort(arr: List[int]) -> List[int]:
    a = arr.copy()

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key

    return a


if __name__ == "__main__":
    sample = [5, 3, 8, 4, 2, 7, 1, 6]
    print("Time Complexity:", TIME_COMPLEXITY)
    print("Original:", sample)
    print("Sorted  :", insertion_sort(sample))
