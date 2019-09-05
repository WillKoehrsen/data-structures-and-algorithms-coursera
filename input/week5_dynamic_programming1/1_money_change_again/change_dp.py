# Uses python3
import sys


def get_change(m):
    coins = [1, 3, 4]
    table = [float("inf") for _ in range(m + 1)]
    table[0] = 0

    coin_unique_count = len(coins)
    for i in range(1, m + 1):
        for j in range(coin_unique_count):
            if coins[j] <= i:
                sub_res = table[i - coins[j]]
                if (sub_res != float("inf")) and (sub_res + 1 < table[i]):
                    table[i] = sub_res + 1

    return table[m]


if __name__ == "__main__":
    m = int(sys.stdin.read())
    print(get_change(m))
