# Uses python3
import sys


def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)


d = {}


def f(n):
    if n == 1:
        return 1, -1
    if d.get(n) is not None:
        return d[n]
    ans = (f(n - 1)[0] + 1, n - 1)

    if n % 2 == 0:
        ret = f(n // 2)
        if ans[0] > ret[0]:
            ans = (ret[0] + 1, n // 2)

    if n % 3 == 0:
        ret = f(n // 3)
        if ans[0] > ret[0]:
            ans = (ret[0] + 1, n // 3)

    d[n] = ans
    return ans


def print_solution(n):
    ans = []

    while f(n)[1] != -1:
        ans.append(n)
        n = f(n)[1]

    ans.append(1)
    ans.reverse()
    return ans


def solve(n):
    for i in range(1, n):
        f(i)[0]
    ans = print_solution(n)
    return ans


if __name__ == "__main__":
    input = sys.stdin.read()
    n = int(input)
    sequence = list(solve(n))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=" ")
