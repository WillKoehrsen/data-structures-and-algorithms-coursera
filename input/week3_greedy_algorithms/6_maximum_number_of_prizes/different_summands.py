# Uses python3
import sys


def optimal_summands(n):
    if n == 1:
        return [1]
    summands = []
    # Amount still to allocate
    remainder = n

    for i in range(1, n):
        # Add next number if we can
        if remainder >= 2 * i + 1:
            summands.append(i)
            remainder -= i
        # Otherwise add leftover value and return
        else:
            summands.append(remainder)
            return summands

    return summands


if __name__ == "__main__":
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=" ")
