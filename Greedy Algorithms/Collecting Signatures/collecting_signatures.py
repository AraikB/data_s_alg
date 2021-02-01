# python3

from collections import namedtuple
from sys import stdin

Segment = namedtuple('Segment', 'start end')


def compute_optimal_points(segments):
    sorted_segments = sorted(segments, key=lambda x: x.end)

    points = []
    while sorted_segments:
        # Place the first point to the right endpoint of the first segment.
        # Remove the segment, since it's considered as covered one.
        segment = sorted_segments.pop(0)
        point = segment.end
        points.append(point)

        # Check whether the point hit the other segments.
        for s in sorted_segments[:]:
            if s.start <= point <= s.end:
                sorted_segments.remove(s)

    return points


if __name__ == '__main__':
    n, *data = map(int, stdin.read().split())
    input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    assert n == len(input_segments)
    output_points = compute_optimal_points(input_segments)
    print(len(output_points))
    print(*output_points)
