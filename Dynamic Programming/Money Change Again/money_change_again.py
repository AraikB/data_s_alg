# python3
import sys

def change_naive(money):
    min_coins = float("inf")

    for num1 in range(money + 1):
        for num3 in range(money // 3 + 1):
            for num4 in range(money // 4 + 1):
                if 1 * num1 + 3 * num3 + 4 * num4 == money:
                    min_coins = min(min_coins, num1 + num3 + num4)

    return min_coins


def change(money):
    coins = [1,3,4]
    m = len(coins)
    V=money
    table = [0 for i in range(V + 1)]

    for i in range(1, V + 1):
        table[i] = sys.maxsize

    for i in range(1, V + 1):
        for j in range(m):
            if (coins[j] <= i):
                sub_res = table[i - coins[j]]
                if (sub_res != sys.maxsize and
                    sub_res + 1 < table[i]):
                    table[i] = sub_res + 1
    return table[V]


if __name__ == '__main__':
    amount = int(input())
    print(change(amount))
