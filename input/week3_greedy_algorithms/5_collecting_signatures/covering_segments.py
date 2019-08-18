# Uses python3
import sys
from collections import namedtuple
from copy import deepcopy

# Segments have a start and end
Segment = namedtuple("Segment", "start end")


def optimal_points(segments):
    points = []
    # Sort by the smallest end ascending
    segments = sorted(segments, key=lambda x: x.end)
    point = segments[0].end
    points.append(point)

    for i in range(1, len(segments)):
        # If segment is not covered
        if point < segments[i].start or point > segments[i].end:
            # Add the ending point of the segment
            point = segments[i].end
            points.append(point)
    return points


if __name__ == "__main__":
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=" ")
