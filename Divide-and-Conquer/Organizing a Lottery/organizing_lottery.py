# python3
from sys import stdin
import collections
from bisect import bisect_left, bisect_right


def points_cover_naive(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)

    for index, point in enumerate(points):
        for start, end in zip(starts, ends):
            if start <= point <= end:
                count[index] += 1

    return count


def points_cover(starts, ends, points):
    left_label, point_label, right_label = (1, 2, 3)
    count = [0] * len(points)

    # Regular dict object cannot be used here, because points are not unique.
    points_map = collections.defaultdict(set)

    pairs = []
    for i in starts:
        pairs.append((i, left_label))
    for i in ends:
        pairs.append((i, right_label))
    for i in range(len(points)):
        point = points[i]
        pairs.append((point, point_label))
        points_map[point].add(i)

    sorted_pairs = sorted(pairs, key=lambda p: (p[0], p[1]))

    coverage = 0
    for pair in sorted_pairs:
        if pair[1] == left_label:
            coverage += 1
        if pair[1] == right_label:
            coverage -= 1
        if pair[1] == point_label:
            indices = points_map[pair[0]]
            for i in indices:
                count[i] = coverage

    return count


if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    output_count = points_cover(input_starts, input_ends, input_points)
    print(*output_count)
