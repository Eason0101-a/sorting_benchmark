from typing import List

TIME_COMPLEXITY = {
    "best": "O(n log n)",
    "average": "O(n log n)",
    "worst": "O(n^2)",
}


def quick_sort(arr: List[int], trace: bool = False) -> List[int]:
    def _quick_sort(data: List[int], depth: int) -> List[int]:
        indent = "  " * depth

        if trace:
            print(f"{indent}[Quick] input: {data}")

        if len(data) <= 1:
            return data.copy()

        pivot = data[len(data) // 2]
        less = [x for x in data if x < pivot]
        equal = [x for x in data if x == pivot]
        greater = [x for x in data if x > pivot]

        if trace:
            print(
                f"{indent}[Quick] pivot={pivot}, less={less}, equal={equal}, greater={greater}"
            )

        left_sorted = _quick_sort(less, depth + 1)
        right_sorted = _quick_sort(greater, depth + 1)
        result = left_sorted + equal + right_sorted

        if trace:
            print(f"{indent}[Quick] combined: {result}")

        return result

    return _quick_sort(arr, depth=0)


if __name__ == "__main__":
    sample = [5, 3, 8, 4, 2, 7, 1, 6]
    print("Time Complexity:", TIME_COMPLEXITY)
    print("Original:", sample)
    print("Sorted  :", quick_sort(sample))
