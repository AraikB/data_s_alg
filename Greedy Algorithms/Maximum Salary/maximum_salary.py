# python3

from itertools import permutations
from functools import cmp_to_key

def largest_number_naive(numbers):

    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def largest_number(numbers):
    res = sorted(numbers, key = cmp_to_key(lambda i, j: -1
                if str(j) + str(i) < str(i) + str(j) else 1))
    bob = ''.join(map(str,res))
    res2=int(bob)
    return res2


if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
