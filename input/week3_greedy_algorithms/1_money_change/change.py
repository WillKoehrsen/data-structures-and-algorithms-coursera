# Uses python3
import sys

def get_change(m):
    tens = m // 10
    leftover = m % 10
    fives = leftover // 5
    return tens + fives + leftover % 5

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
