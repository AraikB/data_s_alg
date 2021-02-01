# python3


def compute_operations(n):
    cache = [0] * (n + 1)  # 1
    for i in range(1, len(cache)):  # 2
        cache[i] = cache[i-1] + 1
        if i % 2 == 0:
            cache[i] = min(cache[i], cache[i // 2] + 1)
        if i % 3 == 0:
            cache[i] = min(cache[i], cache[i // 3] + 1)
    result = [1] * cache[-1]  # 1
    for i in range(1, cache[-1]):  # 2
        result[-i] = n  # 3
        if cache[n-1] == cache[n] - 1:  # 4
            n -= 1
        elif n % 2 == 0 and (cache[n // 2] == cache[n] - 1):  # 5
            n //= 2
        else:  # 6 # target % 3 == 0 and (cache[target // 3] == cache[target] - 1):
            n //= 3
    return result


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
