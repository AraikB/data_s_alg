import unittest
from organizing_lottery import points_cover, points_cover_naive


class PointsAndSegments(unittest.TestCase):
    def test_small(self):
        for starts, ends, points in [
            ([0, 7], [5, 10], [1, 6, 11]),
            ([0, 4], [5, 8], [2, 7, 13])
        ]:
            self.assertEqual(points_cover(list(starts), list(ends), list(points)),
                             points_cover_naive(starts, ends, points))

    def test_random(self):
        ([1,3], [5,6], [7,9,3])

    def test_large(self):
        ([100,1001], [2000,2150], [1120,1131,1231,1532,1593,2123,2143,2500])


if __name__ == '__main__':
    unittest.main()
