# Uses python3
import sys
import math


def solve(ax, ay):
    a = list(zip(ax, ay))
    ax = sorted(a, key=lambda x: x[0])
    ay = sorted(a, key=lambda x: x[1])
    p1, p2, mi = closest_pair(ax, ay)
    return mi


def closest_pair(ax, ay):
    len_ax = len(ax)
    if len_ax <= 3:
        return brute(ax)

    mid = len_ax // 2
    q_x = ax[:mid]
    r_x = ax[mid:]

    midpoint = ax[mid][0]
    q_y = list()
    r_y = list()

    for x in ay:
        if x[0] <= midpoint:
            q_y.append(x)
        else:
            r_y.append(x)

    (p1, q1, mi1) = closest_pair(q_x, q_y)
    (p2, q2, mi2) = closest_pair(r_x, r_y)

    if mi1 <= mi2:
        d = mi1
        mn = (p1, q1)
    else:
        d = mi2
        mn = (p2, q2)

    (p3, q3, mi3) = closest_split_pair(ax, ay, d, mn)

    if d <= mi3:
        return mn[0], mn[1], d
    else:
        return p3, q3, mi3


def brute(ax):
    mi = dist(ax[0], ax[1])
    p1 = ax[0]
    p2 = ax[1]
    len_ax = len(ax)
    if len_ax == 2:
        return p1, p2, mi

    for i in range(len_ax - 1):
        for j in range(i + 1, len_ax):
            if i != 0 and j != 1:
                d = dist(ax[i], ax[j])
                if d < mi:
                    mi = d
                    p1, p2 = ax[i], ax[j]

    return p1, p2, mi


import math


def dist(x, y):
    return math.sqrt((x[1] - x[0]) ** 2 + (y[1] - y[0]) ** 2)


def closest_split_pair(p_x, p_y, delta, best_pair):
    len_x = len(p_x)
    mx_x = p_x[len_x // 2][0]

    s_y = [x for x in p_y if mx_x - delta <= x[0] <= mx_x + delta]
    best = delta
    len_y = len(s_y)
    for i in range(len_y - 1):
        for j in range(i + 1, min(i + 7, len_y)):
            p, q = s_y[i], s_y[j]
            dst = dist(p, q)
            if dst < best:
                best_pair = p, q
                best = dst

    return best_pair[0], best_pair[1], best


def minimum_distance(x, y):
    # write your code here
    return 10 ** 18


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    ax = (x + y)[::2]
    ay = (x + y)[1::2]
    print("{0:.9f}".format(solve(ax, ay)))
