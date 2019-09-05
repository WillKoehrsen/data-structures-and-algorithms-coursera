import math
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


def dist(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


def brute_force(p, n):
    min_ = float("inf")
    for i in range(n):
        for j in range(i + 1, n):
            d = dist(p[i], p[j])
            if d < min_:
                min_ = d

    return min_


def strip_closest(strip, size, d):
    min_ = d
    for i in range(size):
        for j in range(i + 1, size):
            if strip[j].y - strip[i].y < min_:
                break
            d = dist(strip[i], strip[j])
            if d < min_:
                min_ = d

    return min_


def closest_util(px, py, n):
    if n <= 3:
        return brute_force(px, n)

    mid = n // 2
    mid_point = px[mid]

    pyl = [0] * (mid + 1)
    pyr = [0] * (n - mid - 1)

    li = 0
    ri = 0

    for i in range(n):
        if py[i].x <= mid_point.x:
            li += 1
            pyl[li] = py[i]
        else:
            ri += 1
            pyr[ri] = py[i]

    dl = closest_util(px, pyl, mid)
    dr = closest_util(px + mid, pyr, n - mid)

    d = min(dl, dr)

    strip = [0] * n
    j = 0
    for i in range(n):
        if abs(py[i].x - mid_point.x) < d:
            strip[j] = py[i]
            j += 1

    return min(d, strip_closest(strip, j, d))


def closest(xs, ys):
    ps = [Point(x, y) for x, y in zip(xs, ys)]
    px = sorted(ps, key=lambda x: x.x)
    py = sorted(ps, key=lambda x: x.y)

    return closest_util(px, py, len(px))
