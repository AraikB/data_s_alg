# python3


def lcm_naive(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    multiple = max(a, b)
    while multiple % a != 0 or multiple % b != 0:
        multiple += 1

    return multiple

def lcm(a, b) -> int:
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9
    def gcd(a, b):
        assert 0 <= a <= 2 * 10 ** 9 and 0 <= b <= 2 * 10 ** 9

        if b == 0:
            return a
        aprime = a%b
        return gcd(b,aprime)
    prod = a*b
    gcd = gcd(a,b)
    return int(prod/gcd)


if __name__ == '__main__':
    input_a, input_b = map(int, input().split())
    print(lcm(input_a, input_b))
