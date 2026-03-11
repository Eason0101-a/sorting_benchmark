import argparse
import math
import random
import statistics
import time
from typing import Callable, Dict, List

from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort

Sorter = Callable[..., List[int]]


def time_once(sort_fn: Sorter, data: List[int], show_process: bool = False) -> float:
    if show_process:
        print(f"input : {data}")

    start = time.perf_counter()
    sorted_data = sort_fn(data, trace=show_process)
    end = time.perf_counter()

    if sorted_data != sorted(data):
        raise ValueError(f"{sort_fn.__name__} produced incorrect output")

    if show_process:
        print(f"output: {sorted_data}")
        print(f"elapsed(ms): {(end - start) * 1000.0:.4f}")

    return (end - start) * 1000.0


def benchmark(
    sizes: List[int],
    trials: int,
    lower: int,
    upper: int,
    seed: int,
    show_process: bool = False,
) -> Dict[str, Dict[int, List[float]]]:
    rng = random.Random(seed)

    algorithms: Dict[str, Sorter] = {
        "Quick Sort": quick_sort,
        "Merge Sort": merge_sort,
        "Bubble Sort": bubble_sort,
        "Insertion Sort": insertion_sort,
    }

    results: Dict[str, Dict[int, List[float]]] = {
        name: {n: [] for n in sizes} for name in algorithms
    }

    for n in sizes:
        datasets = [
            [rng.randint(lower, upper) for _ in range(n)] for _ in range(trials)
        ]

        for name, fn in algorithms.items():
            for trial_index, data in enumerate(datasets, start=1):
                if show_process:
                    print("=" * 72)
                    print(f"Algorithm: {name} | n={n} | trial={trial_index}/{trials}")
                elapsed_ms = time_once(fn, data, show_process=show_process)
                results[name][n].append(elapsed_ms)

    return results


def print_report(results: Dict[str, Dict[int, List[float]]], sizes: List[int]) -> None:
    header = (
        "Algorithm".ljust(16)
        + "n".rjust(8)
        + "avg(ms)".rjust(12)
        + "std(ms)".rjust(12)
        + "avg/(nlogn)".rjust(14)
        + "avg/(n^2)".rjust(14)
    )
    print(header)
    print("-" * len(header))

    for algo, size_map in results.items():
        for n in sizes:
            times = size_map[n]
            avg = statistics.mean(times)
            std = statistics.pstdev(times) if len(times) > 1 else 0.0
            nlogn = n * math.log2(max(n, 2))
            n2 = n * n

            print(
                f"{algo.ljust(16)}"
                f"{str(n).rjust(8)}"
                f"{avg:12.4f}"
                f"{std:12.4f}"
                f"{(avg / nlogn):14.8f}"
                f"{(avg / n2):14.8f}"
            )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Empirical time complexity comparison for sorting algorithms"
    )
    parser.add_argument(
        "--sizes",
        type=int,
        nargs="+",
        default=[100, 500, 1000, 2000],
        help="Input sizes to benchmark",
    )
    parser.add_argument(
        "--trials",
        type=int,
        default=5,
        help="Number of random arrays per size",
    )
    parser.add_argument(
        "--lower",
        type=int,
        default=0,
        help="Lower bound for random values",
    )
    parser.add_argument(
        "--upper",
        type=int,
        default=10000,
        help="Upper bound for random values",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed for reproducibility",
    )
    parser.add_argument(
        "--show-process",
        action="store_true",
        help="Print full sorting process for every algorithm and trial",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    sizes = sorted(set(args.sizes))
    if any(n <= 0 for n in sizes):
        raise ValueError("All sizes must be positive integers")

    results = benchmark(
        sizes=sizes,
        trials=args.trials,
        lower=args.lower,
        upper=args.upper,
        seed=args.seed,
        show_process=args.show_process,
    )
    print_report(results, sizes)


if __name__ == "__main__":
    main()
