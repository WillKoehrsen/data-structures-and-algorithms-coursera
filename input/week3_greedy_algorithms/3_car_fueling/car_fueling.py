# python3
import sys


def compute_min_refills(distance, tank, stops):
    current_position = 0
    fillups = 0
    new_stops = stops[:]
    while (current_position + tank) < distance:
        fillups += 1
        diffs = [stop for stop in new_stops if (stop - current_position) <= tank]
        if not diffs:
            return -1
        next_stop = max(diffs)
        current_position = next_stop
        new_stops.remove(next_stop)

    # write your code here
    return fillups


if __name__ == "__main__":
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
