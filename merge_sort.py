from typing import List

TIME_COMPLEXITY = {
    "best": "O(n log n)",
    "average": "O(n log n)",
    "worst": "O(n log n)",
}


def merge_sort(arr: List[int], trace: bool = False) -> List[int]:
    def _merge_sort(data: List[int], depth: int) -> List[int]:
        indent = "  " * depth
        if trace:
            print(f"{indent}[Merge] split: {data}")

        if len(data) <= 1:
            return data.copy()

        mid = len(data) // 2
        left = _merge_sort(data[:mid], depth + 1)
        right = _merge_sort(data[mid:], depth + 1)

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

        if trace:
            print(f"{indent}[Merge] merge: {left} + {right} -> {merged}")

        return merged

    return _merge_sort(arr, depth=0)


if __name__ == "__main__":
    sample = [5, 3, 8, 4, 2, 7, 1, 6]
    print("Time Complexity:", TIME_COMPLEXITY)
    print("Original:", sample)
    print("Sorted  :", merge_sort(sample))
