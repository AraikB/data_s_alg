# python3


def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []

    bigger = n
    smaller = 1
    if n == 2 or n == 1:
        summands.append(n)
    else:
        for i in range(1,bigger):
            if bigger <= 2*smaller:
                summands.append(bigger)
                break
            else:
                summands.append(smaller)
                bigger = bigger - smaller
                smaller+=1

    return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
