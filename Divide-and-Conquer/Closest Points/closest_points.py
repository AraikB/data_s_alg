# python3
from collections import namedtuple
from itertools import combinations
from math import sqrt
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
    def calc_distance(point_1, point_2):
        return math.sqrt(((point_2.x - point_1.x)**2) +
                         ((point_2.y - point_1.y)**2))

    def bruteForce(points, distance) -> float:
        '''Brute force function to calculate min distance of size 3 or smaller arrays'''
        minimum_distance = calc_distance(points[0], points[1])
        for i,(x,y) in enumerate(points):
            for j in range(i+1, len(points)):
                if calc_distance(points[i], points[j]) < minimum_distance:
                    minimum_distance = calc_distance(points[i], points[j])

        return minimum_distance

    def strip_distance(strip, distance) -> float:
        '''calculates the dista'''
        lens = len(strip)
        for i in range(lens):
            for j in range(i+1, lens):
                if (strip[j][1] - strip[i][1]) < distance and calc_distance(strip[i], strip[j]) < distance:
                    distance = calc_distance(strip[i], strip[j])
        return distance

    def reduce_work(points, lenpoints) -> float:
        '''recursive function which splits the set of points into
        two halves until length of each array is 3 solves and then
        combined the minimums back into distance which is even
        further reduced by strip'''
        if lenpoints <= 3:
            return bruteForce(points, lenpoints)
        #split arrays and solve for each half
        mid = (lenpoints) // 2
        leftHalf = reduce_work(points[:mid], mid)
        rightHalf = reduce_work(points[mid:], lenpoints - mid)

        #combine results into distance
        distance = min(leftHalf, rightHalf)
        strip = []
        for i in range(lenpoints):
            if abs(points[i].x - points[mid].x) < distance:
                strip.append(points[i])

        strip.sort(key = lambda point: point.y)

        return min(distance, strip_distance(strip, distance))

    points.sort(key = lambda point: point.x)
    return reduce_work(points, len(points))**2



if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    print("{0:.9f}".format(sqrt(minimum_distance_squared(input_points))))
