# Uses python3

import sys


def is_greater_equal(a, b):
    if b == float("-inf"):
        return True
    # Direct comparison of order
    if "".join([str(a), str(b)]) >= "".join([str(b), str(a)]):
        return True
    return False


def largest_number(a):
    ans = []

    while a:
        max_digit = float("-inf")
        # Iterate through each remaining digit
        for digit in a:
            # Add if this digit results in a greater number
            if is_greater_equal(digit, max_digit):
                max_digit = digit
        # Add to answer and remove from list of digits
        ans.append(max_digit)
        a.remove(max_digit)

    return int("".join(ans))


if __name__ == "__main__":
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))

