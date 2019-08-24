# Uses python3
import sys
from collections import Counter


def get_majority_element(a, left, right):
    counts = Counter(a)
    most_common = counts.most_common(1)[0]

    if most_common[1] > len(a) / 2:
        return most_common[0]
    return 0


if __name__ == "__main__":
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
