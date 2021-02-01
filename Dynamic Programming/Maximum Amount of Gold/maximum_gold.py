# python3
import sys
from sys import stdin


def maximum_gold(capacity, weights):
    assert 1 <= capacity <= 10 ** 4
    assert 1 <= len(weights) <= 10 ** 3
    assert all(1 <= w <= 10 ** 5 for w in weights)
    def knapSack(W, wt, val, n):

        K = [[0 for x in range(W + 1)] for x in range(n + 1)]

        # Build table K[][] in bottom up manner
        for i in range(n + 1):
            for w in range(W + 1):
                if i == 0 or w == 0:
                    K[i][w] = 0
                elif wt[i-1] <= w:
                    K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
                else:
                    K[i][w] = K[i-1][w]

        return K[n][W]

    return knapSack(capacity, weights, weights, len(weights) )



if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
