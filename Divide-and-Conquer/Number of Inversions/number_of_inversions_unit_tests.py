import unittest
from number_of_inversions import compute_inversions, compute_inversions_naive
from random import randint


class TestNumberOfInversions(unittest.TestCase):
    def test_small(self):
        for array in [
            ([1, 2, 3]),
            ([3, 2, 1]),
            ([0,1,1])
        ]:
            self.assertEqual(compute_inversions(array),
                             compute_inversions_naive(array))

    def test_random(self):
        for n in (10, 100):
            for max_value in (1, 2, 10, 10 ** 5):
                array = [randint(0, max_value) for _ in range(n)]
                self.assertEqual(compute_inversions(array),
                                 compute_inversions_naive(array))

    def test_large(self):
        self.assertEqual(compute_inversions([1] * 100), 0)
        self.assertEqual(compute_inversions([1,2,4,3,5,7,6]), 2)

if __name__ == '__main__':
    unittest.main()
