# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)
    value = 0
    data_sorted = sorted(list(zip(prices,weights)),key=lambda item: (item[0]/item[1],item[0]),reverse=True)
    for i in data_sorted:
        if capacity == 0:
            return value
        if i[1] <= capacity:
            value += i[0]
            capacity -= i[1]
        else:
            temp = float(i[0])/float(i[1])
            value += (temp*capacity)
            capacity = 0
    return value



if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
