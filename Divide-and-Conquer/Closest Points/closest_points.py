# python3
from collections import namedtuple
from itertools import combinations
from math import sqrt
import time
import math

Point = namedtuple('Point', 'x y')


def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2


def minimum_distance_squared_naive(points):
    min_distance_squared = float("inf")

    for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared,
                                   distance_squared(p, q))

    return min_distance_squared


def minimum_distance_squared(points):

    def dist(p1, p2):
        return math.sqrt(((p2.x - p1.x)**2) +
                         ((p2.y - p1.y)**2))

    def bruteForce(P, n):
        min_d = dist(P[0], P[1])
        for i,(x,y) in enumerate(P):
            for j in range(i+1, n):
                if dist(P[i], P[j]) < min_d:
                    min_d = dist(P[i], P[j])

        return min_d

    def stripClosest(strip, d):
        lens = len(strip)
        for i in range(lens):
            for j in range(i+1, lens):
                if (strip[j][1] - strip[i][1]) < d and dist(strip[i], strip[j]) < d:
                    d = dist(strip[i], strip[j])
        return d

    def closestUtil(P, n) -> float:
        '''recursive function which splits the set of points into
        two halfs and repeats until size 3 or lower and then solves for min
        distance of each side back up to the desired'''
        if n <= 3:
            return bruteForce(P, n)

        mid = (n) // 2

        dl = closestUtil(P[:mid], mid)
        dr = closestUtil(P[mid:], n - mid)
        d = min(dl, dr)
        strip = []
        for i in range(len(P)):
            if abs(P[i].x - P[mid].x) < d:
                strip.append(P[i])
        strip.sort(key = lambda point: point.y)
        return min(d, stripClosest(strip, d))

    points.sort(key = lambda point: point.x)
    return closestUtil(points, len(points))**2



if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    print("{0:.9f}".format(sqrt(minimum_distance_squared(input_points))))
